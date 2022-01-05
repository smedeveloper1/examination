#
# chk_anc.py
# for check angle and coords
# 2022/01/05 nakahie 
# add datetime info.
#
# 2021/12/17 nakahide
#
import datetime
import time
import os
import sys
from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle, Coord

sys.path.append(os.path.dirname(__file__))
from port_setup import setup
# 2021/11/01 nakahide
from port_setup import setup_naka
import RPi.GPIO as GPIO

reset = [153.19, 137.81, -153.54, 156.79, 87.27, 13.62]

# 2021/10/29 nakahide
def test(mycobot):
    print("\nStart check angle and coords")
    print(__file__)
###################################################################
# led test
###################################################################
# yellow
#    mycobot.set_color(255, 255, 0)
#    print("::set_color() ==> color {}\n".format("255 255 0"))
#    time.sleep(.5)
# pink
    mycobot.set_color(255, 0, 255)
#    print("::set_color() ==> color {}\n".format("255 0 255"))
    time.sleep(.5)
# blue
#    mycobot.set_color(0, 255,  255)
#    print("::set_color() ==> color {}\n".format("0 255 255"))
#    time.sleep(.5)
# white
    mycobot.set_color(255, 255, 255)
#    print("::set_color() ==> color {}\n".format("255 255 255"))
    time.sleep(.5)

###################################################################
#
# check angles
#
###################################################################
    dt_now=datetime.datetime.now()
    print(dt_now)
    print("::get_angles() ==> degrees: {}".format(mycobot.get_angles()))
    print("::get_coords() ==> coords: {}".format(mycobot.get_coords()))

    time.sleep(1)

# GPIO set output mode
    GPIO.setmode(GPIO.BCM)
# set vacuum ON!
    print("GPIO20,GPIO21 output-L => vacuum ON")
    GPIO.setup(20,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(21,GPIO.OUT,initial=GPIO.LOW)

    mycobot.wait(.5)

    print("GPIO20,GPIO21 output-H => vacuum OFF")
    GPIO.setup(20,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(21,GPIO.OUT,initial=GPIO.HIGH)

    mycobot.wait(.5)

    GPIO.cleanup(20)
    GPIO.cleanup(21)


#    print("::set_free_mode()\n")
#    mycobot.send_angles(reset, 50)
    time.sleep(1)
    mycobot.release_all_servos()

    print("=== check end ===\n")


if __name__ == "__main__":
    print(
        """
--------------------------------------------
| This file will test basic option method: |
|     set_led_color()                      |
|     send_angles()                        |
|     get_angles()                         |
|     send_angle()                         |
|     send_radians()                       |
|     get_radians()                        |
|     send_coords()                        |
|     get_coords()                         |
|     send_coord()                         |
--------------------------------------------
          """
    )
    time.sleep(3)
    # port = subprocess.check_output(['echo -n /dev/ttyUSB*'],
    # shell=True).decode()
    # with open(os.path.dirname(__file__) + "/port.txt") as f:
        # port = f.read().strip().replace("\n", "")
        # print(port)
# 2021/11/01 nakahide
#    mycobot = setup()
    mycobot = setup_naka()
    test(mycobot)
