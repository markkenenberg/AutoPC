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

class testSendMessageP2P:
    #Define variables
    friendName = "Alehaptap"
    msgContent = "this is a text"
    
    #Start or focus on Zalo (Zalo will be maximized)
    wait(1)
    MainClass.startZalo(appUnderTest, insDir)
    MainClass.switchToZalo(appUnderTest)
    
    iconSearch = find(Resource.imgSearch) #Find and click Search
    iconSearch.highlight(1)
    click(Resource.imgSearch)
    type(friendName + Key.ENTER) #Search name, press Enter to open Chat Window
    type(msgContent + Key.ENTER) #Send message
    
    r = MainClass.findInRangeAbove(Resource.imgTextboxChatFocused, 800) #Set range in Chat Window to find sent message
    r.highlight(1) #Highlight Chat Window
    
    #identify latest message based on ACK
    if r.exists(Resource.imgDaGui):
        rightClick(Resource.imgDaGui)
    elif r.exists(Resource.imgDaNhan):
        rightClick(Resource.imgDaNhan)
    elif r.exists(Resource.imgDaXem):
        rightClick(Resource.imgDaXem)
    
    click(Resource.imgSaoChep)
    
    msgfromClipboard = Utils.getFromClipboard()
    if msgfromClipboard == msgContent:
        popup("PASS: Message sent and displayed correctly!")
    else:
        popup("FAIL: Message sent but did not display correctly!")
    
class testSendPhoto:
    #Define variables
    friendName = "Alehaptap"
    
    #Start or focus on Zalo (Zalo will be maximized)
    wait(1)
    MainClass.startZalo(appUnderTest, insDir)
    MainClass.switchToZalo(appUnderTest)
    
    iconSearch = find(Resource.imgSearch) #Find and click Search
    iconSearch.highlight(1)
    click(Resource.imgSearch)
    type(friendName + Key.ENTER) #Search name, press Enter to open Chat Window

    if exists(Resource.imgAttachPhoto):
        click(Resource.imgAttachPhoto)
        wait(1)
        type("d", Key.ALT) #Hotkey to focus directory textbox
        wait(0.5)
        type("C:\Program Files (x86)\Windows Media Player\Media Renderer" + Key.ENTER)
        wait(1)
        type("n", Key.ALT) #Hotkey to focus filename textbox
        type("DMR_120.jpg" + Key.ENTER)
    else:
        popup("ERROR: Can not find Photo Attachment Icon")