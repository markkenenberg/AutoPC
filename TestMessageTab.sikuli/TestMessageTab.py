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

class TestDeleteConversation:
    #Start or focus on Zalo (Zalo will be maximized)
    wait(1)
    MainClass.startZalo(appUnderTest, insDir)
    MainClass.switchToZalo(appUnderTest)

    friendName = "Alehaptap"
    msgContent = "Test cai nha"

    #Send a message to create first Thread Chat
    iconSearch = find(Resource.imgSearch) #Find and click Search
    iconSearch.highlight(1)
    click(Resource.imgSearch)
    type(friendName + Key.ENTER) #Search name, press Enter to open Chat Window
    wait(0.5)
    type(msgContent + Key.ENTER) #Send message

    firstThread = MainClass.findInRangeBelow(Resource.imgTabDock, 72) #Conversation height: 72px
    firstThread.highlight(1)

    imgFirstThread = capture(firstThread) #Capture image to check existence after delete

    rightClick(firstThread)
    wait(0.5)
    click(Resource.imgXoaHoiThoai)
    wait(1)
    click(Resource.imgConfirmNo)
    wait(1)
    if not firstThread.exists(imgFirstThread):
        popup("FAIL: Thread chat disappear?!")
    else:
        popup("PASS: Thread chat remained.")

    rightClick(firstThread)
    wait(0.5)
    click(Resource.imgXoaHoiThoai)
    wait(1)
    click(Resource.imgConfirmYes)
    wait(1)
    if firstThread.exists(imgFirstThread):
        popup("FAIL: Thread chat not deleted")
    else:
        popup("PASS: Thread chat is removed from conversation list.")


class TestFocusAndSwitchTab:
    #Start or focus on Zalo (Zalo will be maximized)
    wait(1)
    MainClass.startZalo(appUnderTest, insDir)
    MainClass.switchToZalo(appUnderTest)

    #Click message tab and verify
    rMessage = find(Resource.imgMessageTab)
    rMessage.highlight(1)
    click(Resource.imgMessageTab)

    headerSearch = Resource.imgHeaderSearchBar
    r2 = MainClass.findInRangeBelow(headerSearch, 100)
    r2.highlight(1)
    wait(1)
    if not r2.exists(Resource.imgSubContactTab):
        popup("PASS: this is message tab.")
    else:
        popup("FAIL: this is Danh Ba tab.")

    #Click Contact tab and verify
    rContact = find(Resource.imgContactTab)
    rContact.highlight(1)
    click(Resource.imgContactTab)
    r2.highlight(1)
    wait(1)
    if r2.exists(Resource.imgSubContactTab):
        popup("PASS: found Ban Be and Danh Sach Nhom, this is contact tab.")
    else:
        popup("FAIL: can not find header bar of contact tab (Ban be and Nhom).")