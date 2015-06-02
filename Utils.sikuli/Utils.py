from sikuli import *
import time

class Utils:

    def printTextOnScreen():
        print selectRegion().text()

    @classmethod
    def getFromClipboard(self):
        textClipboard = Env.getClipboard().strip()
        return textClipboard

    @classmethod
    def getCurrDatetime(self):
        now = time.localtime()
        displayTime = ("%2d:%02d" % (now.tm_hour, now.tm_min))
        return displayTime

    @classmethod
    def startChrome(self):
        insDir = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        openApp(insDir)

    @classmethod
    def saySth(self, textToSay):
        type("JARVIS: " + textToSay + Key.ENTER)

    @classmethod
    def logPassed(self):
        intPassed
        intPassed += 1
        return intPassed

    @classmethod
    def logFailed(self):
        intFailed
        intFailed += 1
        return intFailed