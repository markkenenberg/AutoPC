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

friendName = "A D9u7c5"
userHashCode = "1571477844342770738"
localDir = "%USERPROFILE%/AppData/Local/ZaloPC/" + userHashCode + "/ZaloDownloads"
class SendFromPCUndoFromPC:
    #Define variables
    msgContent = "Test undo message"
    
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

    click(Resource.imgMenuUndo)
    wait(1)

    r.highlight(1)
    if r.exists(Resource.imgUndoContent):
        popup("FAILED: Message was not undo correctly" + 
                "\nExpect: Message content must be " + "Tin nhan da bi thu hoi")
    else:
        popup("SUCCESS: Message was undo!")

    wait(2)

class SendFromMobileUndoFromPC:
    #Define variables
    
    #Start or focus on Zalo (Zalo will be maximized)
    wait(1)
    MainClass.startZalo(appUnderTest, insDir)
    MainClass.switchToZalo(appUnderTest)

    iconSearch = find(Resource.imgSearch) #Find and click Search
    iconSearch.highlight(1)
    click(Resource.imgSearch)
    type(friendName + Key.ENTER) #Search name, press Enter to open Chat Window
    wait(0.5)

    popup(u"A login trên mobile và PC" +
            u"\nA gửi tin nhắn có nội dung sau từ mobile: Test undo message" +
            u"\nSau đó nhấn OK để tiếp tục.")

    r = MainClass.findInRangeAbove(Resource.imgTextboxChatFocused, 800) #Set range in Chat Window to find sent message
    r.highlight(1) #Highlight Chat Window
    
    #identify latest message based on ACK
    if r.exists(Resource.imgDaGui):
        rightClick(Resource.imgDaGui)
    elif r.exists(Resource.imgDaNhan):
        rightClick(Resource.imgDaNhan)
    elif r.exists(Resource.imgDaXem):
        rightClick(Resource.imgDaXem)

    click(Resource.imgMenuUndo)
    wait(1)

    r.highlight(1)
    if r.exists(Resource.imgUndoContent):
        popup("FAILED: Message was not undo correctly on PC." + 
                "\nExpect: Message content must be " + "Tin nhan da bi thu hoi")
    else:
        popup(u"SUCCESS: Tin nhắn đã được Undo ở PC. Kiểm tra trạng thái Undo trên Mobile!")
    wait(2)
class SendFromMobileUndoFromMobile:
    #Define variables
    
    #Start or focus on Zalo (Zalo will be maximized)
    wait(1)
    MainClass.startZalo(appUnderTest, insDir)
    MainClass.switchToZalo(appUnderTest)

    iconSearch = find(Resource.imgSearch) #Find and click Search
    iconSearch.highlight(1)
    click(Resource.imgSearch)
    type(friendName + Key.ENTER) #Search name, press Enter to open Chat Window
    wait(0.5)

    popup(u"1. A gửi tin nhắn có nội dung sau từ mobile: Test undo message" +
            u"\n2. Nhấn OK để tiếp tục.")
 
    r = MainClass.findInRangeAbove(Resource.imgTextboxChatFocused, 800) #Set range in Chat Window to find sent message
    r.highlight(1) #Highlight Chat Window

    if r.exists(Resource.imgUndoContent):
        popup(u"Tiếp theo: dùng mobile, undo tin nhắn vừa gửi"
                u"\nNhấn OK để tiếp tục.")
        wait(1)
        if r.exists(Resource.imgUndoMessage):
            popup(u"SUCCESS: Tin nhắn đã được undo")
        else:
            popup(u"FAILED: Lỗi undo tin nhắn!")
    else:
        popup("FAILED: Ca    wait(2) message on PC!")
        
    wait(2)        
    
class RemoveLocalPhotoWhenUndo:
    #Start or focus on Zalo (Zalo will be maximized)
    wait(1)
    MainClass.startZalo(appUnderTest, insDir)
    MainClass.switchToZalo(appUnderTest)

    iconSearch = find(Resource.imgSearch) #Find and click Search
    iconSearch.highlight(1)
    click(Resource.imgSearch)
    type(friendName + Key.ENTER) #Search name, press Enter to open Chat Window
    wait(0.5)

    popup(u"Case: Gửi tin photo từ mobile, thu hồi trên PC, kiểm tra xoá file local trên PC." +
            u"\n" +
            u"\nSteps:" +
            u"\nA login trên mobile và PC" +
            u"\nA gửi tin nhắn Photo từ mobile" +
            u"\nNhấn OK để tiếp tục.")

    r = MainClass.findInRangeAbove(Resource.imgTextboxChatFocused, 1200) #Set range in Chat Window to find sent message
    r.highlight(1) #Highlight Chat Window
    
    if r.exists(Resource.imgDaGui):
        rightClick(Resource.imgDaGui)
    elif r.exists(Resource.imgDaNhan):
        rightClick(Resource.imgDaNhan)
    elif r.exists(Resource.imgDaXem):
        rightClick(Resource.imgDaXem)

    click(Resource.imgMenuPhotoFolder)
    wait(1)
        
    popup(u"Chuẩn bị Thu hồi tin nhắn." +
            u"\nNhấn OK và quay lại Zalo để tiếp tục.")
    wait(1)
    MainClass.switchToZalo(appUnderTest)
    wait(1)

    if r.exists(Resource.imgDaGui):
        rightClick(Resource.imgDaGui)
    elif r.exists(Resource.imgDaNhan):
        rightClick(Resource.imgDaNhan)
    elif r.exists(Resource.imgDaXem):
        rightClick(Resource.imgDaXem)

    click(Resource.imgMenuUndo)
    wait(1)
    r.highlight(1)
    if r.exists(Resource.imgUndoMessage):
        popup(u"Tin nhắn đã được undo, kiểm tra file ảnh trên folder local đã mở trước đó."
               u"\nExpect: File ảnh đã được xoá.")
    else:
        popup(u"FAILED: Tin nhắn chưa được undo!")
    
    wait(2)

