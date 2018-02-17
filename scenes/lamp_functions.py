import scenes.lamps as lamps
import scenes.pre_process as pre_process
import time

def lf1():
    """Controll Lamps."""
    HOUSE = pre_process.get_house()

    v1 = HOUSE.lamps[1]
    v2 = HOUSE.lamps[2]
    v3 = HOUSE.lamps[3]
    window = HOUSE.lamps[5]
    ball = HOUSE.lamps[19]

    active_lamps = set()
    active_lamps.add(v1.id_number)
    active_lamps.add(v2.id_number)
    active_lamps.add(v3.id_number)
    active_lamps.add(window.id_number)
    active_lamps.add(ball.id_number)

    for id_num, lamp in HOUSE.lamps.items():
        if id_num not in active_lamps:
            lamp.turn_off()
            lamp.set_transition_time(50)
            lamp.send_command()

    time.sleep(6)

    v1.turn_on()
    v2.turn_on()
    v3.turn_on()
    window.turn_on()
    ball.turn_on()

    v1.set_brigthness(30)
    v2.set_brigthness(30)
    v3.set_brigthness(30)

    window.set_brigthness(200)
    window.set_transition_time(50)
    window.set_ct(500)

    ball.set_brigthness(100)
    ball.set_transition_time(50)
    ball.set_hue(43690)
    ball.set_sat(254)
    ball.set_xy(0.1691, 0.0441)

    v1.send_command()
    v2.send_command()
    v3.send_command()
    window.send_command()
    ball.send_command()


def all_lamps_slow():
    """Turn on all lamps in the house in 50 seconds."""
    HOUSE = pre_process.get_house()

    for id_num, lamp in HOUSE.lamps.items():
        lamp.turn_on()
        lamp.set_transition_time(500)
        lamp.set_brigthness(254)
        lamp.send_command()

