import socket

class webSocketServer:

    #Global fields 
    maxConnections = 1

    #constructor defines class properties (duh)
    def __init__(self,ip,port,bufferSize):
        self.ip = ip
        self.port = port
        self.bufferSize = bufferSize
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #binds socket to a port and IP, and listens for a connection, accepts this connection.
    def openConnection():
        
        socket.bind((ip, port))
        socket.listen(maxConnections)
        connection, addr = s.accept()

        if not connection:
            return False
        if not addr:
            return False

        print 'Connection address:', addr
        return True

    #returns incomming data from connection after empty check
    def recieveData():
        data = connection.recv(bufferSize)
        if not data:
            print "no data recieved"
            return False
        return data

    #sends data through connection after empty check
    def sendData(data):
        if not data:
            return False
        connection.send(data)
        return True

    #marks the socket closed
    def closeConnection():
        if not connection:
            return False
        socket.close()
        return True