class RemoveLocalVoiceWhenUndo:
    #Start or focus on Zalo (Zalo will be maximized)
    wait(1)
    MainClass.startZalo(appUnderTest, insDir)
    MainClass.switchToZalo(appUnderTest)

    iconSearch = find(Resource.imgSearch) #Find and click Search
    iconSearch.highlight(1)
    click(Resource.imgSearch)
    type(friendName + Key.ENTER) #Search name, press Enter to open Chat Window
    wait(0.5)

    popup(u"Case: Gửi tin voice từ mobile, thu hồi trên PC, kiểm tra xoá file local trên PC." +
            u"\n" +
            u"\nSteps:" +
            u"\nA login trên mobile và PC" +
            u"\nA gửi tin nhắn Voice từ mobile" +
            u"\nNhấn OK để tiếp tục.")

    r = MainClass.findInRangeAbove(Resource.imgTextboxChatFocused, 1200) #Set range in Chat Window to find sent message
    r.highlight(1) #Highlight Chat Window

    type("e", Key.WIN)
    wait(1)
    type("d", Key.ALT)
    type(localDir + "/voice" + Key.ENTER)
    wait(1)

    popup(u"Chuẩn bị Thu hồi tin nhắn." +
            u"\nNhấn OK và quay lại Zalo để tiếp tục.")
    wait(1)
    MainClass.switchToZalo(appUnderTest)
    wait(1)

    if r.exists(Resource.imgDaGui):
        rightClick(Resource.imgDaGui)
    elif r.exists(Resource.imgDaNhan):
        rightClick(Resource.imgDaNhan)
    elif r.exists(Resource.imgDaXem):
        rightClick(Resource.imgDaXem)

    click(Resource.imgMenuUndo)
    wait(1)
    r.highlight(1)
    if r.exists(Resource.imgUndoMessage):
        popup(u"Tin nhắn đã được undo, kiểm tra file ảnh trên folder local đã mở trước đó."
               u"\nExpect: File voice đã được xoá.")
    else:
        popup(u"FAILED: Tin nhắn chưa được undo!")

    wait(2)
    
class RemoveLocalVideoWhenUndo:
    #Start or focus on Zalo (Zalo will be maximized)
    wait(1)
    MainClass.startZalo(appUnderTest, insDir)
    MainClass.switchToZalo(appUnderTest)

    iconSearch = find(Resource.imgSearch) #Find and click Search
    iconSearch.highlight(1)
    click(Resource.imgSearch)
    type(friendName + Key.ENTER) #Search name, press Enter to open Chat Window
    wait(0.5)

    popup(u"Case: Gửi tin video từ mobile, thu hồi trên PC, kiểm tra xoá file local trên PC." +
            u"\n" +
            u"\nSteps:" +
            u"\nA login trên mobile và PC" +
            u"\nA gửi tin nhắn Video từ mobile" +
            u"\nNhấn OK để tiếp tục.")

    r = MainClass.findInRangeAbove(Resource.imgTextboxChatFocused, 1200) #Set range in Chat Window to find sent message
    r.highlight(1) #Highlight Chat Window

    if r.exists(Resource.imgDaGui):
        rightClick(Resource.imgDaGui)
    elif r.exists(Resource.imgDaNhan):
        rightClick(Resource.imgDaNhan)
    elif r.exists(Resource.imgDaXem):
        rightClick(Resource.imgDaXem)

    click(Resource.imgMenuVideoFolder)
    wait(1)

    popup(u"Chuẩn bị Thu hồi tin nhắn." +
            u"\nNhấn OK và quay lại Zalo để tiếp tục.")
    wait(1)
    MainClass.switchToZalo(appUnderTest)
    wait(1)

    if r.exists(Resource.imgDaGui):
        rightClick(Resource.imgDaGui)
    elif r.exists(Resource.imgDaNhan):
        rightClick(Resource.imgDaNhan)
    elif r.exists(Resource.imgDaXem):
        rightClick(Resource.imgDaXem)

    click(Resource.imgMenuUndo)
    wait(1)
    r.highlight(1)
    if r.exists(Resource.imgUndoMessage):
        popup(u"Tin nhắn đã được undo, kiểm tra file ảnh trên folder local đã mở trước đó."
               u"\nExpect: File voice đã được xoá.")
    else:
        popup(u"FAILED: Tin nhắn chưa được undo!")

    wait(2)