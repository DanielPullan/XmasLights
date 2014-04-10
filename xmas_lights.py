## Dan's PyGlow Christmas Lights.
##
## The piglow can be bought from pimoroni.
## With thanks to Jason (@boeeerb) who wrote the PyGlow Python Module.

from pyglow import PyGlow

pyglow = PyGlow()


name = raw_input("What is your name?: ")
weather = raw_input("What does the weather look like today?: ")
val = input("How bright? (0-225): ")
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
	print("nothing here yet! ")
else:
	print("nothing for you here. ")


print "Well done ", name ," for completing this program on a ", weather ," day!"
