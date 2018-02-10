from requests_oauth2 import OAuth2
import requests
import json
import base64

with open("spotifyOauth", "r") as info_file:
    info = info_file.read().split()
    client_id = info[0]
    client_secret = info[1]

APIBASE = "https://api.spotify.com/"

def get_token():
    wierd_header = {"Authorization": "Basic " +\
        base64.standard_b64encode(bytes(client_id + ":" + client_secret, 
            "utf-8")).decode("utf-8")}

    print(wierd_header)
    body = {"grant_type": "client_credentials"}

    token = requests.post("https://accounts.spotify.com/api/token",
                          headers=wierd_header,
                          json=body)

    return token.text




# handler = OAuth2(client_id, client_secrent, "https://api.spotify.com"

print(client_id)
print(client_secret)
print(get_token())

