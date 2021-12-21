# direct_pp_coords.py
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

# angles for tray address

# 6th trial(pickup +11mm,change & C4R,C5R=> hand setting )
    C1L_angles=[55.89, 69.96, 50.18, 60.02, 79.36, -2.1]
    C1L_coords=[-93.8, -171.8, 45.7, 90.03, 2.28, -113.46]
#    C1L_coords=[-93.8, -171.8, 45.7-1, 90.03, 2.28, -113.46]

    C2L_angles=[59.67, 69.96, 50.18, 59.94, 84.46, -0.79]
#    C2L_coords=[-80.8, -173.9, 45.7, 90.0, 0.87, -114.78]
#    C2L_coords=[-80.8, -173.9, 45.7-2, 90.0, 0.87, -114.78]
#    C2L_coords=[-80.8, -173.9, 45.7-3, 90.0, 0.87, -114.78]
    C2L_coords=[-80.8, -173.9, 45.7-4, 90.0, 0.87, -114.78]

    C3L_angles=[63.01, 64.95, 60.38, 54.05, 83.75, 0.08]
#    C3L_coords=[-67.4, -172.2, 47.4, 89.93, -0.69, -110.74]
    C3L_coords=[-67.4, -172.2, 47.4-2, 89.93, -0.69, -110.74]

    C4L_angles=[66.09, 65.12, 60.29, 49.3, 93.42, -4.65]
#    C4L_coords=[-57.6, -174.1, 47.0, 90.31, -0.6, -117.32]
    C4L_coords=[-57.6, -174.1, 47.0-2, 90.31, -0.6, -117.32]

    C5L_angles=[69.52, 63.36, 65.56, 48.69, 90.08, -4.21]
#    C5L_coords=[-45.0, -171.4, 45.3, 90.0, 1.84, -110.56]
#    C5L_coords=[-45.0, -171.4, 45.3-2, 90.0, 1.84, -110.56]
#    C5L_coords=[-45.0+1, -171.4, 45.3-3, 90.0, 1.84, -110.56]
    C5L_coords=[-45.0+2, -171.4+2, 45.3-3, 90.0, 1.84, -110.56]


    L_R_angles=[90.52, 30.32, 105.29, 46.75, 55.63, -0.61]
    L_R_coords=[27.0, -145.2, 81.8, 91.34, 2.57, -55.07]

#    L_angles=[61.25, 42.27, 67.5, 71.8, 65.39, -3.25]
#    L_coords=[-68.0, -169.7, 104.8, 90.66, 4.69, -94.08]
#    R_angles=[123.22, 50.18, 56.77, 75.76, 62.22, 0.26]
#    R_coords=[125.8, -150.0, 98.0, 91.22, 2.06, -28.98]


    C1R_angles=[117.5, 62.31, 68.37, 50.18, 72.15, -1.05]
    C1R_coords=[102.4, -153.3, 44.6, 90.26, 1.89, -44.64]

    C2R_angles=[120.41, 62.13, 68.29, 50.8, 65.74, -1.14]
    C2R_coords=[113.8, -150.9, 45.1, 90.5, 2.26, -35.31]

    C3R_angles=[122.25, 61.96, 68.9, 50.8, 57.91, -2.02]
    C3R_coords=[123.4, -149.2, 44.5, 90.88, 3.43, -25.62]

    C4R_angles=[125.68, 65.91, 54.93, 60.82, 62.31, 2.1]
    C4R_coords=[136.6, -150.8, 51.4, 90.77, -0.63, -26.64]

    C5R_angles=[126.03, 66.53, 55.98, 59.76, 52.64, 4.3]
    C5R_coords=[143.6, -151.3, 47.4, 91.38, -2.48, -16.69]
    
    #########################################################
    '''
# 5th trial(pickup +11mm,L side angle change & C4R,C5R )
    C1L_angles=[55.89, 69.96, 50.18, 60.02, 79.36, -2.1]
    C1L_coords=[-93.8, -171.8, 45.7, 90.03, 2.28, -113.46]

    C2L_angles=[59.67, 69.96, 50.18, 59.94, 84.46, -0.79]
    C2L_coords=[-80.8, -173.9, 45.7, 90.0, 0.87, -114.78]

    C3L_angles=[63.01, 64.95, 60.38, 54.05, 83.75, 0.08]
    C3L_coords=[-67.4, -172.2, 47.4, 89.93, -0.69, -110.74]

    C4L_angles=[66.09, 65.12, 60.29, 49.3, 93.42, -4.65]
    C4L_coords=[-57.6, -174.1, 47.0, 90.31, -0.6, -117.32]

    C5L_angles=[69.52, 63.36, 65.56, 48.69, 90.08, -4.21]
    C5L_coords=[-45.0, -171.4, 45.3, 90.0, 1.84, -110.56]


    L_R_angles=[90.52, 30.32, 105.29, 46.75, 55.63, -0.61]
    L_R_coords=[27.0, -145.2, 81.8, 91.34, 2.57, -55.07]

#    L_angles=[61.25, 42.27, 67.5, 71.8, 65.39, -3.25]
#    L_coords=[-68.0, -169.7, 104.8, 90.66, 4.69, -94.08]
#    R_angles=[123.22, 50.18, 56.77, 75.76, 62.22, 0.26]
#    R_coords=[125.8, -150.0, 98.0, 91.22, 2.06, -28.98]


    C1R_angles=[117.5, 62.31, 68.37, 50.18, 72.15, -1.05]
    C1R_coords=[102.4, -153.3, 44.6, 90.26, 1.89, -44.64]

    C2R_angles=[120.41, 62.13, 68.29, 50.8, 65.74, -1.14]
    C2R_coords=[113.8, -150.9, 45.1, 90.5, 2.26, -35.31]

    C3R_angles=[122.25, 61.96, 68.9, 50.8, 57.91, -2.02]
    C3R_coords=[123.4, -149.2, 44.5, 90.88, 3.43, -25.62]

    C4R_angles=[120.84, 55.37, 84.81, 37.61, 40.86, -2.1]
    C4R_coords=[126.0, -145.6, 46.5, 88.33, 0.67, -10.05]

    C5R_angles=[123.92, 59.58, 74.7, 45.43, 42.45, -0.35]
    C5R_coords=[137.5, -146.0, 45.1, 89.8, 0.17, -8.52]
    '''
