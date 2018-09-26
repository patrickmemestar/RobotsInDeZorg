#!/usr/bin/env python3

#importing used files
from procesManager import *
from webSocket import *

#define global constants
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20

#initialise needed components
procesManager = procesManager()
webSocket = webSocket()

#define local functions
def testProcesManager():
	procesManager.showPicture("myphoto.jpg", 5)
	procesManager.killSlideShow()

#do it
testProcesManager()

