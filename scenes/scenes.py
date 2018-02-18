import time
import scenes.lamp_functions as lf


class Scene(object):
    """Scene object."""

    def __init__(self, name, text="Okay then.", music_url=None, lamp_function=None):
        """Constructor."""
        self.name = name
        self.text = text
        self.music_url = music_url
        self.lamp_function = lamp_function

def get_song(name):
    return open("scenes/music/" + name, "r").read()[0:-1]

SCENES = [
    Scene("Imagine", "Imagine some stuff, okay?", [get_song("imagine_jl")], lf.lf1),
    Scene("Chill", "Chillax", [get_song("timber")], lf.lf1),
    Scene("Wakeup", "Wake up sleepy", [get_song("lejon_konung")], lf.all_lamps_slow),
    Scene("Home", "Welcome home, sir", [get_song("am")], lf.all_lamps_slow)
    ]


