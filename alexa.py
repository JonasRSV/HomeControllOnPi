import sys
from multiprocessing import Process
from scenes import scenes
import random


class AUDIO_DIRECTIVES(object):
    """Class for audio directives."""

    STOP = {"type": "AudioPlayer.Stop"}

    def START(url):
        """Return directive for starting song at specific url."""
        return {
            "type": "AudioPlayer.Play",
            "playBehavior": "REPLACE_ALL",
            "audioItem": {
                    "stream": {
                        "token": "not sure what this is for tbh",
                        "url": url,
                        "offsetInMilliseconds": 0
                    }
            }
        }


def build_responselet(speech, directives):
    """Build a responselet for the response."""
    return {
        "outputSpeech": {
            "type": "PlainText",
            "text": speech
        },
        "reprompt": {},
        "directives": directives,
        "shouldSessionEnd": True
    }


def build_response(response):
    """Build a response in the expected format for Alexa."""
    return {
        "version": "1.0",
        "sessionAttributes": None,
        "response": response
    }


class REQUEST_TYPE(object):
    """Alexa Request Types."""

    START_INTERACTION = "LaunchRequest",
    INTENT = "IntentRequest"


def stop_handler(text="Raspi Out!"):
    """Handle stop intents."""
    return build_response(
        build_responselet(
            text,
            [AUDIO_DIRECTIVES.STOP]
        )
    )


def play_handler(text="Okay then", url=None):
    """Handle play intents such as starting music."""
    return build_response(
        build_responselet(
            text,
            [AUDIO_DIRECTIVES.START(url)]
        )
    )


def respond_handler(text="Okay then"):
    """Handle textual responses."""
    return build_response(
        build_responselet(
            text,
            []
        )
    )


def crash_handler():
    """Handle crashes."""
    return respond_handler("You sir have written bad code")


def undefined_behavior():
    """Initialize a interaction between Alexa and User."""
    return respond_handler("I'm no slave, fix your own shit")


class INTENT_HANDLERS(object):
    """Alexa Intents."""

    def handle(evt_name):
        """Handle incomming events."""
        sys.stdout.write("Recieved " + str(evt_name) + " Intent")
        sys.stdout.flush()

        if evt_name == "AMAZON.StopIntent" or evt_name == "AMAZON.PauseIntent":
            return stop_handler()

        for scene in scenes.SCENES:
            if scene.name == evt_name:
                if scene.lamp_function is not None:
                    Process(target=scene.lamp_function).start()

                if scene.music_url is not None:
                    return play_handler(scene.text, random.choice(scene.music_url))
                else:
                    return respond_handler(scene.text)

        return undefined_behavior()


def lambda_handler(event):
    """Entry point where requests is recieved and handled."""
    # sys.stdout.write(str(event))
    # sys.stdout.flush()
    try:
        request_type = event["request"]["type"]

        if request_type == REQUEST_TYPE.START_INTERACTION:
            return undefined_behavior()
        elif request_type == REQUEST_TYPE.INTENT:
            return INTENT_HANDLERS.handle(event["request"]["intent"]["name"])
        else:
            return undefined_behavior()
    except KeyError:
        sys.stderr.write("Alexa sent malformed request, probably.")
        return crash_handler()
    # except Exception as error:
        # sys.stderr.write(str(error))
        # sys.stderr.flush()
        # return crash_handler()

