# ci_direct_pp_coords.py
# 2021/12/22 nakahide
# Environment change => circle layout Ver.
# 1st try
# C1L=>C1R:moving ====> C2-C5 copy
#
# # direct_pp_coords.py
# 2021/12/20 nakahide
# angles()=>coords()
# add subtle adjustment(x,y,z)
#
# C1-C5 pickup_OK, place_ALLNG!
#
# direct_pp_angles.py
# 2021/12/20 nakahide
# add vacuum execute => C1:pickup_OK C2-C5:pickup_NG
# direct teaching 6th(+11mm+angles change + bring hand setting)
#    :
#    :
# direct teaching 2nd (+7mm)
# 2021/12/17 nakahide
# direct teaching 1st for C1-5L => C1-5R : result NG(Contacted on the pickup point)
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
#    mycobot.set_color(255, 255, 0)
#    print("::set_color() ==> color {}".format("255 255 0"))
#    time.sleep(.5)
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
#
#   1:vacuum_use, 0:vacuum_not_use
#    vacuum_use=1
    vacuum_use=0
#
#   j1_rotate(degree)
#   j2_up(degree)
    j1r=80
    j2r=20

# angles for tray address
##############################################################
# 1st trial()
    C1L_angles=[41.22, 53.34, 70.04, 55.81, 81.29, -4.21]
    C1L_coords=[-120.7, -130.1, 69.3, 89.88, 3.43, -130.08]

    C2L_angles=[45.35, 53.26, 70.13, 57.83, 81.12, -0.96]
    C2L_coords=[-109.2, -136.7, 69.2, 90.19, 2.18, -125.76]

    C3L_angles=[49.21, 53.34, 70.04, 56.77, 85.07, -0.08]
    C3L_coords=[-99.0, -142.2, 69.2, 90.01, 0.26, -125.85]

    C4L_angles=[53.34, 53.52, 70.13, 56.07, 84.28, -2.63]
    C4L_coords=[-89.1, -150.0, 68.6, 89.97, 2.37, -120.93]

    C5L_angles=[56.95, 53.61, 70.04, 53.34, 86.04, -2.63]
    C5L_coords=[-80.8, -157.1, 68.7, 89.79, -0.34, -119.09]


    L_R_angles=[82.79, 30.05, 70.13, 58.35, 86.66, -2.63]
    L_R_coords=[-4.8, -180.5, 140.8, 88.71, -18.77, -93.68]

    C1L_up_angles=[C1L_angles[0]    ,C1L_angles[1]-j2r,C1L_angles[2],C1L_angles[3],C1L_angles[4],C1L_angles[5]]
    C1R_up_angles=[C1L_angles[0]+j1r,C1L_angles[1]-j2r,C1L_angles[2],C1L_angles[3],C1L_angles[4],C1L_angles[5]]
    C1R_angles   =[C1L_angles[0]+j1r,C1L_angles[1]    ,C1L_angles[2],C1L_angles[3],C1L_angles[4],C1L_angles[5]]

    C2L_up_angles=[C2L_angles[0]    ,C2L_angles[1]-j2r,C2L_angles[2],C2L_angles[3],C2L_angles[4],C2L_angles[5]]
    C2R_up_angles=[C2L_angles[0]+j1r,C2L_angles[1]-j2r,C2L_angles[2],C2L_angles[3],C2L_angles[4],C2L_angles[5]]
    C2R_angles   =[C2L_angles[0]+j1r,C2L_angles[1]    ,C2L_angles[2],C2L_angles[3],C2L_angles[4],C2L_angles[5]]

    C3L_up_angles=[C3L_angles[0]    ,C3L_angles[1]-j2r,C3L_angles[2],C3L_angles[3],C3L_angles[4],C3L_angles[5]]
    C3R_up_angles=[C3L_angles[0]+j1r,C3L_angles[1]-j2r,C3L_angles[2],C3L_angles[3],C3L_angles[4],C3L_angles[5]]
    C3R_angles   =[C3L_angles[0]+j1r,C3L_angles[1]    ,C3L_angles[2],C3L_angles[3],C3L_angles[4],C3L_angles[5]]

    C4L_up_angles=[C4L_angles[0]    ,C4L_angles[1]-j2r,C4L_angles[2],C4L_angles[3],C4L_angles[4],C4L_angles[5]]
    C4R_up_angles=[C4L_angles[0]+j1r,C4L_angles[1]-j2r,C4L_angles[2],C4L_angles[3],C4L_angles[4],C4L_angles[5]]
    C4R_angles   =[C4L_angles[0]+j1r,C4L_angles[1]    ,C4L_angles[2],C4L_angles[3],C4L_angles[4],C4L_angles[5]]

    C5L_up_angles=[C5L_angles[0]    ,C5L_angles[1]-j2r,C5L_angles[2],C5L_angles[3],C5L_angles[4],C5L_angles[5]]
    C5R_up_angles=[C5L_angles[0]+j1r,C5L_angles[1]-j2r,C5L_angles[2],C5L_angles[3],C5L_angles[4],C5L_angles[5]]
    C5R_angles   =[C5L_angles[0]+j1r,C5L_angles[1]    ,C5L_angles[2],C5L_angles[3],C5L_angles[4],C5L_angles[5]]