################################################################
    '''
# 4th trial(pickup +11mm,L side angle change & C4R,C5R )
    C1L_angles=[15.46, 54.66, 85.25, 37.08, -92.02, 0.26]
    C1L_coords=[-119.5, -146.1, 46.5, 90.1, 2.72, 17.49]

    C2L_angles=[15.99, 54.75, 85.34, 39.46, -96.32, -2.1]
    C2L_coords=[-111.6, -145.1, 46.1, 90.04, 2.54, 22.32]

    C3L_angles=[19.95, 57.56, 77.43, 45.43, -105.73, -1.4]
    C3L_coords=[-102.6, -151.3, 47.5, 89.88, 0.98, 35.68]

    C4L_angles=[20.47, 56.95, 80.24, 45.87, -110.65, -5.88]
    C4L_coords=[-91.8, -147.5, 46.9, 88.91, 3.0, 41.04]

    C5L_angles=[24.16, 56.95, 80.24, 44.82, -113.55, -4.04]
    C5L_coords=[-81.8, -152.0, 46.6, 89.19, 2.18, 47.68]


    L_R_angles=[90.52, 30.32, 105.29, 46.75, 55.63, -0.61]
    L_R_coords=[27.0, -145.2, 81.8, 91.34, 2.57, -55.07]

#    L_angles=[61.25, 42.27, 67.5, 71.8, 65.39, -3.25]
#    L_coords=[-68.0, -169.7, 104.8, 90.66, 4.69, -94.08]
#    R_angles=[123.22, 50.18, 56.77, 75.76, 62.22, 0.26]
#    R_coords=[125.8, -150.0, 98.0, 91.22, 2.06, -28.98]


    C1R_angles=[117.5, 62.31, 68.37, 50.18, 72.15, -1.05]
    C1R_coords=[102.4, -153.3, 44.6, 90.26, 1.89, -44.64]

    C2R_angles=[120.41, 62.13, 68.29, 50.8, 65.74, -1.14]
    C2R_coords=[113.8, -150.9, 45.1, 90.5, 2.26, -35.31]

    C3R_angles=[122.25, 61.96, 68.9, 50.8, 57.91, -2.02]
    C3R_coords=[123.4, -149.2, 44.5, 90.88, 3.43, -25.62]

    C4R_angles=[119.17, 55.81, 84.02, 40.42, 33.31, -1.14]
    C4R_coords=[126.6, -148.0, 44.6, 90.22, 1.28, -4.12]

    C5R_angles=[122.95, 59.23, 74.61, 47.63, 34.18, -0.17]
    C5R_coords=[140.4, -147.1, 45.1, 91.23, 1.01, -1.21]
    '''
