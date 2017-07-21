#Original written by David Whale located here as part of his BITIO library
#https://github.com/whaleygeek/bitio/blob/master/src/tilt_mc.py
#adapted by @ncscomputing 20/07/17


import mcpi.minecraft as minecraft
import mcpi.block as block
import microbit
import time
import random




mc = minecraft.Minecraft.create()

blocksList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
time.sleep(7)
mc.postToChat("Rainbow Road 3.0 Micro:bit controlled")
while True:
    pos = mc.player.getTilePos()
    x = microbit.accelerometer.get_x()/300 # -ve=left/+ve=right
    y = microbit.accelerometer.get_y()/300 # -ve=forward/+ve=backward

    pos.x += x # east/west
    pos.z += y # north/south

    Count = 1
    while Count <=16 :
        mc.player.setTilePos(pos.x, pos.y, pos.z)
        mc.setBlock(pos.x-Count, pos.y-1, pos.z,35,Count)
        Count = Count+1
    time.sleep(0.25)