#    C1R_angles=[]
#    C1R_coords=[]

#    C2R_angles=[]
#    C2R_coords=[]

#    C3R_angles=[]
#    C3R_coords=[]

#    C4R_angles=[]
#    C4R_coords=[]

#    C5R_angles=[]
#    C5R_coords=[]


    print("===== 0 ==> L_R")
#    mycobot.send_angles(L_R_angles, speed)
    mycobot.send_coords(L_R_coords, speed,0)
    time.sleep(wait)


#### C1 Start ####

    print("===== 0 ==> C1L_up")
    mycobot.send_angles(C1L_up_angles, speed)
#    mycobot.send_coords(C1L_coords, speed,0)
    time.sleep(wait)

# set vacuum ON!
    if (vacuum_use):
        print("GPIO20,GPIO21 output-L => vacuum ON")
        GPIO.setup(20,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(21,GPIO.OUT,initial=GPIO.LOW)
        time.sleep(.5)

    print("===== 1L ==> C1L pickup")
#    mycobot.send_angles(C1L_angles, speed)
    mycobot.send_coords(C1L_coords, speed,0)
    time.sleep(wait)

    print("===== 1L ==> J2_up")
    mycobot.send_angles(C1L_up_angles, speed)
#    mycobot.send_coords(C1L_coords, speed,0)
    time.sleep(wait)

    print("===== 1R ==> J1_rotate_R")
    mycobot.send_angles(C1R_up_angles, speed)
#    mycobot.send_coords(C1L_coords, speed,0)
    time.sleep(wait)

    print("===== 1L ==> J2_down")
    mycobot.send_angles(C1R_angles, speed)
#    mycobot.send_coords(C1L_coords, speed,0)
    time.sleep(wait)

# set vacuum OFF!
    if (vacuum_use):
        print("GPIO20,GPIO21 output-H => vacuum OFF")
        GPIO.setup(20,GPIO.OUT,initial=GPIO.HIGH)
        GPIO.setup(21,GPIO.OUT,initial=GPIO.HIGH)
        time.sleep(.5)

    print("===== 1R ==> J2_up")
    mycobot.send_angles(C1R_up_angles, speed)
#    mycobot.send_coords(C1L_coords, speed,0)
    time.sleep(wait)

    print("===== 0 ==> L_R")
    mycobot.send_angles(L_R_angles, speed)
#    mycobot.send_coords(L_R_coords, speed,0)
    time.sleep(wait)

#### C1 End ####
#### C2 Start ####

    print("===== 0 ==> C2L_up")
    mycobot.send_angles(C2L_up_angles, speed)
#    mycobot.send_coords(C2L_coords, speed,0)
    time.sleep(wait)

# set vacuum ON!
    if (vacuum_use):
        print("GPIO20,GPIO21 output-L => vacuum ON")
        GPIO.setup(20,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(21,GPIO.OUT,initial=GPIO.LOW)
        time.sleep(.5)

    print("===== 2L ==> C2L pickup")
#    mycobot.send_angles(C2L_angles, speed)
    mycobot.send_coords(C2L_coords, speed,0)
    time.sleep(wait)

    print("===== 2L ==> J2_up")
    mycobot.send_angles(C2L_up_angles, speed)
#    mycobot.send_coords(C2L_coords, speed,0)
    time.sleep(wait)

    print("===== 2R ==> J1_rotate_R")
    mycobot.send_angles(C2R_up_angles, speed)
#    mycobot.send_coords(C2R?_coords, speed,0)
    time.sleep(wait)

    print("===== 2R ==> J2_down")
    mycobot.send_angles(C2R_angles, speed)
#    mycobot.send_coords(C2L_coords, speed,0)
    time.sleep(wait)

# set vacuum OFF!
    if (vacuum_use):
        print("GPIO20,GPIO21 output-H => vacuum OFF")
        GPIO.setup(20,GPIO.OUT,initial=GPIO.HIGH)
        GPIO.setup(21,GPIO.OUT,initial=GPIO.HIGH)
        time.sleep(.5)

    print("===== 2R ==> J2_up")
    mycobot.send_angles(C2R_up_angles, speed)
#    mycobot.send_coords(C2L_coords, speed,0)
    time.sleep(wait)

    print("===== 0 ==> L_R")
    mycobot.send_angles(L_R_angles, speed)
#    mycobot.send_coords(L_R_coords, speed,0)
    time.sleep(wait)

#### C2 End ####

#### C3 Start ####

    print("===== 0 ==> C3L_up")
    mycobot.send_angles(C3L_up_angles, speed)
#    mycobot.send_coords(C3L_coords, speed,0)
    time.sleep(wait)

# set vacuum ON!
    if (vacuum_use):
        print("GPIO20,GPIO21 output-L => vacuum ON")
        GPIO.setup(20,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(21,GPIO.OUT,initial=GPIO.LOW)
        time.sleep(.5)

    print("===== 3L ==> C3L pickup")
#    mycobot.send_angles(C3L_angles, speed)
    mycobot.send_coords(C3L_coords, speed,0)
    time.sleep(wait)

    print("===== 3L ==> J2_up")
    mycobot.send_angles(C3L_up_angles, speed)
#    mycobot.send_coords(C3L_coords, speed,0)
    time.sleep(wait)

    print("===== 3R ==> J1_rotate_R")
    mycobot.send_angles(C3R_up_angles, speed)
#    mycobot.send_coords(C3R?_coords, speed,0)
    time.sleep(wait)

    print("===== 3R ==> J2_down")
    mycobot.send_angles(C3R_angles, speed)
#    mycobot.send_coords(C3L_coords, speed,0)
    time.sleep(wait)

# set vacuum OFF!
    if (vacuum_use):
        print("GPIO20,GPIO21 output-H => vacuum OFF")
        GPIO.setup(20,GPIO.OUT,initial=GPIO.HIGH)
        GPIO.setup(21,GPIO.OUT,initial=GPIO.HIGH)
        time.sleep(.5)

    print("===== 3R ==> J2_up")
    mycobot.send_angles(C3R_up_angles, speed)
#    mycobot.send_coords(C3L_coords, speed,0)
    time.sleep(wait)

    print("===== 0 ==> L_R")
    mycobot.send_angles(L_R_angles, speed)
#    mycobot.send_coords(L_R_coords, speed,0)
    time.sleep(wait)

#### C3 End ####

#### C4 Start ####

    print("===== 0 ==> C4L_up")
    mycobot.send_angles(C4L_up_angles, speed)
#    mycobot.send_coords(C4L_coords, speed,0)
    time.sleep(wait)

# set vacuum ON!
    if (vacuum_use):
        print("GPIO20,GPIO21 output-L => vacuum ON")
        GPIO.setup(20,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(21,GPIO.OUT,initial=GPIO.LOW)
        time.sleep(.5)

    print("===== 4L ==> C4L pickup")
#    mycobot.send_angles(C4L_angles, speed)
    mycobot.send_coords(C4L_coords, speed,0)
    time.sleep(wait)

    print("===== 4L ==> J2_up")
    mycobot.send_angles(C4L_up_angles, speed)
#    mycobot.send_coords(C4L_coords, speed,0)
    time.sleep(wait)

    print("===== 4R ==> J1_rotate_R")
    mycobot.send_angles(C4R_up_angles, speed)
#    mycobot.send_coords(C4R?_coords, speed,0)
    time.sleep(wait)

    print("===== 4R ==> J2_down")
    mycobot.send_angles(C4R_angles, speed)
#    mycobot.send_coords(C4L_coords, speed,0)
    time.sleep(wait)

# set vacuum OFF!
    if (vacuum_use):
        print("GPIO20,GPIO21 output-H => vacuum OFF")
        GPIO.setup(20,GPIO.OUT,initial=GPIO.HIGH)
        GPIO.setup(21,GPIO.OUT,initial=GPIO.HIGH)
        time.sleep(.5)

    print("===== 4R ==> J2_up")
    mycobot.send_angles(C4R_up_angles, speed)
#    mycobot.send_coords(C4L_coords, speed,0)
    time.sleep(wait)

    print("===== 0 ==> L_R")
    mycobot.send_angles(L_R_angles, speed)
#    mycobot.send_coords(L_R_coords, speed,0)
    time.sleep(wait)

#### C4 End ####

#### C5 Start ####

    print("===== 0 ==> C5L_up")
    mycobot.send_angles(C5L_up_angles, speed)
#    mycobot.send_coords(C5L_coords, speed,0)
    time.sleep(wait)

# set vacuum ON!
    if (vacuum_use):
        print("GPIO20,GPIO21 output-L => vacuum ON")
        GPIO.setup(20,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(21,GPIO.OUT,initial=GPIO.LOW)
        time.sleep(.5)

    print("===== 5L ==> C5L pickup")
#    mycobot.send_angles(C5L_angles, speed)
    mycobot.send_coords(C5L_coords, speed,0)
    time.sleep(wait)

    print("===== 5L ==> J2_up")
    mycobot.send_angles(C5L_up_angles, speed)
#    mycobot.send_coords(C5L_coords, speed,0)
    time.sleep(wait)

    print("===== 5R ==> J1_rotate_R")
    mycobot.send_angles(C5R_up_angles, speed)
#    mycobot.send_coords(C5R?_coords, speed,0)
    time.sleep(wait)

    print("===== 5R ==> J2_down")
    mycobot.send_angles(C5R_angles, speed)
#    mycobot.send_coords(C5R?_coords, speed,0)
    time.sleep(wait)

# set vacuum OFF!
    if (vacuum_use):
        print("GPIO20,GPIO21 output-H => vacuum OFF")
        GPIO.setup(20,GPIO.OUT,initial=GPIO.HIGH)
        GPIO.setup(21,GPIO.OUT,initial=GPIO.HIGH)
        time.sleep(.5)

    print("===== 4R ==> J2_up")
    mycobot.send_angles(C4R_up_angles, speed)
#    mycobot.send_coords(C4L_coords, speed,0)
    time.sleep(wait)

    print("===== 0 ==> L_R")
    mycobot.send_angles(L_R_angles, speed)
#    mycobot.send_coords(L_R_coords, speed,0)
    time.sleep(wait)

#### C5 End ####


    print("===== 0 ==> L_R")
#    mycobot.send_angles(L_R_angles, speed)
    mycobot.send_coords(L_R_coords, speed,0)
    time.sleep(wait)





# 2021/11/23 nakahide
# for debug
#
    print("x_shift=",x_shift)
    print("y_shift=",y_shift)
#    print("C1L=",C1L)
#    print("C1R=",C1R)
    print("up_height=",up_height)
    print("set_height=",set_height)

    '''
    for i in range(loop):
        print("loop:",i)

# for test (to C1L)up
        print("===== 1 ==> C1Lup")
        mycobot.send_coords(C1L, speed,0)
        time.sleep(wait)
#        print("::get_coords() ==> coords: {}".format(mycobot.get_coords()))
        print("upC1L=",i,C1L)
#        print("gtC1L=",mycobot.get_coords())
        print("gtC1L=",np.array(mycobot.get_coords()))
        print("upC1L-gtC1L=",C1L-np.array(mycobot.get_coords()))


# set vacuum ON!
        print("GPIO20,GPIO21 output-L => vacuum ON")
        GPIO.setup(20,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(21,GPIO.OUT,initial=GPIO.LOW)
        time.sleep(.5)

# for test (to C1L)set
        print("===== 2 ==> C1Lset")
        mycobot.send_coord(Coord.Z.value,set_height, 10) # Z value set
#        print("::get_coords() ==> coords: {}".format(mycobot.get_coords()))
        time.sleep(wait)
        print("upC1L,Z=",i,C1L,set_height)
        print("gtC1L=",np.array(mycobot.get_coords()))
#        print("upC1L-gtC1L=",C1L-np.array(mycobot.get_coords()))



# for test (to C1L)up
        print("===== 3 ==> C1Lup")
        mycobot.send_coord(Coord.Z.value,up_height, 10)
        time.sleep(wait+1)
#        print("::get_coords() ==> coords: {}".format(mycobot.get_coords()))
        print("upC1L,Z=",i,C1L,up_height)
        print("gtC1L=",np.array(mycobot.get_coords()))
#        print("upC1L-gtC1L=",C1L-np.array(mycobot.get_coords()))

############################################################################
# for test (middle-point1)
#        angles = [80, 25, 45, 15, 35, -45]
#        mycobot.send_angles(angles, 50)
#        print("::send_angles() ==> angles {}, speed 50\n".format(angles))
#        time.sleep(2)
############################################################################

# for test (from C1L to C1R)up
        print("===== 4 ==> C1Lup =>C1Rup")
        mycobot.send_coords(C1R, speed,0)
#        print("::get_coords() ==> coords: {}".format(mycobot.get_coords()))
        time.sleep(wait)
        print("upC1R",i,C1R)
        print("gtC1R=",np.array(mycobot.get_coords()))
        print("upC1R-gtC1R=",C1R-np.array(mycobot.get_coords()))

# for test (from C1L to C1R)set
        print("===== 5 ==> C1Rset")
        mycobot.send_coord(Coord.Z.value,set_height, 10)
#        print("::get_coords() ==> coords: {}".format(mycobot.get_coords()))
        time.sleep(wait)
        print("upC1R,Z=",i,C1R,set_height)
        print("gtC1R=",np.array(mycobot.get_coords()))
#        print("upC1R-gtC1R=",C1L-np.array(mycobot.get_coords()))

# set vacuum OFF!
        print("GPIO20,GPIO21 output-H => vacuum OFF")
        GPIO.setup(20,GPIO.OUT,initial=GPIO.HIGH)
        GPIO.setup(21,GPIO.OUT,initial=GPIO.HIGH)
        time.sleep(.5)

# for test (from C1R to C1R)up
        print("===== 6 ==> C1Rup")
        mycobot.send_coord(Coord.Z.value,up_height,10)
#        print("::get_coords() ==> coords: {}".format(mycobot.get_coords()))
        time.sleep(wait)
        print("upC1R,Z=",i,C1R,up_height)
        print("gtC1R=",np.array(mycobot.get_coords()))
#        print("upC1R-gtC1R=",C1L-np.array(mycobot.get_coords()))


# for test (middle-point1)
        angles = [80, 25, 45, 15, 35, -45]
        mycobot.send_angles(angles, 50)
#        print("::send_angles() ==> angles {}, speed 50\n".format(angles))
        time.sleep(2)
#        print("::get_angles() ==> degrees: {}".format(mycobot.get_angles()))


#        C1L=[-116.6, -150.5, 50, 90.53, 1.68, -3.23]
#        C1R=[91.6, -153.3, 50, 88.88, 2.02, 1.1]
#        C1L=[-116.6+x_shift, -150.5, 50, 90.53, 1.68, -3.23]
#        C1R=[91.6+x_shift, -153.3, 50, 88.88, 2.02, 1.1]
#        x_shift=x_shift+12
#        print("x_shift=",x_shift)
#
#                x              y       z     rx     ry    rz
        C1L=[C1L[0]+x_shift, C1L[1],C1L[2],C1L[3],C1L[4],C1L[5]]
        C1R=[C1R[0]+x_shift, C1R[1],C1R[2],C1R[3],C1R[4],C1R[5]]

        print("i=",i)

        print("C1L=",C1L)
        print("C1R=",C1R)

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
    '''

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
