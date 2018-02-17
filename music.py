
import subprocess
"""Used for calls to play music with MPD using MPC."""
import random
import sys


class some_song_names(object):
    """Define some song names that might be used."""

    IMAGINE = "John Lennon - Beatles (John Lennon) - Imagine All The People"
    DAN_LÅT = "Pointer Sisters - I'm So Excited"
    GET_IT_ON = "Marvin Gaye - Let's Get It On"
    MAD_WORLD = "Gary Jules - Mad World"
    LOSE_YOURSELF = "eminem_lose_yourself.mp3"
    SAMUEL_WAKE_UP = "samuel_wake_up.mp3"


SONGS = []


class Song(object):
    """Song object."""

    def __init__(self, name, id_number):
        """Constructor."""
        self.name = name
        self.id_number = id_number


def get_songs():
    """Set the global SONGS variable."""
    global SONGS

    songs_unformatted = subprocess.check_output("mpc playlist", shell=True)\
        .decode("utf-8").split("\n")

    if songs_unformatted[-1] != '':
        songs_formatted = songs_unformatted[:-1]
    else:
        songs_formatted = songs_unformatted[:-1]

    for id_number, name in enumerate(songs_formatted):
        SONGS.append(Song(name, id_number + 1))


def play_song(song):
    """Play a song object."""
    subprocess.call("mpc play " + str(song.id_number), shell=True)


def play_random_song():
    """Play random song from SONGS."""
    global SONGS

    option = random.choice(SONGS)

    play_song(option)


def play_song_by_name(name):
    """Play song by name - name."""
    global SONGS

    for song in SONGS:
        if song.name == name:
            play_song(song)
            return

    sys.stderr.write("Unable to play song " + name + " because it was not found")
    sys.stderr.flush()


def stop_song():
    """Stop playing current song."""
    subprocess.call("mpc stop", shell=True)


def next_song():
    """Play next song."""
    subprocess.call("mpc next", shell=True)


def prev_song():
    """Play prev song."""
    subprocess.call("mpc prev", shell=True)


def shuffle_songs():
    """Shuffle the playlist."""
    subprocess.call("mpc shuffle", shell=True)

    """Need to get new IDs for songs"""
    get_songs()


def set_volume(number):
    """Set volume, number between 0-100."""
    subprocess.call("mpc volume " + str(number), shell=True)


def toggle_play_pause():
    """Toggles play pause, plays if stopped."""
    subprocess.call("mpc toggle", shell=True)


def seek_to(percent):
    """Forward / Rewind to percent."""
    subprocess.call("mpc seek " + str(percent), shell=True)


get_songs()


