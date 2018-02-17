import requests
import scenes.lamps as lamps
import json
import sys

HOUSE_GROUPS = {
    "LivingRoom": ["V1", "V2", "V3", "Window"],
    "Kitchen": ["K1", "K2", "K3", "K4"],
    "BestRoom": ["Ball", "The Room"]
}


with open("apikey", "r") as apifile:
    APIKEY = apifile.read()[0:-1]
    API = "http://192.168.10.124/api/" + APIKEY


def get_lamps():
    """Getter for all lamp objects."""
    object_lamps = None
    try:
        object_lamps = json.loads(requests.get(API + "/lights").text)
    except Exception:
        sys.stderr.write("Unable to fetch lamps for HUE API, closing server")
        sys.exit(1)

    all_lamps = dict()
    for k, v in object_lamps.items():
        k = int(k)
        lamp = None
        if v['type'] == "Dimmable light":
            lamp = lamps.Dimmable.build(v, k)
        elif v['type'] == "Color temperature light":
            lamp = lamps.ColorTemperature.build(v, k)
        elif v['type'] == "Extended color light":
            lamp = lamps.ColorExtended.build(v, k)
        else:
            sys.stderr.write("Unrecognizable type " + v['type'])

        all_lamps[k] = lamp

    return all_lamps


LAMPS = get_lamps()


def get_house():
    """Define groups for house, there's a smarter way probably.. but cba."""
    global HOUSE_GROUPS
    global LAMPS

    groups = []
    """Might be abit slow if we get > 1000000 lamps"""
    for group_name, members in HOUSE_GROUPS.items():
        lamps_in_group = dict()
        for lamp_id, lamp in LAMPS.items():
            if lamp.name in members:
                lamps_in_group[lamp_id] = lamp

        groups.append(lamps.Group(group_name, lamps_in_group))

    return lamps.House(LAMPS, groups)

