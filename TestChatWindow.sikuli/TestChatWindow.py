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
    msgContent = "Start at " + Utils.getCurrDatetime()
    
    #Start or focus on Zalo (Zalo will be maximized)
    wait(1)
    MainClass.startZalo(appUnderTest, insDir)
    MainClass.switchToZalo(appUnderTest)

    iconSearch = find(Resource.imgSearch) #Find and click Search
    iconSearch.highlight(1)
    click(Resource.imgSearch)
    type(friendName + Key.ENTER) #Search name, press Enter to open Chat Window
    wait(0.5)
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
    
    click(Resource.imgSaoChep) #copy message content to clipboard
    
    msgfromClipboard = Utils.getFromClipboard()
    if msgfromClipboard == msgContent:
        popup("SUCCESS: Message sent and displayed correctly!" + 
                "\nExpect text: " + msgContent +
                "\nActual text: " + msgfromClipboard)
    else:
        popup("ERROR: Message sent but did not display correctly!" + 
                "\nExpect text: " + msgContent +
                "\nActual text: " + msgfromClipboard)
    
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
    Utils.saySth("Start send photo @" + Utils.getCurrDatetime())

    if exists(Resource.imgAttachPhoto):
        imgAttachPhoto = find(Resource.imgAttachPhoto)
        imgAttachPhoto.highlight(1)
        click(Resource.imgAttachPhoto)
        wait(1)
        type("d", Key.ALT) #Hotkey to focus directory textbox
        wait(0.5)
        type("C:\Program Files (x86)\Windows Media Player\Media Renderer" + Key.ENTER)
        wait(1)
        type("n", Key.ALT) #Hotkey to focus filename textbox
        type("DMR_120.jpg" + Key.ENTER)
        Utils.saySth("Photo was sent succesfully!")
    else:
        Utils.saySth("Error: Can't find attachment icon, or something else happened...")

class TestSendFile:
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
    Utils.saySth("Start send file @" + Utils.getCurrDatetime())

    if exists(Resource.imgAttachFile):
        imgAttachFile = find(Resource.imgAttachFile)
        imgAttachFile.highlight(1)
        click(Resource.imgAttachFile)
        wait(1)
        type("d", Key.ALT) #Hotkey to focus directory textbox
        wait(0.5)
        type("C:\Program Files (x86)\Windows Media Player\Media Renderer" + Key.ENTER)
        wait(1)
        type("n", Key.ALT) #Hotkey to focus filename textbox
        type("RenderingControl.xml" + Key.ENTER)
        Utils.saySth("File was sent succesfully!")
    else:
        Utils.saySth("Error: Can't find attachment icon, or something else happened...")

class testSendSticker:
    #Define variables
    friendName = "Alehaptap"
    msgContent = "Start sticker test @" + Utils.getCurrDatetime()
    
    #Start or focus on Zalo (Zalo will be maximized)
    wait(1)
    MainClass.startZalo(appUnderTest, insDir)
    MainClass.switchToZalo(appUnderTest)

    iconSearch = find(Resource.imgSearch) #Find and click Search
    iconSearch.highlight(1)
    click(Resource.imgSearch)
    type(friendName + Key.ENTER) #Search name, press Enter to open Chat Window
    wait(0.5)
    type(msgContent + Key.ENTER) #Send message

    iconSticker = find(Resource.imgSticker)
    iconSticker.highlight(1)
    click(Resource.imgSticker)
    wait(0.5)
    click(Resource.imgDefaultSticker)
    wait(0.5)
    click(Resource.imgCuHanh1)
    Utils.saySth("Sticker sent succesfully.")