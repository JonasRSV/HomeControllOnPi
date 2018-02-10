import pre_process
import time
import lamps


HOUSE = pre_process.get_house()

print(HOUSE)



VardagsLampa1 = HOUSE.lamps[1]

print(VardagsLampa1)

VardagsLampa1.turn_on()
VardagsLampa1.set_brigthness(200)
VardagsLampa1.set_transition_time(10)
VardagsLampa1.set_alert(lamps.Alerts.LSELECT)
VardagsLampa1.send_command()


DanLampa1 = HOUSE.lamps[16]
DanLampa1.turn_on()
DanLampa1.set_brigthness(200)
DanLampa1.set_effect(lamps.Effects.COLORLOOP)
DanLampa1.send_command()


time.sleep(7)

DanLampa1.set_effect(lamps.Effects.NONE)
DanLampa1.send_command()

time.sleep(2)

DanLampa1.turn_off()
DanLampa1.send_command()








