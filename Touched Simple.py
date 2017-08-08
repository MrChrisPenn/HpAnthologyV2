# touched.py - demonstrates using pin touch

import microbit
from mcpi import minecraft as minecraft
from mcpi import block as block
import time
import random

WoolList = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

 
mc = minecraft.Minecraft.create()
 

while True:
    
    time.sleep(1)
    if microbit.pin0.is_touched():
        msg = "Pin 0 touched, Wool block colour 0"
        print(msg)
        mc.postToChat(msg)
        pos = mc.player.getTilePos()
        mc.setBlock(pos.x, pos.y-1, pos.z,35,0)
    if microbit.pin1.is_touched():
        msg = "Pin 1 touched, Wool block colour 1"
        print(msg)
        mc.postToChat(msg)
        pos = mc.player.getTilePos()
        mc.setBlock(pos.x, pos.y-1, pos.z,35,1)
    if microbit.pin2.is_touched():
        msg = "Pin 2 touched, Wool block colour 2"
        print(msg)
        mc.postToChat(msg)
        pos = mc.player.getTilePos()
        mc.setBlock(pos.x, pos.y-1, pos.z,35,2)
        
