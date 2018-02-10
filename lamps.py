import sys
import requests
import json

"""
I've yet to implement most of the inc functions because
I see no real usecase for them.
"""

with open("apikey", "r") as apifile:
    APIKEY = apifile.read()[0:-1]
    API = "http://192.168.10.124/api/" + APIKEY + "/lights/"


class Effects(object):
    """All effects available for HUE at 10 feb 2018."""

    NONE = "none"
    COLORLOOP = "colorloop"


class Alerts(object):
    """All alerts available for HUE at 10 feb 2018."""

    NONE = "none"
    SELECT = "select"
    LSELECT = "lselect"


class Lamp(object):
    """Base class for Lamp."""

    def build(lamp, id_number):
        """Build lamp from request."""
        on = bool(lamp['state']['on'])
        name = lamp['name']

        return Lamp(id_number, name, on)

    def __init__(self, id_number, name, on):
        """Constructor."""
        self.id_number = id_number
        self.name = name
        self.on = on
        self.command = dict()

    def __str__(self):
        """Overloaded toString method."""
        return self.name + " " + str(self.id_number) + " " + str(self.on)

    def turn_off(self):
        """Turn the light off."""
        self.on = False
        self.command["on"] = False

    def turn_on(self):
        """Turn the light on."""
        self.on = True
        self.command["on"] = True

    def send_command(self):
        """Send the command."""
        requests.put(API + str(self.id_number) + "/state",
                     data=json.dumps(self.command))


class Dimmable(Lamp):
    """Class for Dimmable Light."""

    def build(lamp, id_number):
        """Build Dimmaple from request."""
        on = bool(lamp['state']['on'])
        name = lamp['name']
        bri = int(lamp['state']['bri'])
        alert = lamp['state']['alert']

        return Dimmable(id_number, name, on, bri, alert)

    def __init__(self, id_number, name, on, bri, alert):
        """Constructor."""
        self.bri = bri
        self.alert = alert
        Lamp.__init__(self, id_number, name, on)

    def __str__(self):
        """Overloaded toString method."""
        return self.name + " " + str(self.id_number) + " " + str(self.on)\
            + " " + str(self.bri) + " " + str(self.alert)

    def set_brigthness(self, bri):
        """Set brigthness of lamp."""
        self.bri = bri % 256
        self.command["bri"] = self.bri

    def set_alert(self, alert):
        """Set alert of a lamp."""
        self.alert = alert
        self.command["alert"] = self.alert

    def set_transition_time(self, transition_time):
        """Set transition time for this command in number of 100s of ms."""
        self.command["transitiontime"] = transition_time


class ColorTemperature(Dimmable):
    """Class for Color Temperature Light."""

    def build(lamp, id_number):
        """Build ColorTemerature from request."""
        on = bool(lamp['state']['on'])
        name = lamp['name']
        bri = int(lamp['state']['bri'])
        ct = int(lamp['state']['ct'])
        alert = lamp['state']['alert']

        return ColorTemperature(id_number, name, on, bri, ct, alert)

    def __init__(self, id_number, name, on, bri, ct, alert):
        """Constructor."""
        self.ct = ct
        Dimmable.__init__(self, id_number, name, on, bri, alert)

    def __str__(self):
        """Overloaded toString method."""
        return self.name + " " + str(self.id_number) + " " + str(self.on)\
            + " " + str(self.bri) + " " + str(self.ct) + " " + str(self.alert)

    def set_ct(self, ct):
        """Set the temperature, values between 153 -> 500 works."""
        self.ct = ct
        self.command["ct"] = self.ct

    def set_alert(self, alert):
        """Set alert of lamp."""
        self.alert = alert
        self.command["alert"] = self.alert


class ColorExtended(ColorTemperature):
    """Class for Color Extended Light."""

    def build(lamp, id_number):
        """Build ColorExtended from request."""
        on = bool(lamp['state']['on'])
        name = lamp['name']
        bri = int(lamp['state']['bri'])
        ct = int(lamp['state']['ct'])
        alert = lamp['state']['alert']
        sat = int(lamp['state']['sat'])
        hue = int(lamp['state']['hue'])
        xy = lamp['state']['xy']
        effect = lamp['state']['effect']

        return ColorExtended(id_number, name, on, bri,
                             ct, alert, sat, hue, xy, effect)

    def __init__(self, id_number, name, on, bri,
                 ct, alert, sat, hue, xy, effect):
        """Constructor."""
        self.sat = sat
        self.hue = hue
        self.xy = xy
        self.effect = effect
        ColorTemperature.__init__(self, id_number, name, on, bri, ct, alert)

    def __str__(self):
        """Overloaded toString method."""
        return self.name + " " + str(self.id_number) + " " + str(self.on)\
            + " " + str(self.bri) + " " + str(self.ct) + " " + str(self.sat)\
            + " " + str(self.hue) + " " + str(self.xy) + " " + str(self.alert)\
            + " " + str(self.effect)

    def set_hue(self, hue):
        """Set hue of lamp."""
        self.hue = hue
        self.command["hue"] = self.hue

    def set_sat(self, sat):
        """Set sat of lamp."""
        self.sat = sat
        self.command["sat"] = self.sat

    def set_xy(self, x, y):
        """Set xy of lamp."""
        self.xy = {"0": x, "1": y}
        self.command["xy"] = self.xy

    def set_effect(self, effect):
        """Set effect of lamp."""
        self.effect = effect
        self.command["effect"] = self.effect


class Group(object):
    """Class for House Groups."""

    def __init__(self, name, lamps=dict()):
        """Constructor."""
        self.name = name
        self.lamps = lamps

    def __str__(self):
        """Overloaded toString method."""
        group = "Name: " + self.name + "\n"
        for _, v in self.lamps.items():
            group += str(v) + "\n"

        return group


class House(object):
    """Class for House functionalities."""

    def __init__(self, lamps=dict(), groups=[]):
        """Constructor."""
        self.lamps = lamps
        self.groups = groups

    def __str__(self):
        """Overloaded toString method."""
        house = "*** House ***\n\n"
        house += "Groups:\n"

        for group in self.groups:
            house += str(group) + "\n"

        house += "\nLamps:\n"

        for _, v in self.lamps.items():
            house += str(v) + "\n"

        return house