################################################################
    '''
# 3rd trial(pickup +11mm)
    C1L_angles=[51.41, 56.68, 80.59, 44.64, 47.9, -1.93]
    C1L_coords=[-92.5, -163.3, 45.2, 91.29, 3.36, -86.42]

    C2L_angles=[54.4, 53.17, 89.73, 36.91, 46.93, -2.9]
    C2L_coords=[-78.9, -161.9, 45.8, 89.87, 2.77, -82.53]

    C3L_angles=[58.35, 53.08, 89.73, 37.44, 54.58, -2.02]
    C3L_coords=[-68.0, -160.5, 45.8, 90.15, 2.23, -86.21]

    C4L_angles=[64.07, 56.42, 81.47, 45.17, 66.09, 0.43]
    C4L_coords=[-55.1, -163.0, 45.1, 91.24, 2.37, -92.0]

    C5L_angles=[68.11, 54.31, 87.18, 39.81, 64.51, -0.61]
    C5L_coords=[-41.7, -163.5, 45.0, 90.56, 1.8, -86.38]


    L_R_angles=[90.52, 30.32, 105.29, 46.75, 55.63, -0.61]
    L_R_coords=[27.0, -145.2, 81.8, 91.34, 2.57, -55.07]

#    L_angles=[61.25, 42.27, 67.5, 71.8, 65.39, -3.25]
#    L_coords=[-68.0, -169.7, 104.8, 90.66, 4.69, -94.08]
#    R_angles=[123.22, 50.18, 56.77, 75.76, 62.22, 0.26]
#    R_coords=[125.8, -150.0, 98.0, 91.22, 2.06, -28.98]


    C1R_angles=[117.5, 62.31, 68.37, 50.18, 72.15, -1.05]
    C1R_coords=[102.4, -153.3, 44.6, 90.26, 1.89, -44.64]

    C2R_angles=[120.41, 62.13, 68.29, 50.8, 65.74, -1.14]
    C2R_coords=[113.8, -150.9, 45.1, 90.5, 2.26, -35.31]

    C3R_angles=[122.25, 61.96, 68.9, 50.8, 57.91, -2.02]
    C3R_coords=[123.4, -149.2, 44.5, 90.88, 3.43, -25.62]

    C4R_angles=[124.1, 63.01, 66.35, 51.76, 53.96, -1.23]
    C4R_coords=[132.9, -149.0, 44.8, 90.67, 2.15, -19.84]

    C5R_angles=[126.73, 68.02, 54.4, 59.85, 57.39, 1.05]
    C5R_coords=[142.6, -149.3, 45.0, 91.23, 0.87, -20.65]
    '''
################################################################
    '''
# 2nd trial(pickup +7mm)
    C1L_angles=[52.91, 60.64, 74.88, 46.23, 54.75, 0.61]
    C1L_coords=[-92.1, -165.3, 41.0, 91.01, 0.82, -91.84]

    C2L_angles=[55.89, 58.35, 80.85, 41.92, 54.49, -0.7]
    C2L_coords=[-80.0, -165.1, 40.8, 90.66, 1.63, -88.58]

    C3L_angles=[58.27, 56.07, 86.74, 39.19, 52.82, -0.52]
    C3L_coords=[-68.7, -162.6, 40.3, 91.22, 2.13, -84.52]

    C4L_angles=[63.89, 57.12, 84.11, 40.86, 61.69, -0.96]
    C4L_coords=[-54.6, -164.3, 40.4, 91.0, 2.82, -87.76]

    C5L_angles=[66.0, 54.58, 90.52, 37.61, 55.63, 0.43]
    C5L_coords=[-44.3, -163.0, 40.2, 91.53, 1.8, -79.61]


    L_R_angles=[90.52, 30.32, 105.29, 46.75, 55.63, -0.61]
    L_R_coords=[27.0, -145.2, 81.8, 91.34, 2.57, -55.07]


    C1R_angles=[116.98, 60.99, 74.44, 47.54, 63.01, -0.17]
    C1R_coords=[102.2, -150.6, 40.3, 91.35, 2.83, -35.99]

    C2R_angles=[117.5, 59.15, 78.22, 45.52, 52.11, 0.61]
    C2R_coords=[109.2, -150.4, 40.8, 91.78, 1.67, -24.59]

    C3R_angles=[120.41, 63.45, 67.32, 54.14, 53.78, 1.66]
    C3R_coords=[120.0, -151.9, 40.7, 92.9, 2.3, -23.36]

    C4R_angles=[123.92, 64.24, 66.62, 50.88, 53.52, -0.61]
    C4R_coords=[132.0, -148.3, 40.5, 91.04, 2.02, -19.57]

    C5R_angles=[124.18, 64.07, 67.14, 51.15, 42.89, -0.61]
    C5R_coords=[140.1, -148.7, 39.8, 91.73, 2.22, -8.65]
    '''
