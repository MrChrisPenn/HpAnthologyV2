"""
Tweeting ISS current position at set intervals with Minecraft Pi.
Get current ISS position from http://wheretheiss.at/ and map it on
a raspberry pi with minecraft
Damian Mooney wrote this minecraft Tracker in 2016. I have added a few
features on top, namely:
walking random wool blocks to mark current and positions
ability to screenshot the position using Martin O'Hanlons raspi2png tutorial:
(http://www.stuffaboutcode.com/2016/03/raspberry-pi-take-screenshot-of.html)
ability to tweet that using twython python library
"""
__author__ = '@damianmooney' #additions by @ncscomputing
from mcpi import minecraft as minecraft
from mcpi import block as block
from datetime import datetime
import time
import urllib2
import json
import random
import subprocess # to run shell script to autocall raspi2png
import sys
from twython import Twython
import BuildWorldDM as BuildWorld


consumer_key = '5wcNNDJBX2W9GI4IfExb4Pi4F'
consumer_secret = 'rrm6oH3elfBYChkLfS4WptYhcTidsxKt6BJ37xiyfQbpokVUJw'
access_token = '726847769592401920-fAwjImqEWKss0n22KWMT8uTvxeUBINl'
access_token_secret = 'eLI9xbgGXQ26H8K0KXC7U6y2TFFqExeNXAd5XagSzHRuE'
       
api = Twython(consumer_key,consumer_secret,access_token,access_token_secret)

WoolList = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

""" call where the iss at api thanks to Bill Shupp"""
def getiss():
    response = urllib2.urlopen('https://api.wheretheiss.at/v1/satellites/25544')
    mydata = response.read()
    return mydata

""" longitude: convert our longitude to a minecraft co-ordinate"""
def do_coord(longitude):
    mine_long = longitude * -.55
    return mine_long


#if __name__ == "__main__":


mc = minecraft.Minecraft.create()
mc.postToChat(" Minecraft ISS Tracker for @naascoderdojo")
mc.player.setting("autojump", False)
mc.player.setPos(6, 20, 50)
time.sleep(10)
while True:

    try:
        BuildWorld.Build()
        time.sleep(5)
        iss = getiss()
        pos = json.loads(iss)
        lat = pos['latitude']
        lon = pos['longitude']
        mc.postToChat("MC ISS tracker Version 1.4.1 of @naascoderdojo's Minecraft ISS Tracker")
        mc.camera.setFollow()
        mc.postToChat("Credits to @damianmooney")
        mc.postToChat(' ISS Location Lat: %.2f Long: %.2f' % (lat,lon))
        new_long = do_coord(lon)
        mc.player.setPos(int(new_long), 20, int(lat))
        mc.setBlock(int(new_long), 20-1, int(lat),35,random.choice(WoolList))
        msg = 'ISS pos '+'@SpacePiJam'+' lon %d lat %d' % (new_long, lat)
                    #print msg
        mc.postToChat(msg)
                    #ory to location that you havesaved raspi2png in
                    
        a=subprocess.check_output('./raspi2png -d 3 -p "myscreenshot.png"',shell=True)
        photo = open('myscreenshot.png', 'rb')
        time.sleep(8)
        api.update_status_with_media(status=msg, media=photo)
    except:
        mc.postToChat("update issue")
        a=subprocess.check_output('./raspi2png -d 3 -p "myscreenshot.png"',shell=True)
        photo = open('myscreenshot.png', 'rb')
        api.update_status_with_media(status="update issue", media=photo)

    time.sleep(450) # --only update once every 15 minutes

