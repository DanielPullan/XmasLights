## Xmas Lights by Dan Pullan (https://danielpullan.co.uk)
## Does some christmas-themed patterns on a Piglow, which can be bought from Pimoroni.
## Thanks to @boeeerb who wrote the PyGlow Python Module.
## Originally created for Python2 on 10/04/2014, rewritten for Python3 on 20/11/2018

from pyglow import PyGlow
import sys

pyglow = PyGlow()

val = input("How bright? (0-225): ")

if val < 0 or val > 255:
	print("Sorry, try again")
	sys.exit()

speedval = input("How fast? (500 recommended): ")


pyglow.all(0)

print("Check out my bright idea.")
pyglow.pulse(1, val, speedval)
pyglow.pulse(2, val, speedval)
pyglow.pulse(3, val, speedval)
pyglow.pulse(4, val, speedval)
pyglow.pulse(5, val, speedval)
pyglow.pulse(6, val, speedval)
pyglow.pulse(7, val, speedval)
pyglow.pulse(8, val, speedval)
pyglow.pulse(9, val, speedval)
pyglow.pulse(10, val, speedval)
pyglow.pulse(11, val, speedval)
pyglow.pulse(12, val, speedval)
pyglow.pulse(13, val, speedval)
pyglow.pulse(14, val, speedval)
pyglow.pulse(15, val, speedval)
pyglow.pulse(16, val, speedval)
pyglow.pulse(17, val, speedval)
pyglow.pulse(18, val, speedval)

arm_choice = input("Pick a number between 1 and 3: ")

if arm_choice < 0 or arm_choice > 3:
	sys.exit()

pyglow.pulse_arm(arm_choice, val, speedval)

pulse_choice = input("Pulse all? 1/0: ")
if pulse_choice == 1:
	pyglow.pulse_all(val, speedval)
else :
	print("Oh, okay then. :(") 


pulse_pattern = input("What pattern do you want? Choice between 1-5: ")
if pulse_pattern == 1:
	pyglow.pulse_all(val, speedval)
elif pulse_pattern == 2:
	pyglow.pulse_arm(1, val, speedval)
elif pulse_pattern == 3:
	pyglow.pulse(1, val, speedval)
	pyglow.pulse_arm(3, val, speedval)
elif pulse_pattern == [4,5]:
	print("nothing here yet!")
else:
	print("nothing for you here.")