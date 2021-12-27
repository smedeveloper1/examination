# ci_direct_pp_coords.py
# 2021/12/27 nakahide
# C4,C5 adjuxt z,-1
# B1-B5 pickup OK
#
# # 2021/12/24
# add sum by np.array()
# wait:wait 4 =>2
# speed: fast=80/speed=50/slow=10
# pickup degree j2r: 15 => 3
#
#
# 2021/12/23 nakahide
# add vacuum function
#( add A1-A5,B1-B5,D1-D5,E1-E5 )
#
# 2021/12/22 nakahide
# Environment change => circle layout Ver.
# 1st try
# C1L=>C1R:moving ====> C2-C5 copy
# coords adjust x,y,-5,-5
# C1-C3 adjust z,-1

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

#############################################################
#
# function vacuum
#
#############################################################
    def vacuum_on():
        print("GPIO20,GPIO21 output-L => vacuum ON")
        GPIO.setup(20,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(21,GPIO.OUT,initial=GPIO.LOW)
        time.sleep(.5)

    def vacuum_off():
        print("GPIO20,GPIO21 output-H => vacuum OFF")
        GPIO.setup(20,GPIO.OUT,initial=GPIO.HIGH)
        GPIO.setup(21,GPIO.OUT,initial=GPIO.HIGH)
        time.sleep(.5)


######################################################################
#
# define parameter
#
######################################################################
    loop=5

### speed setting ###
    fast =80
    speed=50
    slow =10

### wait setting ###
#    wait=4
    wait=2

    up_height=60.0
#    up_height=65.0
    set_height=43.0
# Tray pitch
    x_shift=12
    y_shift=0
#
#
# 2021/12/23 nakahide
#   tray_address_A-E select
#
    t_ad_A=1
    t_ad_B=1
    t_ad_C=1
#    t_ad_D=1
#    t_ad_E=1
#
#   1:vacuum_use, 0:vacuum_not_use
    vacuum_use=1
#    vacuum_use=0
#
#   j1_rotate(degree)
#   j2_up(degree)
    j1r=80
#    j2r=20
#    j2r=15
#    j2r=10
#    j2r=8
#    j2r=5
    j2r=3

#
#    for angles parameter
#
#                             J1   J2   J3   J4   J5   J6
    L_up_angles = np.array([   0,-j2r,   0,   0,   0,   0])
    R_up_angles = np.array([ j1r,-j2r,   0,   0,   0,   0])
    R_angles    = np.array([ j1r,   0,   0,   0,   0,   0])

#####################################################################





##############################################################
# angles for tray address
##############################################################
    if(t_ad_C):
# 1st trial()
# add adjust x,y -5,-5
# add C1,C2,C3,C4,C5 adjust z -1
        C1L_angles=np.array([41.22, 53.34, 70.04, 55.81, 81.29, -4.21])
#    C1L_coords=[-120.7, -130.1, 69.3, 89.88, 3.43, -130.08]
#    C1L_coords=[-120.7-5, -130.1-5, 69.3, 89.88, 3.43, -130.08]
        C1L_coords=np.array([-120.7-5, -130.1-5, 69.3-1, 89.88, 3.43, -130.08])

        C2L_angles=np.array([45.35, 53.26, 70.13, 57.83, 81.12, -0.96])
#    C2L_coords=[-109.2, -136.7, 69.2, 90.19, 2.18, -125.76]
#    C2L_coords=[-109.2-5, -136.7-5, 69.2, 90.19, 2.18, -125.76]
        C2L_coords=np.array([-109.2-5, -136.7-5, 69.2-1, 90.19, 2.18, -125.76])

        C3L_angles=np.array([49.21, 53.34, 70.04, 56.77, 85.07, -0.08])
#    C3L_coords=[-99.0, -142.2, 69.2, 90.01, 0.26, -125.85]
#    C3L_coords=[-99.0-5, -142.2-5, 69.2, 90.01, 0.26, -125.85]
        C3L_coords=np.array([-99.0-5, -142.2-5, 69.2-1, 90.01, 0.26, -125.85])

        C4L_angles=np.array([53.34, 53.52, 70.13, 56.07, 84.28, -2.63])
#    C4L_coords=[-89.1, -150.0, 68.6, 89.97, 2.37, -120.93]
        C4L_coords=np.array([-89.1-6, -150.0-5, 68.6-1, 89.97, 2.37, -120.93])

        C5L_angles=np.array([56.95, 53.61, 70.04, 53.34, 86.04, -2.63])
#    C5L_coords=[-80.8, -157.1, 68.7, 89.79, -0.34, -119.09]
        C5L_coords=np.array([-80.8-5, -157.1-5, 68.7-1, 89.79, -0.34, -119.09])

        L_R_angles=np.array([82.79, 30.05, 70.13, 58.35, 86.66, -2.63])
        L_R_coords=np.array([-4.8, -180.5, 140.8, 88.71, -18.77, -93.68])


        C1L_up_angles = C1L_angles + L_up_angles
        C1R_up_angles = C1L_angles + R_up_angles
        C1R_angles    = C1L_angles + R_angles

        C2L_up_angles = C2L_angles + L_up_angles
        C2R_up_angles = C2L_angles + R_up_angles
        C2R_angles    = C2L_angles + R_angles

        C3L_up_angles = C3L_angles + L_up_angles
        C3R_up_angles = C3L_angles + R_up_angles
        C3R_angles    = C3L_angles + R_angles

        C4L_up_angles = C4L_angles + L_up_angles
        C4R_up_angles = C4L_angles + R_up_angles
        C4R_angles    = C4L_angles + R_angles

        C5L_up_angles = C5L_angles + L_up_angles
        C5R_up_angles = C5L_angles + R_up_angles
        C5R_angles    = C5L_angles + R_angles

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


        print("=== init ==> L_R")
#    mycobot.send_angles(C1_LR_angles, speed) # 2021/12/24 => NG:average of C1L_up & C1R_up
#    mycobot.send_angles(L_R_angles, speed,0)
        mycobot.send_coords(L_R_coords, speed,0)
        time.sleep(wait)


#### C1 Start #################################
        print("===== 1L ==> C1L_up")
        mycobot.send_angles(C1L_up_angles, fast)
#    mycobot.send_coords(C1L_coords, speed,0)
        time.sleep(wait)
# set vacuum ON!
        if (vacuum_use):
            vacuum_on()
        print("===== 1L ==> C1L pickup")
#    mycobot.send_angles(C1L_angles, speed)
        mycobot.send_coords(C1L_coords, slow,0)
        time.sleep(wait)
        print("===== 1L ==> J2_up")
        mycobot.send_angles(C1L_up_angles, fast)
#    mycobot.send_coords(C1L_coords, speed,0)
        time.sleep(wait)
        print("===== 1R ==> J1_rotate_R")
        mycobot.send_angles(C1R_up_angles, fast)
#    mycobot.send_coords(C1R?_coords, speed,0)
        time.sleep(wait)
        print("===== 1R ==> J2_down")
        mycobot.send_angles(C1R_angles, slow)
#    mycobot.send_coords(C1R?_coords, speed,0)
        time.sleep(wait)
# set vacuum OFF!
        if (vacuum_use):
            vacuum_off()
        print("===== 1R ==> J2_up")
        mycobot.send_angles(C1R_up_angles, fast)
#    mycobot.send_coords(C1R?_coords, speed,0)
        time.sleep(wait)
        print("== 1-end ==> L_R")
        mycobot.send_angles(L_R_angles, fast)
#    mycobot.send_coords(L_R_coords, speed,0)
        time.sleep(wait)
#### C1 End ###################################
#### C2 Start #################################
        print("===== 2L ==> C2L_up")
        mycobot.send_angles(C2L_up_angles, fast)
#    mycobot.send_coords(C2L_coords, speed,0)
        time.sleep(wait)
# set vacuum ON!
        if (vacuum_use):
            vacuum_on()
        print("===== 2L ==> C2L pickup")
#    mycobot.send_angles(C2L_angles, speed)
        mycobot.send_coords(C2L_coords, slow,0)
        time.sleep(wait)
        print("===== 2L ==> J2_up")
        mycobot.send_angles(C2L_up_angles, fast)
#    mycobot.send_coords(C2L_coords, speed,0)
        time.sleep(wait)
        print("===== 2R ==> J1_rotate_R")
        mycobot.send_angles(C2R_up_angles, fast)
#    mycobot.send_coords(C2R?_coords, speed,0)
        time.sleep(wait)
        print("===== 2R ==> J2_down")
        mycobot.send_angles(C2R_angles, slow)
#    mycobot.send_coords(C2R?_coords, speed,0)
        time.sleep(wait)
# set vacuum OFF!
        if (vacuum_use):
            vacuum_off()
        print("===== 2R ==> J2_up")
        mycobot.send_angles(C2R_up_angles, fast)
#    mycobot.send_coords(C2R?_coords, speed,0)
        time.sleep(wait)
        print("== 2-end ==> L_R")
        mycobot.send_angles(L_R_angles, fast)
#    mycobot.send_coords(L_R_coords, speed,0)
        time.sleep(wait)
#### C2 End ###################################
#### C3 Start #################################
        print("===== 3L ==> C3L_up")
        mycobot.send_angles(C3L_up_angles, fast)
#    mycobot.send_coords(C3L_coords, speed,0)
        time.sleep(wait)
# set vacuum ON!
        if (vacuum_use):
            vacuum_on()
        print("===== 3L ==> C3L pickup")
#    mycobot.send_angles(C3L_angles, speed)
        mycobot.send_coords(C3L_coords, slow,0)
        time.sleep(wait)
        print("===== 3L ==> J2_up")
        mycobot.send_angles(C3L_up_angles, fast)
#    mycobot.send_coords(C3L_coords, speed,0)
        time.sleep(wait)
        print("===== 3R ==> J1_rotate_R")
        mycobot.send_angles(C3R_up_angles, fast)
#    mycobot.send_coords(C3R?_coords, speed,0)
        time.sleep(wait)
        print("===== 3R ==> J2_down")
        mycobot.send_angles(C3R_angles, slow)
#    mycobot.send_coords(C3R?_coords, speed,0)
        time.sleep(wait)
# set vacuum OFF!
        if (vacuum_use):
            vacuum_off()
        print("===== 3R ==> J2_up")
        mycobot.send_angles(C3R_up_angles, fast)
#    mycobot.send_coords(C3R?_coords, speed,0)
        time.sleep(wait)
        print("== 3-end ==> L_R")
        mycobot.send_angles(L_R_angles, fast)
#    mycobot.send_coords(L_R_coords, speed,0)
        time.sleep(wait)
#### C3 End ###################################
#### C4 Start #################################
        print("===== 4L ==> C4L_up")
        mycobot.send_angles(C4L_up_angles, fast)
#    mycobot.send_coords(C4L_coords, speed,0)
        time.sleep(wait)
# set vacuum ON!
        if (vacuum_use):
            vacuum_on()
        print("===== 4L ==> C4L pickup")
#    mycobot.send_angles(C4L_angles, speed)
        mycobot.send_coords(C4L_coords, slow,0)
        time.sleep(wait)
        print("===== 4L ==> J2_up")
        mycobot.send_angles(C4L_up_angles, fast)
#    mycobot.send_coords(C4L_coords, speed,0)
        time.sleep(wait)
        print("===== 4R ==> J1_rotate_R")
        mycobot.send_angles(C4R_up_angles, fast)
#    mycobot.send_coords(C4R?_coords, speed,0)
        time.sleep(wait)
        print("===== 4R ==> J2_down")
        mycobot.send_angles(C4R_angles, slow)
#    mycobot.send_coords(C4R?_coords, speed,0)
        time.sleep(wait)
# set vacuum OFF!
        if (vacuum_use):
            vacuum_off()
        print("===== 4R ==> J2_up")
        mycobot.send_angles(C4R_up_angles, fast)
#    mycobot.send_coords(C4R?_coords, speed,0)
        time.sleep(wait)
        print("== 4-end ==> L_R")
        mycobot.send_angles(L_R_angles, fast)
#    mycobot.send_coords(L_R_coords, speed,0)
        time.sleep(wait)
#### C4 End ###################################
#### C5 Start #################################
        print("===== 5L ==> C5L_up")
        mycobot.send_angles(C5L_up_angles, fast)
#    mycobot.send_coords(C5L_coords, speed,0)
        time.sleep(wait)
# set vacuum ON!
        if (vacuum_use):
            vacuum_on()
        print("===== 5L ==> C5L pickup")
#    mycobot.send_angles(C5L_angles, speed)
        mycobot.send_coords(C5L_coords, slow,0)
        time.sleep(wait)
        print("===== 5L ==> J2_up")
        mycobot.send_angles(C5L_up_angles, fast)
#    mycobot.send_coords(C5L_coords, speed,0)
        time.sleep(wait)
        print("===== 5R ==> J1_rotate_R")
        mycobot.send_angles(C5R_up_angles, fast)
#    mycobot.send_coords(C5R?_coords, speed,0)
        time.sleep(wait)
        print("===== 5R ==> J2_down")
        mycobot.send_angles(C5R_angles, slow)
#    mycobot.send_coords(C5R?_coords, speed,0)
        time.sleep(wait)
# set vacuum OFF!
        if (vacuum_use):
            vacuum_off()
        print("===== 5R ==> J2_up")
        mycobot.send_angles(C5R_up_angles, fast)
#    mycobot.send_coords(C5R?_coords, speed,0)
        time.sleep(wait)
        print("== 5-end ==> L_R")
        mycobot.send_angles(L_R_angles, fast)
#    mycobot.send_coords(L_R_coords, speed,0)
        time.sleep(wait)
#### C5 End ###################################



##############################################################
# angles for tray address
##############################################################
    if(t_ad_B):
# 1st trial()
# add adjust x,y,z,-3,-3,-3
        B1L_angles=np.array([42.36, 70.4, 32.51, 78.39, 75.49, 0.0])
#    B1L_coords=np.array([-140.1, -153.8, 71.4, 90.33, 1.27, -123.13])
        B1L_coords=np.array([-140.1-3, -153.8-3, 71.4-3, 90.33, 1.27, -123.13])

        B2L_angles=np.array([45.43, 70.4, 32.43, 78.39, 75.58, 0.0])
#    B2L_coords=np.array([-131.7, -161.2, 71.6, 90.3, 1.19, -120.14])
        B2L_coords=np.array([-131.7-3, -161.2-3, 71.6-3, 90.3, 1.19, -120.14])

        B3L_angles=np.array([48.86, 70.48, 32.51, 78.39, 75.58, -1.49])
#    B3L_coords=np.array([-121.7, -168.6, 71.1, 90.35, 2.85, -116.7])
        B3L_coords=np.array([-121.7-3, -168.6-3, 71.1-3, 90.35, 2.85, -116.7])

        B4L_angles=np.array([51.94, 70.48, 32.51, 78.39, 75.58, -1.49])
#    B4L_coords=np.array([-112.5, -174.9, 71.1, 90.35, 2.85, -113.62])
        B4L_coords=np.array([-112.5-3, -174.9-3, 71.1-3, 90.35, 2.85, -113.62])

        B5L_angles=np.array([55.19, 70.48, 32.51, 78.48, 74.88, -0.79])
#    B5L_coords=np.array([-102.5, -181.4, 71.1, 90.38, 2.23, -109.67])
        B5L_coords=np.array([-102.5-3, -181.4-3, 71.1-3, 90.38, 2.23, -109.67])

        L_R_angles=np.array([89.12, 58.27, 44.82, 66.0, 74.88, -8.26])
        L_R_coords=np.array([16.0, -213.8, 96.4, 87.12, -2.43, -75.9])


        B1L_up_angles = B1L_angles + L_up_angles
        B1R_up_angles = B1L_angles + R_up_angles
        B1R_angles    = B1L_angles + R_angles

        B2L_up_angles = B2L_angles + L_up_angles
        B2R_up_angles = B2L_angles + R_up_angles
        B2R_angles    = B2L_angles + R_angles

        B3L_up_angles = B3L_angles + L_up_angles
        B3R_up_angles = B3L_angles + R_up_angles
        B3R_angles    = B3L_angles + R_angles

        B4L_up_angles = B4L_angles + L_up_angles
        B4R_up_angles = B4L_angles + R_up_angles
        B4R_angles    = B4L_angles + R_angles

        B5L_up_angles = B5L_angles + L_up_angles
        B5R_up_angles = B5L_angles + R_up_angles
        B5R_angles    = B5L_angles + R_angles

#    B1R_angles=[]
#    B1R_coords=[]

#    B2R_angles=[]
#    B2R_coords=[]

#    B3R_angles=[]
#    B3R_coords=[]

#    B4R_angles=[]
#    B4R_coords=[]

#    B5R_angles=[]
#    B5R_coords=[]


        print("=== init ==> L_R")
#    mycobot.send_angles(B1_LR_angles, speed) # 2021/12/24 => NG:average of B1L_up & B1R_up
#    mycobot.send_angles(L_R_angles, speed,0)
        mycobot.send_coords(L_R_coords, speed,0)
        time.sleep(wait)


#### B1 Start #################################
        print("===== 1L ==> B1L_up")
        mycobot.send_angles(B1L_up_angles, fast)
#    mycobot.send_coords(B1L_coords, speed,0)
        time.sleep(wait)
# set vacuum ON!
        if (vacuum_use):
            vacuum_on()
        print("===== 1L ==> B1L pickup")
#    mycobot.send_angles(B1L_angles, speed)
        mycobot.send_coords(B1L_coords, slow,0)
        time.sleep(wait)
        print("===== 1L ==> J2_up")
        mycobot.send_angles(B1L_up_angles, fast)
#    mycobot.send_coords(B1L_coords, speed,0)
        time.sleep(wait)
        print("===== 1R ==> J1_rotate_R")
        mycobot.send_angles(B1R_up_angles, fast)
#    mycobot.send_coords(B1R?_coords, speed,0)
        time.sleep(wait)
        print("===== 1R ==> J2_down")
        mycobot.send_angles(B1R_angles, slow)
#    mycobot.send_coords(B1R?_coords, speed,0)
        time.sleep(wait)
# set vacuum OFF!
        if (vacuum_use):
            vacuum_off()
        print("===== 1R ==> J2_up")
        mycobot.send_angles(B1R_up_angles, fast)
#    mycobot.send_coords(B1R?_coords, speed,0)
        time.sleep(wait)
        print("== 1-end ==> L_R")
        mycobot.send_angles(L_R_angles, fast)
#    mycobot.send_coords(L_R_coords, speed,0)
        time.sleep(wait)
#### B1 End ###################################
#### B2 Start #################################
        print("===== 2L ==> B2L_up")
        mycobot.send_angles(B2L_up_angles, fast)
#    mycobot.send_coords(B2L_coords, speed,0)
        time.sleep(wait)
# set vacuum ON!
        if (vacuum_use):
            vacuum_on()
        print("===== 2L ==> B2L pickup")
#    mycobot.send_angles(B2L_angles, speed)
        mycobot.send_coords(B2L_coords, slow,0)
        time.sleep(wait)
        print("===== 2L ==> J2_up")
        mycobot.send_angles(B2L_up_angles, fast)
#    mycobot.send_coords(B2L_coords, speed,0)
        time.sleep(wait)
        print("===== 2R ==> J1_rotate_R")
        mycobot.send_angles(B2R_up_angles, fast)
#    mycobot.send_coords(B2R?_coords, speed,0)
        time.sleep(wait)
        print("===== 2R ==> J2_down")
        mycobot.send_angles(B2R_angles, slow)
#    mycobot.send_coords(B2R?_coords, speed,0)
        time.sleep(wait)
# set vacuum OFF!
        if (vacuum_use):
            vacuum_off()
        print("===== 2R ==> J2_up")
        mycobot.send_angles(B2R_up_angles, fast)
#    mycobot.send_coords(B2R?_coords, speed,0)
        time.sleep(wait)
        print("== 2-end ==> L_R")
        mycobot.send_angles(L_R_angles, fast)
#    mycobot.send_coords(L_R_coords, speed,0)
        time.sleep(wait)
#### B2 End ###################################
#### B3 Start #################################
        print("===== 3L ==> B3L_up")
        mycobot.send_angles(B3L_up_angles, fast)
#    mycobot.send_coords(B3L_coords, speed,0)
        time.sleep(wait)
# set vacuum ON!
        if (vacuum_use):
            vacuum_on()
        print("===== 3L ==> B3L pickup")
#    mycobot.send_angles(B3L_angles, speed)
        mycobot.send_coords(B3L_coords, slow,0)
        time.sleep(wait)
        print("===== 3L ==> J2_up")
        mycobot.send_angles(B3L_up_angles, fast)
#    mycobot.send_coords(B3L_coords, speed,0)
        time.sleep(wait)
        print("===== 3R ==> J1_rotate_R")
        mycobot.send_angles(B3R_up_angles, fast)
#    mycobot.send_coords(B3R?_coords, speed,0)
        time.sleep(wait)
        print("===== 3R ==> J2_down")
        mycobot.send_angles(B3R_angles, slow)
#    mycobot.send_coords(B3R?_coords, speed,0)
        time.sleep(wait)
# set vacuum OFF!
        if (vacuum_use):
            vacuum_off()
        print("===== 3R ==> J2_up")
        mycobot.send_angles(B3R_up_angles, fast)
#    mycobot.send_coords(B3R?_coords, speed,0)
        time.sleep(wait)
        print("== 3-end ==> L_R")
        mycobot.send_angles(L_R_angles, fast)
#    mycobot.send_coords(L_R_coords, speed,0)
        time.sleep(wait)
#### B3 End ###################################
#### B4 Start #################################
        print("===== 4L ==> B4L_up")
        mycobot.send_angles(B4L_up_angles, fast)
#    mycobot.send_coords(B4L_coords, speed,0)
        time.sleep(wait)
# set vacuum ON!
        if (vacuum_use):
            vacuum_on()
        print("===== 4L ==> B4L pickup")
#    mycobot.send_angles(B4L_angles, speed)
        mycobot.send_coords(B4L_coords, slow,0)
        time.sleep(wait)
        print("===== 4L ==> J2_up")
        mycobot.send_angles(B4L_up_angles, fast)
#    mycobot.send_coords(B4L_coords, speed,0)
        time.sleep(wait)
        print("===== 4R ==> J1_rotate_R")
        mycobot.send_angles(B4R_up_angles, fast)
#    mycobot.send_coords(B4R?_coords, speed,0)
        time.sleep(wait)
        print("===== 4R ==> J2_down")
        mycobot.send_angles(B4R_angles, slow)
#    mycobot.send_coords(B4R?_coords, speed,0)
        time.sleep(wait)
# set vacuum OFF!
        if (vacuum_use):
            vacuum_off()
        print("===== 4R ==> J2_up")
        mycobot.send_angles(B4R_up_angles, fast)
#    mycobot.send_coords(B4R?_coords, speed,0)
        time.sleep(wait)
        print("== 4-end ==> L_R")
        mycobot.send_angles(L_R_angles, fast)
#    mycobot.send_coords(L_R_coords, speed,0)
        time.sleep(wait)
#### B4 End ###################################
#### B5 Start #################################
        print("===== 5L ==> B5L_up")
        mycobot.send_angles(B5L_up_angles, fast)
#    mycobot.send_coords(B5L_coords, speed,0)
        time.sleep(wait)
# set vacuum ON!
        if (vacuum_use):
            vacuum_on()
        print("===== 5L ==> B5L pickup")
#    mycobot.send_angles(B5L_angles, speed)
        mycobot.send_coords(B5L_coords, slow,0)
        time.sleep(wait)
        print("===== 5L ==> J2_up")
        mycobot.send_angles(B5L_up_angles, fast)
#    mycobot.send_coords(B5L_coords, speed,0)
        time.sleep(wait)
        print("===== 5R ==> J1_rotate_R")
        mycobot.send_angles(B5R_up_angles, fast)
#    mycobot.send_coords(B5R?_coords, speed,0)
        time.sleep(wait)
        print("===== 5R ==> J2_down")
        mycobot.send_angles(B5R_angles, slow)
#    mycobot.send_coords(B5R?_coords, speed,0)
        time.sleep(wait)
# set vacuum OFF!
        if (vacuum_use):
            vacuum_off()
        print("===== 5R ==> J2_up")
        mycobot.send_angles(B5R_up_angles, fast)
#    mycobot.send_coords(B5R?_coords, speed,0)
        time.sleep(wait)
        print("== 5-end ==> L_R")
        mycobot.send_angles(L_R_angles, fast)
#    mycobot.send_coords(L_R_coords, speed,0)
        time.sleep(wait)
#### B5 End ###################################

##############################################################
# angles for tray address
##############################################################
    if(t_ad_A):
# 1st trial()
# add adjust x,y,-5,-5
        '''
        A1L_angles=np.array([25.66, 55.01, 65.3, 60.73, -6.15, -0.7])
#        A1L_coords=np.array([-166.2, -155.6, 70.1, 91.04, 0.58, -58.17])
        A1L_coords=np.array([-166.2-5, -155.6-5, 70.1, 91.04, 0.58, -58.17])

        A2L_angles=np.array([28.47, 55.01, 65.21, 61.78, -5.97, -1.58])
#        A2L_coords=np.array([-157.4, -162.9, 69.5, 92.01, 1.37, -55.49])
        A2L_coords=np.array([-157.4-5, -162.9-5, 69.5, 92.01, 1.37, -55.49])
        '''

        A3L_angles=np.array([30.58, 53.08, 69.6, 57.04, -10.63, -2.63])
#        A3L_coords=np.array([-147.8, -170.8, 70.8, 89.74, 2.68, -48.79])
        A3L_coords=np.array([-147.8-3, -170.8-3, 70.8+1, 89.74, 2.68, -48.79])

        A4L_angles=np.array([34.01, 53.08, 69.6, 56.95, -7.82, -1.58])
#        A4L_coords=np.array([-139.0, -177.7, 70.9, 89.65, 1.62, -48.17])
        A4L_coords=np.array([-139.0-1, -177.7-3, 70.9+1, 89.65, 1.62, -48.17])

        A5L_angles=np.array([36.91, 53.08, 69.6, 56.86, -7.82, -2.54])
#        A5L_coords=np.array([-129.9, -184.6, 70.9, 89.56, 2.6, -45.28])
        A5L_coords=np.array([-129.9-1, -184.6-2, 70.9+1, 89.56, 2.6, -45.28])

        '''
        L_R_angles=np.array([71.54, 41.22, 69.52, 64.24, -13.18, 5.27])
        L_R_coords=np.array([2.4, -225.7, 109.3, 85.1, -4.11, -4.87])
        '''
#
# 2021/12/27 nakahide
# add adjust C1-C5        z,+1
# add adjust C3,C4,C5,    x,y,-5,-5
        A1L_angles=np.array([32.34, 60.73, 53.43, 67.76, 15.55, -0.35])
#        A1L_coords=np.array([-162.9, -163.7, 69.3, 91.86, 0.86, -73.19])
        A1L_coords=np.array([-162.9, -163.7, 69.3+1, 91.86, 0.86, -73.19])

        A2L_angles=np.array([35.33, 60.82, 53.08, 68.02, 15.55, -2.28])
#        A2L_coords=np.array([-154.3, -172.1, 69.6, 91.86, 2.8, -70.14])
        A2L_coords=np.array([-154.3, -172.1, 69.6+1, 91.86, 2.8, -70.14])

        '''
        A3L_angles=np.array([39.81, 60.82, 53.34, 67.32, 22.85, -2.28])
#        A3L_coords=np.array([-142.8, -178.5, 69.6, 91.37, 2.86, -72.97])
        A3L_coords=np.array([-142.8-6, -178.5-5, 69.6+1, 91.37, 2.86, -72.97])

        A4L_angles=np.array([42.71, 60.82, 53.34, 67.32, 22.67, -2.28])
#        A4L_coords=np.array([-133.5, -185.6, 69.6, 91.38, 2.86, -69.89])
        A4L_coords=np.array([-133.5-7, -185.6-5, 69.6+1, 91.38, 2.86, -69.89])

        A5L_angles=np.array([45.43, 60.82, 53.52, 67.32, 21.7, -2.28])
#        A5L_coords=np.array([-124.0, -192.2, 69.2, 91.55, 2.9, -66.19])
        A5L_coords=np.array([-124.0-7, -192.2-5, 69.2+1, 91.55, 2.9, -66.19])
        '''

        L_R_angles=np.array([83.67, 48.69, 52.99, 56.07, 21.88, -2.28])
        L_R_coords=np.array([19.1, -248.1, 131.1, 69.32, -5.97, -27.53])

        A1L_up_angles = A1L_angles + L_up_angles
        A1R_up_angles = A1L_angles + R_up_angles
        A1R_angles    = A1L_angles + R_angles

        A2L_up_angles = A2L_angles + L_up_angles
        A2R_up_angles = A2L_angles + R_up_angles
        A2R_angles    = A2L_angles + R_angles

        A3L_up_angles = A3L_angles + L_up_angles
        A3R_up_angles = A3L_angles + R_up_angles
        A3R_angles    = A3L_angles + R_angles

        A4L_up_angles = A4L_angles + L_up_angles
        A4R_up_angles = A4L_angles + R_up_angles
        A4R_angles    = A4L_angles + R_angles

        A5L_up_angles = A5L_angles + L_up_angles
        A5R_up_angles = A5L_angles + R_up_angles
        A5R_angles    = A5L_angles + R_angles

#    A1R_angles=[]
#    A1R_coords=[]

#    A2R_angles=[]
#    A2R_coords=[]

#    A3R_angles=[]
#    A3R_coords=[]

#    A4R_angles=[]
#    A4R_coords=[]

#    A5R_angles=[]
#    A5R_coords=[]


        print("=== init ==> L_R")
#    mycobot.send_angles(A1_LR_angles, speed) # 2021/12/24 => NG:average of A1L_up & A1R_up
#    mycobot.send_angles(L_R_angles, speed,0)
        mycobot.send_coords(L_R_coords, speed,0)
        time.sleep(wait)


#### A1 Start #################################
        print("===== 1L ==> A1L_up")
        mycobot.send_angles(A1L_up_angles, fast)
#    mycobot.send_coords(A1L_coords, speed,0)
        time.sleep(wait)
# set vacuum ON!
        if (vacuum_use):
            vacuum_on()
        print("===== 1L ==> A1L pickup")
#    mycobot.send_angles(A1L_angles, speed)
        mycobot.send_coords(A1L_coords, slow,0)
        time.sleep(wait)
        print("===== 1L ==> J2_up")
        mycobot.send_angles(A1L_up_angles, fast)
#    mycobot.send_coords(A1L_coords, speed,0)
        time.sleep(wait)
        print("===== 1R ==> J1_rotate_R")
        mycobot.send_angles(A1R_up_angles, fast)
#    mycobot.send_coords(A1R?_coords, speed,0)
        time.sleep(wait)
        print("===== 1R ==> J2_down")
        mycobot.send_angles(A1R_angles, slow)
#    mycobot.send_coords(A1R?_coords, speed,0)
        time.sleep(wait)
# set vacuum OFF!
        if (vacuum_use):
            vacuum_off()
        print("===== 1R ==> J2_up")
        mycobot.send_angles(A1R_up_angles, fast)
#    mycobot.send_coords(A1R?_coords, speed,0)
        time.sleep(wait)
        print("== 1-end ==> L_R")
        mycobot.send_angles(L_R_angles, fast)
#    mycobot.send_coords(L_R_coords, speed,0)
        time.sleep(wait)
#### A1 End ###################################
#### A2 Start #################################
        print("===== 2L ==> A2L_up")
        mycobot.send_angles(A2L_up_angles, fast)
#    mycobot.send_coords(A2L_coords, speed,0)
        time.sleep(wait)
# set vacuum ON!
        if (vacuum_use):
            vacuum_on()
        print("===== 2L ==> A2L pickup")
#    mycobot.send_angles(A2L_angles, speed)
        mycobot.send_coords(A2L_coords, slow,0)
        time.sleep(wait)
        print("===== 2L ==> J2_up")
        mycobot.send_angles(A2L_up_angles, fast)
#    mycobot.send_coords(A2L_coords, speed,0)
        time.sleep(wait)
        print("===== 2R ==> J1_rotate_R")
        mycobot.send_angles(A2R_up_angles, fast)
#    mycobot.send_coords(A2R?_coords, speed,0)
        time.sleep(wait)
        print("===== 2R ==> J2_down")
        mycobot.send_angles(A2R_angles, slow)
#    mycobot.send_coords(A2R?_coords, speed,0)
        time.sleep(wait)
# set vacuum OFF!
        if (vacuum_use):
            vacuum_off()
        print("===== 2R ==> J2_up")
        mycobot.send_angles(A2R_up_angles, fast)
#    mycobot.send_coords(A2R?_coords, speed,0)
        time.sleep(wait)
        print("== 2-end ==> L_R")
        mycobot.send_angles(L_R_angles, fast)
#    mycobot.send_coords(L_R_coords, speed,0)
        time.sleep(wait)
#### A2 End ###################################
#### A3 Start #################################
        print("===== 3L ==> A3L_up")
        mycobot.send_angles(A3L_up_angles, fast)
#    mycobot.send_coords(A3L_coords, speed,0)
        time.sleep(wait)
# set vacuum ON!
        if (vacuum_use):
            vacuum_on()
        print("===== 3L ==> A3L pickup")
#    mycobot.send_angles(A3L_angles, speed)
        mycobot.send_coords(A3L_coords, slow,0)
        time.sleep(wait)
        print("===== 3L ==> J2_up")
        mycobot.send_angles(A3L_up_angles, fast)
#    mycobot.send_coords(A3L_coords, speed,0)
        time.sleep(wait)
        print("===== 3R ==> J1_rotate_R")
        mycobot.send_angles(A3R_up_angles, fast)
#    mycobot.send_coords(A3R?_coords, speed,0)
        time.sleep(wait)
        print("===== 3R ==> J2_down")
        mycobot.send_angles(A3R_angles, slow)
#    mycobot.send_coords(A3R?_coords, speed,0)
        time.sleep(wait)
# set vacuum OFF!
        if (vacuum_use):
            vacuum_off()
        print("===== 3R ==> J2_up")
        mycobot.send_angles(A3R_up_angles, fast)
#    mycobot.send_coords(A3R?_coords, speed,0)
        time.sleep(wait)
        print("== 3-end ==> L_R")
        mycobot.send_angles(L_R_angles, fast)
#    mycobot.send_coords(L_R_coords, speed,0)
        time.sleep(wait)
#### A3 End ###################################
#### A4 Start #################################
        print("===== 4L ==> A4L_up")
        mycobot.send_angles(A4L_up_angles, fast)
#    mycobot.send_coords(A4L_coords, speed,0)
        time.sleep(wait)
# set vacuum ON!
        if (vacuum_use):
            vacuum_on()
        print("===== 4L ==> A4L pickup")
#    mycobot.send_angles(A4L_angles, speed)
        mycobot.send_coords(A4L_coords, slow,0)
        time.sleep(wait)
        print("===== 4L ==> J2_up")
        mycobot.send_angles(A4L_up_angles, fast)
#    mycobot.send_coords(A4L_coords, speed,0)
        time.sleep(wait)
        print("===== 4R ==> J1_rotate_R")
        mycobot.send_angles(A4R_up_angles, fast)
#    mycobot.send_coords(A4R?_coords, speed,0)
        time.sleep(wait)
        print("===== 4R ==> J2_down")
        mycobot.send_angles(A4R_angles, slow)
#    mycobot.send_coords(A4R?_coords, speed,0)
        time.sleep(wait)
# set vacuum OFF!
        if (vacuum_use):
            vacuum_off()
        print("===== 4R ==> J2_up")
        mycobot.send_angles(A4R_up_angles, fast)
#    mycobot.send_coords(A4R?_coords, speed,0)
        time.sleep(wait)
        print("== 4-end ==> L_R")
        mycobot.send_angles(L_R_angles, fast)
#    mycobot.send_coords(L_R_coords, speed,0)
        time.sleep(wait)
#### A4 End ###################################
#### A5 Start #################################
        print("===== 5L ==> A5L_up")
        mycobot.send_angles(A5L_up_angles, fast)
#    mycobot.send_coords(A5L_coords, speed,0)
        time.sleep(wait)
# set vacuum ON!
        if (vacuum_use):
            vacuum_on()
        print("===== 5L ==> A5L pickup")
#    mycobot.send_angles(A5L_angles, speed)
        mycobot.send_coords(A5L_coords, slow,0)
        time.sleep(wait)
        print("===== 5L ==> J2_up")
        mycobot.send_angles(A5L_up_angles, fast)
#    mycobot.send_coords(A5L_coords, speed,0)
        time.sleep(wait)
        print("===== 5R ==> J1_rotate_R")
        mycobot.send_angles(A5R_up_angles, fast)
#    mycobot.send_coords(A5R?_coords, speed,0)
        time.sleep(wait)
        print("===== 5R ==> J2_down")
        mycobot.send_angles(A5R_angles, slow)
#    mycobot.send_coords(A5R?_coords, speed,0)
        time.sleep(wait)
# set vacuum OFF!
        if (vacuum_use):
            vacuum_off()
        print("===== 5R ==> J2_up")
        mycobot.send_angles(A5R_up_angles, fast)
#    mycobot.send_coords(A5R?_coords, speed,0)
        time.sleep(wait)
        print("== 5-end ==> L_R")
        mycobot.send_angles(L_R_angles, fast)
#    mycobot.send_coords(L_R_coords, speed,0)
        time.sleep(wait)
#### A5 End ###################################

    '''
    print("===== 0 ==> L_R")
#    mycobot.send_angles(L_R_angles, speed)
    mycobot.send_coords(L_R_coords, speed,0)
    time.sleep(wait)
    '''

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
