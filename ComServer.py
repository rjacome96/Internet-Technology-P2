import socket as aSocket
import time

def ComServer():

    try:
        rootServerSocket = aSocket.socket(aSocket.AF_INET, aSocket.SOCK_STREAM)
        print("[COM]: Successfully created sockets")
    except aSocket.error as err:
        print("Socket open error: {0} \n".format(err))
        
    com_Dict = {}
        
    with open("PROJ2-DNSCOM.txt", "r") as dnsTableFile:
        for fieldLine in dnsTableFile:
            dictKey = fieldLine.rstrip()
            recordString = dictKey.rsplit()
            hostName = recordString[0]
            ipAddress = recordString[1]
            flag = recordString[2].rstrip()
			
            com_Dict[hostName] = (ipAddress, flag)

    port = 7000
    serverBinding = ('', port)
    rootServerSocket.bind(serverBinding)
    print("[COM]: Socket is binded to port: ", port)

    rootServerSocket.listen(1)
    print("[COM]: Listening for one connection on port 5000...")

    rootConnection = rootServerSocket.accept()
    
    rootSocket = rootConnection[0]
    
    while True:
        serverInfo = rootSocket.recv(1024).decode('utf-8')
		
        if not serverInfo: 
            break
		
        dataToServer = None
		
        if serverInfo in com_Dict:
            print("[COM]: Host Found")
            flag = com_Dict[serverInfo][1]
            ipAddress = com_Dict[serverInfo][0]
            dataToServer = serverInfo + " " + ipAddress + " " + flag
        else:
            print("[COM]: Host Not Found. Error")
            dataToServer = serverInfo + " - Error:Host not Found"
		
        rootSocket.send(dataToServer.encode('utf-8'))

    time.sleep(15)

    rootServerSocket.close()


ComServer()
