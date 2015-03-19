from sikuli import *
import Main
reload(Main)
import Resource
reload(Resource)

from Main import MainClass

insDir = "C:\Program Files (x86)\Zalo\Zalo.exe"
appName = "Zalo"
userName = "Nam"
appUnderTest = App(appName + " - " + userName)

wait(2)

MainClass.startZalo(appUnderTest, insDir)
MainClass.switchToZalo(appUnderTest)


click(Resource.imgSearch)
type("Yves" + Key.ENTER)
type("This is a text" + Key.ENTER)
r = MainClass.findInRangeAbove(Resource.imgTextboxChatFocused, 400)
r.find("This is a text")


