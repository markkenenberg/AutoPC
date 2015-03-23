from sikuli import *

#insDir = "C:\Program Files (x86)\Zalo\Zalo.exe"
#appName = "Zalo"
#userName = "Nam"
#appUnderTest = App(appName + " - " + userName)

class MainClass:
    @classmethod
    def startZalo(self, appUnderTest, insDir):
        if not appUnderTest.window():
            appUnderTest.open(insDir)
            
    @classmethod
    def switchToZalo(self, appUnderTest):
        #appUnderTest.focus()
        switchApp(appUnderTest)
        wait(1)
        type(" ", KEY_ALT); type("x") #work-around with minimized application
        
    @classmethod
    def terminateZalo(self, appUnderTest):
        closeApp(appUnderTest)

    @classmethod
    def clickOffset(self, image, x, y):
        t = Pattern(image).targetOffset(x, y)
        click(t)

    @classmethod
    def clickImage(self, image):
        click(image)

    @classmethod
    def returnImageCount(self, region, image):
        count = 0
        for i in region.findAll(image):
            count += 1
        return count

    @classmethod 
    def findInRangeAbove(self, imgOrigin, pixel):
        r = find(imgOrigin).above(pixel)
        return r

    @classmethod
    def findInRangeBelow(self, imgOrigin, pixel):
        r = find(imgOrigin).below(pixel)
        return r

    @classmethod
    def highlightRegion(self, imgOrigin, second):
        r = find(imgOrigin)
        r.highlight(second)

    @classmethod
    def blinkingRegion(self, region, second, count):
        for x in range (0, count):
            region.highlight(second)