##############################################################
    ''' 1st trial(pickup girigiri)
    C1L_angles=[30.14, 51.06, 108.98, 19.07, -18.89, -0.7]
    C1L_coords=[-101.6, -149.4, 35.9, 89.16, 0.98, -40.96]

    C2L_angles=[38.14, 49.83, 113.37, 15.9, 1.4, -0.43]
    C2L_coords=[-86.4, -147.0, 36.1, 89.12, 0.41, -53.26]

    C3L_angles=[25.22, 49.65, 115.31, 14.5, -47.9, -0.08]
    C3L_coords=[-85.4, -147.7, 35.2, 89.64, 0.47, -16.87]

    C4L_angles=[19.95, 49.65, 116.63, 13.27, -69.52, -0.79]
    C4L_coords=[-79.8, -141.8, 34.4, 89.84, 1.2, -0.53]

    C5L_angles=[19.95, 49.57, 113.11, 14.76, -88.33, 0.35]
    C5L_coords=[-73.0, -142.4, 36.2, 89.92, 2.19, 18.28]


    L_R_angles=[70.04, 44.47, 79.89, 54.66, -19.33, -0.87]
    L_R_coords=[5.2, -215.6, 81.4, 89.08, 1.19, -0.63]


    C1R_angles=[111.79, 55.01, 96.32, 27.33, 40.86, -0.26]
    C1R_coords=[95.2, -147.8, 36.0, 89.0, -0.59, -19.06]

    C2R_angles=[112.14, 54.31, 97.64, 26.89, 31.81, 0.0]
    C2R_coords=[102.4, -147.2, 36.6, 89.02, -0.6, -9.66]

    C3R_angles=[111.7, 54.05, 99.84, 24.69, 18.19, -0.96]
    C3R_coords=[111.0, -146.0, 35.8, 88.66, 0.52, 3.49]

    C4R_angles=[112.32, 54.93, 97.11, 27.24, 8.96, -2.19]
    C4R_coords=[120.9, -146.3, 35.3, 89.3, 2.08, 13.33]

    C5R_angles=[112.32, 55.81, 94.83, 28.12, 0.43, -1.4]
    C5R_coords=[128.8, -147.7, 35.5, 88.76, 1.39, 21.85]
    '''


    print("===== 0 ==> L_R")
#    mycobot.send_angles(L_R_angles, speed)
    mycobot.send_coords(L_R_coords, speed,0)
    time.sleep(wait)

