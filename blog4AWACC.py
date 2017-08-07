#“Written by : @ncscomputing /@warksraspijam”
 
from mcpi import minecraft as minecraft
from mcpi import block as block
from datetime import datetime
import time
import random
import BuildWorldDM as bw

###
"""
Written by @ncscomputing on top of the bitio produced by David Whale
https://github.com/whaleygeek/bitio

world building code imported library from Damien Mooney's blog:
https://damianmooney.wordpress.com/2016/02/16/raspberry-pi-minecraft-iss-tracker/

"""
import serial
from mcpi.minecraft import Minecraft
import time
from mcpi import block as block
import random


mc = Minecraft.create()


# button.py - demonstrates using a button

import microbit

print("micro:bit connected - press button A to test")
WoolList = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
 
EngX = 1.0
EngZ = 50.0
 
UsaX =  53.8
UsaZ = 39.7
 
CanadaX = 59.0
CanadaZ = 61.3
 
IceLandX = 10.0
IceLandZ = 61.1

##

##

def Teleport(x,z,Country):
    mc.player.setPos(x,20,z)
    mc.camera.setFollow()
    mc.setBlock(x,1, z,35,random.choice(WoolList))
    mc.postToChat(Country)

while True:
    time.sleep(0.25)
    #=======buildworld call when a button pressed
    if microbit.button_a.was_pressed():
        mc.postToChat("Button A pressed: build world")    
        print("Button A pressed: build world")

        bw.Build()
        time.sleep(2)
 
        microbit.display.show("build world")


    # manual teleport using acceleromter readings
    pos = mc.player.getTilePos()
    x = microbit.accelerometer.get_x()/300 # -ve=left/+ve=right
    y = microbit.accelerometer.get_y()/300 # -ve=forward/+ve=backward

    pos.x += x # east/west
    pos.z += y # north/south

    mc.player.setTilePos(pos.x, pos.y, pos.z) # set player position

    #time.sleep(0.5)
    #=========
    if microbit.button_b.was_pressed(): 
        print ("Button B pressed: Manual teleport")
        mc.postToChat("Button B pressed: Teleport")  
        time.sleep(0.5)
        Teleport(EngX,EngZ,"England")
        time.sleep(8)
        Teleport(UsaX,UsaZ,"USA")
        time.sleep(8)
        Teleport(CanadaX,CanadaZ,"Canada")
        time.sleep(8)
        Teleport(IceLandX,IceLandZ,"Iceland")
        time.sleep(8)
