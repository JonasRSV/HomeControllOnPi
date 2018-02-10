import pre_process
import time
import lamps


HOUSE = pre_process.get_house()

print(HOUSE)

dan1 = HOUSE.lamps[16]
dan2 = HOUSE.lamps[17]
dan3 = HOUSE.lamps[18]

# dan1.set_effect(lamps.Effects.NONE)
# dan2.set_effect(lamps.Effects.NONE)
# dan3.set_effect(lamps.Effects.NONE)



dan1.set_effect(lamps.Effects.COLORLOOP)
dan2.set_effect(lamps.Effects.COLORLOOP)
dan3.set_effect(lamps.Effects.COLORLOOP)


# dan1.turn_on()
# dan2.turn_on()
# dan3.turn_on()


dan1.send_command()
time.sleep(1)
dan2.send_command()
time.sleep(1)
dan3.send_command()