# set vacuum ON!
    print("GPIO20,GPIO21 output-L => vacuum ON")
    GPIO.setup(20,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(21,GPIO.OUT,initial=GPIO.LOW)
    time.sleep(.5)

    print("===== 1L ==> C1L")
#    mycobot.send_angles(C1L_angles, speed)
    mycobot.send_coords(C1L_coords, speed,0)
    time.sleep(wait)

    print("===== 0 ==> L_R")
#    mycobot.send_angles(L_R_angles, speed)
    mycobot.send_coords(L_R_coords, speed,0)
    time.sleep(wait)

    print("===== 1R ==> C1R")
#    mycobot.send_angles(C1R_angles, speed)
    mycobot.send_coords(C1R_coords, speed,0)
    time.sleep(wait)

# set vacuum OFF!
    print("GPIO20,GPIO21 output-H => vacuum OFF")
    GPIO.setup(20,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(21,GPIO.OUT,initial=GPIO.HIGH)
    time.sleep(.5)


    print("===== 0 ==> L_R")
    mycobot.send_angles(L_R_angles, speed)
#    mycobot.send_coords(L_R_coords, speed,0)
    time.sleep(wait)

# set vacuum ON!
    print("GPIO20,GPIO21 output-L => vacuum ON")
    GPIO.setup(20,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(21,GPIO.OUT,initial=GPIO.LOW)
    time.sleep(.5)

    print("===== 2L ==> C2L")
#    mycobot.send_angles(C2L_angles, speed)
    mycobot.send_coords(C2L_coords, speed,0)
    time.sleep(wait)

    print("===== 0 ==> L_R")
#    mycobot.send_angles(L_R_angles, speed)
    mycobot.send_coords(L_R_coords, speed,0)
    time.sleep(wait)

    print("===== 2R ==> C2R")
#    mycobot.send_angles(C2R_angles, speed)
    mycobot.send_coords(C2R_coords, speed,0)
    time.sleep(wait)

# set vacuum OFF!
    print("GPIO20,GPIO21 output-H => vacuum OFF")
    GPIO.setup(20,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(21,GPIO.OUT,initial=GPIO.HIGH)
    time.sleep(.5)


    print("===== 0 ==> L_R")
#    mycobot.send_angles(L_R_angles, speed)
    mycobot.send_coords(L_R_coords, speed,0)
    time.sleep(wait)

# set vacuum ON!
    print("GPIO20,GPIO21 output-L => vacuum ON")
    GPIO.setup(20,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(21,GPIO.OUT,initial=GPIO.LOW)
    time.sleep(.5)

    print("===== 3L ==> C3L")
#    mycobot.send_angles(C3L_angles, speed)
    mycobot.send_coords(C3L_coords, speed,0)
    time.sleep(wait)

    print("===== 0 ==> L_R")
#    mycobot.send_angles(L_R_angles, speed)
    mycobot.send_coords(L_R_coords, speed,0)
    time.sleep(wait)

    print("===== 3R ==> C3R")
#    mycobot.send_angles(C3R_angles, speed)
    mycobot.send_coords(C3R_coords, speed,0)
    time.sleep(wait)

# set vacuum OFF!
    print("GPIO20,GPIO21 output-H => vacuum OFF")
    GPIO.setup(20,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(21,GPIO.OUT,initial=GPIO.HIGH)
    time.sleep(.5)


    print("===== 0 ==> L_R")
#    mycobot.send_angles(L_R_angles, speed)
    mycobot.send_coords(L_R_coords, speed,0)
    time.sleep(wait)

# set vacuum ON!
    print("GPIO20,GPIO21 output-L => vacuum ON")
    GPIO.setup(20,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(21,GPIO.OUT,initial=GPIO.LOW)
    time.sleep(.5)

    print("===== 4L ==> C4L")
#    mycobot.send_angles(C4L_angles, speed)
    mycobot.send_coords(C4L_coords, speed,0)
    time.sleep(wait)

    print("===== 0 ==> L_R")
#    mycobot.send_angles(L_R_angles, speed)
    mycobot.send_coords(L_R_coords, speed,0)
    time.sleep(wait)

    print("===== 4R ==> C4R")
#    mycobot.send_angles(C4R_angles, speed)
    mycobot.send_coords(C4R_coords, speed,0)
    time.sleep(wait)

# set vacuum OFF!
    print("GPIO20,GPIO21 output-H => vacuum OFF")
    GPIO.setup(20,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(21,GPIO.OUT,initial=GPIO.HIGH)
    time.sleep(.5)



    print("===== 0 ==> L_R")
#    mycobot.send_angles(L_R_angles, speed)
    mycobot.send_coords(L_R_coords, speed,0)
    time.sleep(wait)

# set vacuum ON!
    print("GPIO20,GPIO21 output-L => vacuum ON")
    GPIO.setup(20,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(21,GPIO.OUT,initial=GPIO.LOW)
    time.sleep(.5)

    print("===== 5L ==> C5L")
#    mycobot.send_angles(C5L_angles, speed)
    mycobot.send_coords(C5L_coords, speed,0)
    time.sleep(wait)

    print("===== 0 ==> L_R")
#    mycobot.send_angles(L_R_angles, speed)
    mycobot.send_coords(L_R_coords, speed,0)
    time.sleep(wait)

    print("===== 5R ==> C5R")
#    mycobot.send_angles(C5R_angles, speed)
    mycobot.send_coords(C5R_coords, speed,0)
    time.sleep(wait)

# set vacuum OFF!
    print("GPIO20,GPIO21 output-H => vacuum OFF")
    GPIO.setup(20,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(21,GPIO.OUT,initial=GPIO.HIGH)
    time.sleep(.5)


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
