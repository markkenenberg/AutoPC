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



class DeleteGroup:
    wait(1)
    click(Resource.imgInviteMore)

    #member list is now open
    listMember = MainClass.findInRangeBelow(Resource.imgSubContactTab, 655).highlight(1)

    while listMember.exists(Resource.imgCheckBoxList):
        isChecked = find(Resource.imgCheckBoxList)
        click(isChecked)
        
    wait(1)
    removeMe = find(Resource.imgSelfLeaveGroup)
    click(removeMe)
    wait(1)
    click(Resource.imgButtonDone)