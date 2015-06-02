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



class RemoveLocalFileWhenUndo:
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
          u"\nKiểm tra file có được xoá khi tin nhắn bị Thu hồi hay không.")

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
    if r.exists(Resource.imgUndoContent):
        popup(u"FAILED: Tin nhắn chưa được undo!")
    else:
        popup(u"Tin nhắn đã được undo, kiểm tra file ảnh trên folder local đã mở trước đó."
               u"\nExpect: File ảnh đã được xoá.")