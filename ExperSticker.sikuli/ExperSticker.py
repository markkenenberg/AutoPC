from sikuli import *
import Main
reload(Main)
import Resource
reload(Resource)
import Utils
reload(Utils)
import shutil

from Main import MainClass
from Utils import Utils

#Define Application Under Test
insDir = "C:\Program Files (x86)\Zalo\Zalo.exe"
appName = "Zalo"
userName = "Nam"
appUnderTest = App(appName + " - " + userName)

class TestSendSticker:
    #Start or focus on Zalo (Zalo will be maximized)
    wait(1)
    MainClass.startZalo(appUnderTest, insDir)
    MainClass.switchToZalo(appUnderTest)

    for x in range (1, 4):
        wait(0.5)
        click(Resource.imgSticker)
        wait(0.5)
        click(Resource.imgCuHanh) 
        wait(1)

        stickerToSend = str(x) + "_65.png"
        if exists(stickerToSend):
            click(stickerToSend) # sticker size trong cửa sổ chọn sticker = 65 nên phải resize ảnh lại nha mấy chế
        else:
            r = MainClass.findInRangeLeft(Resource.imgStickerScroll, 320)
            wheel(r, WHEEL_UP, 10) #scroll to top list first
            
            while not exists(stickerToSend):
                wheel(r, WHEEL_DOWN, 3)

            click(stickerToSend)
            
        r = MainClass.findInRangeAbove(Resource.imgTextboxChatFocused, 800).highlight(1) #Set range in Chat Window to find sent message
        stickerToFind = r.find(str(x) + ".png").highlight(1)
        Utils.saySth("Sticker " + str(x) + " matched!")
        wait(1)