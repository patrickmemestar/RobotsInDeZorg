import subprocess
from time import sleep

class procesManager:

    #constructor defines class properties
    def __init__(self):
        self.image = None
        self.slideShow = None

    #displays specific file "name" for "time" seconds
    def showPicture(self, name, time):
        image = subprocess.Popen(["eog", name])
        #image = subprocess.Popen(["fbi", "-a", name])

        sleep(time)

        image.kill()

    #starts slideShow of photos in specific directory
    def showSlideShow(self,interval, path):
        slideShow = subprocess.Popen(["fbi", "-a", path + "/*.jpg"])

    #stops slideShow
    def killSlideShow(self):
        if self.slideShow is not None:
            slideShow.kill()
        else:
            print("there is no slideshow to kill")