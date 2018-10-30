import socket as aSocket
import time

def ComServer():

    try:
        rootServerSocket = aSocket.socket(aSocket.AF_INET, aSocket.SOCK_STREAM)
        print("[COM]: Successfully created sockets")
    except aSocket.error as err:
        print("Socket open error: {0} \n".format(err))

    comServerDict = {}
    with open("PROJ2-DNSCOM.txt", "r") as dnsCOMfile:
        for fieldLine in dnsCOMfile:
            dictKey = fieldLine.rstrip()
            recordString = dictKey.rsplit()
            hostname = recordString[0]
            ipAddress = recordString[1]
            flag = recordString[2].rstrip()
            comServerDict[hostname] = (ipAddress, flag)
    port = 7000
    serverBinding = ('', port)
    rootServerSocket.bind(serverBinding)
    print("[COM]: Socket is binded to port: ", port)

    rootServerSocket.listen(1)
    print("[COM]: Listening for one connection on port 7000...")
    rootConnection = rootServerSocket.accept()

    rootSocket = rootConnection[0]
    
    while True:
        rootServerInfo = rootSocket.recv(1024).decode('utf-8')
        
        print("[COM]: Received from root server: ", rootServerInfo)
        
        rootSocket.send("Result from Server: ".encode('utf-8'))
        
        break

    # Debug statement to be deleted
    print(rootSocket)

    time.sleep(15)

    rootServerSocket.close()


ComServer()