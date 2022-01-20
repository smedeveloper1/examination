# make _coords_angles.py
# for getting machine learning tesching data
# 2022/01/17 nakahide
# umaku atai torenai koto ga ikutumo aru => umaku ikanai?
#
# make_angles_coords.py
# for getting machine learning teaching data
# 2022/01/17 nakahide
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
import random
import numpy as np
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

# speed setting
    fast=80
    slow=10
# model setting 0:non-linear/1:linear
    linear_model=0

    for i in range(10):
#        j1=random.randint(-90.0,160.0)
#        j2=random.randint(-20.0,80.0)
#        j3=random.randint(-20.0,120.0)
#        j4=random.randint(-20.0,120.0)
#        j5=random.randint(-90.0,90.0)
#        j6=random.randint(-45.0,45.0)
        c_x=random.randint(-260.0,260.0)
        c_y=random.randint(-280.0,0.0)
        c_z=random.randint(10.0,410.0)
        c_rx=random.randint(80.0,100.0)
        c_ry=random.randint(-10.0,10.0)
        c_rz=random.randint(-180.0,0.0)
#        print(j1,j2,j3,j4,j5,j6)
#        random_j1_j6=[j1,j2,j3,j4,j5,j6]
        np_ran_c_x_c_rz=np.array([c_x,c_y,c_z,c_rx,c_ry,c_rz])
#        print(random_j1_j6)
#        print(np_ran_j1_j6)
#        mycobot.send_angels(random_j1_j6,slow)
        mycobot.send_coords(np_ran_c_x_c_rz,slow,linear_model)
        print("::get_coords() ==> coords: {}".format(mycobot.get_coords()))
        print("::get_angles() ==> degrees: {}".format(mycobot.get_angles()))
        time.sleep(5)

# GPIO set output mode
#    GPIO.setmode(GPIO.BCM)
# set vacuum ON!
#    print("GPIO20,GPIO21 output-L => vacuum ON")
#    GPIO.setup(20,GPIO.OUT,initial=GPIO.LOW)
#    GPIO.setup(21,GPIO.OUT,initial=GPIO.LOW)

#    mycobot.wait(.5)

#    print("GPIO20,GPIO21 output-H => vacuum OFF")
#    GPIO.setup(20,GPIO.OUT,initial=GPIO.HIGH)
#    GPIO.setup(21,GPIO.OUT,initial=GPIO.HIGH)

#    mycobot.wait(.5)

#    GPIO.cleanup(20)
#    GPIO.cleanup(21)


#    print("::set_free_mode()\n")
    mycobot.send_angles(reset, 50)
    time.sleep(1)
#    mycobot.release_all_servos()

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
