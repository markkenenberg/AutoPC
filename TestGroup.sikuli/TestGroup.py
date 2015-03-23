from sikuli import *
import Main
reload(Main)
import Resource
reload(Resource)
import Utils
reload(Utils)

from Main import MainClass
from Utils import Utils

#Define Application Under Test
insDir = "C:\Program Files (x86)\Zalo\Zalo.exe"
appName = "Zalo"
userName = "Nam"
appUnderTest = App(appName + " - " + userName)

class RenameGroup:
    #Define variables
    groupNameToChange = "Group Test Nha"
    msgContent = "Start at " + Utils.getCurrDatetime()

    #Start or focus on Zalo (Zalo will be maximized)
    wait(1)
    MainClass.startZalo(appUnderTest, insDir)
    MainClass.switchToZalo(appUnderTest)

    #focus tab Danh ba
    click(Resource.imgContactTab)

    #focus Group List
    MainClass.highlightRegion(Resource.imgGroupList, 1)
    click(Resource.imgGroupList)

    #focus first group item
    firstGroup = MainClass.findInRangeBelow(Resource.imgGroupListTitle, 58)
    MainClass.blinkingRegion(firstGroup, 1, 2)
    click(firstGroup)

    #Right-click on first group item -> choose Doi Ten Nhom
    rightClick(firstGroup)
    wait(1)
    click(Resource.imgDoiTenNhom)

    type("a", Key.CTRL)
    type(groupNameToChange + Key.ENTER)
    wait(1)

    #now try to copy the actual group name...
    rightClick(firstGroup)
    wait(1)
    click(Resource.imgDoiTenNhom)

    type("a", Key.CTRL)
    type("c", Key.CTRL)
    wait(1)

    #...and compare actual group name with expected group name.
    txtFromClipBoard = Utils.getFromClipboard()
    if txtFromClipBoard==groupNameToChange:
        popup("SUCCESS: group name matched!" + 
                "\nExpect name: " + groupNameToChange +
                "\nActual name: " + txtFromClipBoard)
    else:
        popup("FAILED: group name NOT matched!" + 
                "\nExpect name: " + groupNameToChange +
                "\nActual name: " + txtFromClipBoard)

class CreateGroup:
    #Define variables
    groupNameToChange = "Group Create Nha"
    msgContent = "Start at " + Utils.getCurrDatetime()
    intAddGroupMember = 5

    #Start or focus on Zalo (Zalo will be maximized)
    wait(1)
    MainClass.startZalo(appUnderTest, insDir)
    MainClass.switchToZalo(appUnderTest)
    
    MainClass.highlightRegion(Resource.imgMessageTab, 1)
    click(Resource.imgMessageTab)
    wait(1)
    click(Resource.imgTaoTroChuyen)
    for x in range (0, intAddGroupMember):
        type(Key.DOWN + Key.SPACE)
        wait(0.5)

    type(Key.TAB)
    wait(0.5)
    type("a", Key.CTRL)
    wait(0.5)
    type(groupNameToChange + Key.ENTER)
    wait(0.5)
    type(Key.ENTER)