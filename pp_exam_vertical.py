#
# pp_exam_vertical.py
# 2021/12/16
# pick up from vertical
# add degree setting(for R)
#
#
# 2021/12/06
# pp_exam.py
# git test
#
#
# 2021/12/02
# test_sim_coords8.py
# add execute filename.py print
#
# test_sim_coords4.py
# 2021/11/22 nakahide
# edit: Z move method: send_coords()->send_coord()
# reference from model.xls
# add numpy
# 2021/11/23 nakahide
# wait 3=>short
#
# test_sim_coords6-1.py
# 2021/11/24
# rewrite model.xls
#
# 2021/11/24
# test_sim_coords7.py
# rewrite model.xls(add FPC design drawing)
# edit C1L value(axisY)
# edit C1R value(axisXY)
#
#

import numpy as np
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
    print("\nStart check basic options\n")
    print(__file__)

###################################################################
#
# J1-6 test
#
###################################################################
# J1-J6 set 0
    angles = [0, 0, 0, 0, 0, 0]
    mycobot.send_angles(angles, 50)
    print("::send_angles() ==> angles {}, speed 50".format(angles))
    time.sleep(1)

# J1 90_degree,50_speed
    mycobot.send_angle(Angle.J1.value, 90, 50)
    time.sleep(1)
    print("::get_angles() ==> degrees: {}\n".format(mycobot.get_angles()))


###################################################################
# led test
###################################################################
# yellow
    mycobot.set_color(255, 255, 0)
    print("::set_color() ==> color {}".format("255 255 0"))
    time.sleep(.5)
# pink
    mycobot.set_color(255, 0, 255)
    print("::set_color() ==> color {}".format("255 0 255"))
    time.sleep(.5)
# blue
    mycobot.set_color(0, 255,  255)
    print("::set_color() ==> color {}".format("0 255 255"))
    time.sleep(.5)
# white
    mycobot.set_color(255, 255, 255)
    print("::set_color() ==> color {}".format("255 255 255"))
    time.sleep(.5)

###################################################################
#
# J1-6 test
#
###################################################################
# J1-J6 set 0
    angles = [0, 0, 0, 0, 0, 0]
    mycobot.send_angles(angles, 50)
    print("::send_angles() ==> angles {}, speed 50\n".format(angles))
    time.sleep(1)

# J1 90_degree,50_speed
    mycobot.send_angle(Angle.J1.value, 90, 50)
    time.sleep(1)
    print("::get_angles() ==> degrees: {}".format(mycobot.get_angles()))

# for test (middle-point1)
    angles = [80, 25, 45, 15, 35, -45]
#    angles = [74.97, 21.09, 91.84, 65.83, 67.67, 0.35]NG
    mycobot.send_angles(angles, 50)
    print("::send_angles() ==> angles {}, speed 50".format(angles))
    time.sleep(4)
    print("::get_angles() ==> degrees: {}".format(mycobot.get_angles()))


