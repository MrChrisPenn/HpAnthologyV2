# touched.py - demonstrates using pin touch

import microbit

from mcpi import minecraft as minecraft
from mcpi import block as block
from datetime import datetime
import time
import serial
import random
import BuildWorldDM as bw

WoolList =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
EngX = 1.0
EngZ = 50.0

UsaX = 53.8
UsaZ = 39.7
 
mc = minecraft.Minecraft.create()
  
def Teleport(x,z,Country):
    mc.player.setPos(x,20,z)
    mc.camera.setFollow()
    mc.setBlock(x,1, z,35,random.choice(WoolList))
    mc.postToChat(Country)


while True:
    time.sleep(1)
    if microbit.pin0.is_touched():
        print("Pin 0 touched, build world")
        bw.Build()
    elif microbit.pin1.is_touched():
        print("Pin 1 touched, teleport to England")
        Teleport(EngX,EngZ,"England")
    elif microbit.pin2.is_touched():
        print("Pin 2 touched, teleport to the USA") 
        Teleport(UsaX,UsaZ,"USA")
