import music
import lamps
import pre_process
import time


def run():
    """Run eminem wakeup."""
    HOUSE = pre_process.get_house()

    my_room_light = HOUSE.lamps[7]
    ball = HOUSE.lamps[19]

    my_room_light.turn_on()
    ball.turn_on()

    music.play_song_by_name(music.some_song_names.LOSE_YOURSELF)
    music.seek_to(34)
    music.set_volume(2)
    time.sleep(20)
    for i in range(10):
        music.set_volume(2 + i * 10)
        time.sleep(0.1)

    music.set_volume(100)
    ball.set_hue(25000)
    my_room_light.set_brigthness(250)
    ball.set_brigthness(250)
    ball.set_xy(0.4, 0.6)

    ball.set_alert(lamps.Alerts.LSELECT)
    my_room_light.set_alert(lamps.Alerts.LSELECT)

    my_room_light.send_command()
    ball.send_command()
    time.sleep(15)

    ball.set_hue(10000)
    ball.set_xy(0.7, 0.3)
    my_room_light.set_alert(lamps.Alerts.LSELECT)
    my_room_light.send_command()
    for _ in range(40):
        ball.set_alert(lamps.Alerts.SELECT)
        ball.send_command()
        time.sleep(0.5)

    ball.set_hue(0)
    for _ in range(35):
        ball.set_alert(lamps.Alerts.SELECT)
        ball.send_command()
        time.sleep(0.6)

    music.stop_song()
    music.play_song_by_name(music.some_song_names.SAMUEL_WAKE_UP)
    time.sleep(7)
    music.stop_song()