######################################################################
#
# GPIO setting
#
######################################################################
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(19,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    pin16=GPIO.input(16)
    pin19=GPIO.input(19)

######################################################################
#
# define parameter
#
######################################################################
    loop=5
    speed=50
    wait=5

    up_height=60.0
#    up_height=65.0
    set_height=43.0
# Tray pitch
    x_shift=12
    y_shift=0

# coords for tray address

# 2021/11/25
#                   x      y      z   rx  ry  rz
#    C1L=np.array([-114,-168+20,  50,  90,  0,  0])
#    C1R=np.array([  89,-168+20,  50,  90,  0,  0])
#
# 2021/12/16 pickup from vertical
    C1L=np.array([-114+20,-168,  50,  90,  0, -90])
    C1R=np.array([  89-20,-168,  50,  90,  0,  90])

# 2021/11/23 nakahide
# for debug
#
    print("x_shift=",x_shift)
    print("y_shift=",y_shift)
    print("C1L=",C1L)
    print("C1R=",C1R)
    print("up_height=",up_height)
    print("set_height=",set_height)


    for i in range(loop):
        print("loop:",i)

# for test (to C1L)up
        print("===== 1 ==> C1Lup")
        mycobot.send_coords(C1L, speed,0)
        time.sleep(wait)
        print("upC1L=",C1L)
        print("gtC1L=",np.array(mycobot.get_coords()))
        print("upC1L-gtC1L=",C1L-np.array(mycobot.get_coords()))

        '''
# set vacuum ON!
        print("GPIO20,GPIO21 output-L => vacuum ON")
        GPIO.setup(20,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(21,GPIO.OUT,initial=GPIO.LOW)
        time.sleep(.5)
        '''

# for test (to C1L)set
        print("===== 2 ==> C1Lset")
        mycobot.send_coord(Coord.Z.value,set_height, 10) # Z value set
        time.sleep(wait)
        print("upC1L,Z=",C1L,set_height)
        print("gtC1L=",np.array(mycobot.get_coords()))

# for test (to C1L)up
        print("===== 3 ==> C1Lup")
        mycobot.send_coord(Coord.Z.value,up_height, 10)
        time.sleep(wait+1)
        print("upC1L,Z=",C1L,up_height)
        print("gtC1L=",np.array(mycobot.get_coords()))

############################################################################
############################################################################

# for test (from C1L to C1R)up
        print("===== 4 ==> C1Lup =>C1Rup")
        mycobot.send_coords(C1R, speed,0)
        time.sleep(wait)
        print("upC1R",C1R)
        print("gtC1R=",np.array(mycobot.get_coords()))
        print("upC1R-gtC1R=",C1R-np.array(mycobot.get_coords()))

# for test (from C1L to C1R)set
        print("===== 5 ==> C1Rset")
        mycobot.send_coord(Coord.Z.value,set_height, 10)
        time.sleep(wait)
        print("upC1R,Z=",C1R,set_height)
        print("gtC1R=",np.array(mycobot.get_coords()))

        '''
# set vacuum OFF!
        print("GPIO20,GPIO21 output-H => vacuum OFF")
        GPIO.setup(20,GPIO.OUT,initial=GPIO.HIGH)
        GPIO.setup(21,GPIO.OUT,initial=GPIO.HIGH)
        time.sleep(.5)
        '''

# for test (from C1R to C1R)up
        print("===== 6 ==> C1Rup")
        mycobot.send_coord(Coord.Z.value,up_height,10)
        time.sleep(wait)
        print("upC1R,Z=",C1R,up_height)
        print("gtC1R=",np.array(mycobot.get_coords()))

# for test (middle-point1)
        angles = [80, 25, 45, 15, 35, -45]
        mycobot.send_angles(angles, 50)
        time.sleep(2)


#
#                x              y       z     rx     ry    rz
        C1L=[C1L[0]+x_shift, C1L[1],C1L[2],C1L[3],C1L[4],C1L[5]]
        C1R=[C1R[0]+x_shift, C1R[1],C1R[2],C1R[3],C1R[4],C1R[5]]

#        print("i=",i)
#        print("C1L=",C1L)
#        print("C1R=",C1R)

        pin16=GPIO.input(16)
        pin19=GPIO.input(19)


        while True:
            GPIO.setmode(GPIO.BCM)
            if GPIO.input(16)==GPIO.HIGH:
                print("Green")

# test button off(up)
                angles = [75.93, 46.31, 95.88, 27.86, 70.66, -88.15]
                mycobot.send_angles(angles, 50)
                print("::send_angles() ==> angles {}, speed 50\n".format(angles))
                time.sleep(2)

                print("GPIO20,GPIO21 output-L => vacuum ON")
                GPIO.setup(20,GPIO.OUT,initial=GPIO.LOW)
                GPIO.setup(21,GPIO.OUT,initial=GPIO.LOW)

                angles = [93.86, 68.81, 28.74, 78.57, 69.66, 7.91]
                mycobot.send_angles(angles, 50)
                print("::send_angles() ==> angles {}, speed 50\n".format(angles))
                time.sleep(2)

                angles = [93.42, 77.08, 28.12, 72.5, 68.02, 3.51]
                mycobot.send_angles(angles, 50)
                print("::send_angles() ==> angles {}, speed 50\n".format(angles))
                time.sleep(2)

                angles = [90, 0, 0, 0, 0, 0]
                mycobot.send_angles(angles, 50)
                print("w:send_angles() ==> angles {}, speed 50\n".format(angles))
                time.sleep(2)

# green
                mycobot.set_color(0, 255,  0)
                print("::set_color() ==> color {}\n".format("0 255 255"))
                time.sleep(.5)

                angles = [120, 0, 0, 0, 0, 0]
                mycobot.send_angles(angles, 50)
                print("w:send_angles() ==> angles {}, speed 50\n".format(angles))
                time.sleep(1)

                angles = [120, 0, 90, 0, 0, 0]
                mycobot.send_angles(angles, 50)
                print("w:send_angles() ==> angles {}, speed 50\n".format(angles))
                time.sleep(2)

                angles = [154, 86, 44, 27, 102, -17]
                mycobot.send_angles(angles, 50)
                print("w:send_angles() ==> angles {}, speed 50\n".format(angles))
                time.sleep(2)


                print("GPIO20,GPIO21 output-H => vacuum OFF")
                GPIO.setup(20,GPIO.OUT,initial=GPIO.HIGH)
                GPIO.setup(21,GPIO.OUT,initial=GPIO.HIGH)
                time.sleep(1)


                angles = [120, 0, 0, 0, 0, 0]
                mycobot.send_angles(angles, 50)
                print("w:send_angles() ==> angles {}, speed 50\n".format(angles))
                time.sleep(1)

                angles = [90, 0, 0, 0, 0, 0]
                mycobot.send_angles(angles, 50)
                print("w:send_angles() ==> angles {}, speed 50\n".format(angles))
                time.sleep(2)

# white
                mycobot.set_color(255, 255, 255)
                print("::set_color() ==> color {}\n".format("255 255 255"))
                time.sleep(.5)


                break;
###############################################################################
            elif GPIO.input(19)==GPIO.HIGH:
                print("Red")

# test button off(up)
                angles = [75.93, 46.31, 95.88, 27.86, 70.66, -88.15]
                mycobot.send_angles(angles, 50)
                print("::send_angles() ==> angles {}, speed 50\n".format(angles))
                time.sleep(2)


                angles = [90, 0, 0, 0, 0, 0]
                mycobot.send_angles(angles, 50)
                print("w:send_angles() ==> angles {}, speed 50\n".format(angles))
                time.sleep(3)
# red
                mycobot.set_color(255, 0, 0)
                print("::set_color() ==> color {}\n".format("255 0 255"))
                time.sleep(.5)
#
                angles = [60, 0, 0, 0, 0, 0]
                mycobot.send_angles(angles, 50)
                print("w:send_angles() ==> angles {}, speed 50\n".format(angles))
                time.sleep(2)

                angles = [60, 0, 90, 0, 0, 0]
                mycobot.send_angles(angles, 50)
                print("w:send_angles() ==> angles {}, speed 50\n".format(angles))
                time.sleep(2)

                angles = [60, 0, 0, 0, 0, 0]
                mycobot.send_angles(angles, 50)
                print("w:send_angles() ==> angles {}, speed 50\n".format(angles))
                time.sleep(3)


                angles = [90, 0, 0, 0, 0, 0]
                mycobot.send_angles(angles, 50)
                print("w:send_angles() ==> angles {}, speed 50\n".format(angles))
                time.sleep(3)

# white
                mycobot.set_color(255, 255, 255)
                print("::set_color() ==> color {}\n".format("255 255 255"))
                time.sleep(.5)

                break;
###############################################################################
            else:
                print("None")

# for test Button off(up)
#                print("===== for test setup  =====")
#                coords = [-20.3, -147.6, 63.7+40, 78.59, 85.8, -101.92]
#                mycobot.send_coords(coords, 10,0)
#                time.sleep(10)
#                print("::get_coords() ==> coords: {}\n".format(mycobot.get_coords()))

# white?
                mycobot.set_color(255, 255, 000)
                print("::set_color() ==> color {}\n".format("255 255 255"))
                time.sleep(.5)

                break;
###############################################################################
        time.sleep(1)


#
#
#                                                        S
#                                                        O
#                                                        L
#                                                     L  E
#                                                     E  N P
#                                                     D  O U
#                                                     |  I M
#                                                     G  D P
#                                                     *  *  *
#--------------------------------------------------------------
#  5  5  G  N  N  G  G  G  G  G  G  G  G  G  G  G  G  G  G  G
#  .  .  N  C  C  P  N  P  P  N  P  P  P  P  N  P  N  P  P  P
#  0  0  D        I  D  I  I  D  I  I  I  I  D  I  D  I  I  I
#  V  V           O     O  O     O  O  O  O     O     O  O  O
#                 1     2  2     2  0  0  0     1     1  2  2
#                 8     3  4     5  8  7  1     2     6  0  1
#--------------------------------------------------------------
# 02 04 06 08 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40
#
# 01 03 05 07 09 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39
#--------------------------------------------------------------
#  3  N  G  G  G  G  G  G  3  G  G  G  G  G  G  G  G  G  G  G
#  .  C  P  P  N  P  P  P  .  P  P  P  N  P  P  P  P  P  P  N
#  3     I  I  D  I  I  I  3  I  I  I  D  I  I  I  I  I  I  D
#  V     O  O     O  O  O  V  O  O  O     O  O  O  O  O  O
#        0  0     1  2  2     1  0  1     0  0  0  1  1  2
#        3  4     7  7  2     0  9  1     0  5  6  3  9  6
#--------------------------------------------------------------
#                                                     *
#                                                     L
#                                                     E
#                                                     D
#                                                     |
#                                                     R
#                                                     e
#                                                     d
#
#
# GPIO set output mode
#    GPIO.setmode(GPIO.BCM)
#    GPIO.setup(21,GPIO.OUT)
#    GPIO.output(21,True)

# set input mode
#    GPIO.setmode(GPIO.BCM)
#    print("pullup")
#    GPIO.setup(20,GPIO.IN,pull_up_down=GPIO.PUD_UP)
#    GPIO.setup(21,GPIO.IN,pull_up_down=GPIO.PUD_UP)
#
#    mycobot.wait(10)
#
#    print("pulldown")
#    GPIO.setup(20,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
#    GPIO.setup(21,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
#
#    mycobot.wait(10)

# set input mode
#    print("output-H")
#    GPIO.setup(20,GPIO.OUT,initial=GPIO.HIGH)
#    GPIO.setup(21,GPIO.OUT,initial=GPIO.HIGH)
#
#    mycobot.wait(10)

# GPIO set output mode
    GPIO.setmode(GPIO.BCM)
# set vacuum ON!
#    print("GPIO20,GPIO21 output-L => vacuum ON")
#    GPIO.setup(20,GPIO.OUT,initial=GPIO.LOW)
#    GPIO.setup(21,GPIO.OUT,initial=GPIO.LOW)
#
#    mycobot.wait(3)
#
#    print("GPIO20,GPIO21 output-H => vacuum OFF")
    GPIO.setup(20,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(21,GPIO.OUT,initial=GPIO.HIGH)
#
#    mycobot.wait(3)

    GPIO.cleanup(20)
    GPIO.cleanup(21)


#    print("::set_free_mode()\n")
    mycobot.send_angles(reset, 80)
    time.sleep(5)
    mycobot.release_all_servos()

    print("=== check end ===\n")


if __name__ == "__main__":
    print("exec:",__file__)
    print(
#        """
#--------------------------------------------
#| This file will test basic option method: |
#|     set_led_color()                      |
#|     send_angles()                        |
#|     get_angles()                         |
#|     send_angle()                         |
#|     send_radians()                       |
#|     get_radians()                        |
#|     send_coords()                        |
#|     get_coords()                         |
#|     send_coord()                         |
#--------------------------------------------
#          """
    )
    time.sleep(2)
    # port = subprocess.check_output(['echo -n /dev/ttyUSB*'],
    # shell=True).decode()
    # with open(os.path.dirname(__file__) + "/port.txt") as f:
        # port = f.read().strip().replace("\n", "")
        # print(port)
# 2021/11/01 nakahide
#    mycobot = setup()
    mycobot = setup_naka()
    test(mycobot)
