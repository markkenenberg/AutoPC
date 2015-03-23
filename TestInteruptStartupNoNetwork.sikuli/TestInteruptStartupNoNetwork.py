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
userName = "Yves"
appUnderTest = App(appName + " - " + userName)

class TestInteruptStartupNoNetwork:
    #On Windows 8

    #if network is turn off -> turn on to test
    if exists(Resource.imgNoNetwork):
        click(Resource.imgNoNetwork)
        wait(1)
        wifiSection = MainClass.findInRangeBelow(Resource.imgWifiSection, 80)
        wait(1)
        switchOFF = wifiSection.find(Resource.imgSwitchOFF)
        click(switchOFF)
        wait(3)
        type(Key.ESC)#clos the setting panel

    #kill Zalo if running
    wait(1)
    MainClass.terminateZalo(appUnderTest)
    wait(2)

    #start testing now: launch Zalo
    MainClass.startZalo(appUnderTest, insDir)

    click(Resource.imgNetwork) #click network icon
    wifiSection = MainClass.findInRangeBelow(Resource.imgWifiSection, 80)
    wait(1)
    switch = wifiSection.find(Resource.imgSwitchON) #find the wifi switch
    click(switch) #click on switch to turn off network while Zalo is launching
    wait(2)
    type(Key.ESC) #close the setting panel

    