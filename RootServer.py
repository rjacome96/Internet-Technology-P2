import socket as aSocket
import time

def RootServer():

    # Attempt to create three sockets for server
    try:
        comSocketServer = aSocket.socket(aSocket.AF_INET, aSocket.SOCK_STREAM)
        eduSocketServer = aSocket.socket(aSocket.AF_INET, aSocket.SOCK_STREAM)
        clientSocketServer = aSocket.socket(aSocket.AF_INET, aSocket.SOCK_STREAM)
        print("[RS]: Successfully created socket")
    except aSocket.error as err:
        print("Socket open error: {0} \n".format(err))

    # We will find the servers' host name when we come across 'NS' in the file
    comServerHostName = None
    eduServerHostName = None
    # Create Dictionary data structure as DNS table
    rootServerDict = {}
    # Read lines from file
    with open("PROJ2-DNSRS.txt", "r") as dnsTableFile:
        # Populate Dict data structure with hostname as key
        # And IP address and flags as values

        for fieldLine in dnsTableFile:
            dictKey = fieldLine.rstrip()
            recordString = dictKey.rsplit()

            # From a given line in file, store host name, IP address, and flag respectively
            hostName = recordString[0]
            ipAddress = recordString[1]
            flag = recordString[2].rstrip()

            # Found a server field
            if flag == "NS":
                
                typeServer = hostName[-3:] # Takes substring of host name (edu or com)

                if typeServer == "edu":
                    eduServerHostName = ipAddress # Project PDF shows that the IP field will contain the hostname
                elif typeServer == "com":
                    comServerHostName = ipAddress # Might need to be edited as well because of reason stated above

            # Key is host name, value is a tuple of IP address and flag
            rootServerDict[hostName] = (ipAddress, flag)

    # Pick port and bind it to this machine's IP address for Client
    port = 6000
    serverBinding = ('', port)
    clientSocketServer.bind(serverBinding)
    print("[RS]: Socket is binded to port: ", port)

    # Connect to .edu server
    eduServerPort = 6500
    eduServerAddr = aSocket.gethostbyname(eduServerHostName)
    eduServerConnection = (eduServerAddr, eduServerPort)
    #eduServerConnection = ('', eduServerPort)
    eduSocketServer.connect(eduServerConnection)

    # Connect to .com server
    comServerPort = 7000
    comServerAddr = aSocket.gethostbyname(comServerHostName)
    comServerConnection = (comServerAddr, comServerPort)
    #comServerConnection = ('', comServerPort)
    comSocketServer.connect(comServerConnection)

    
    # Have socket listen on the port 6000
    clientSocketServer.listen(1)
    print("[RS]: Listening for one connection on port 6000...")
    clientConnection = clientSocketServer.accept()

    clientSocket = clientConnection[0]

    # Once connected, service the client until the end
    while True:

        clientInfo = clientSocket.recv(1024).decode('utf-8')

        print("[RS]: Recieved from client: ", clientInfo)
        
        if not clientInfo:
            break
		
        dataToClient = None
        #dataToEDU = None
        #dataToCOM = None
        typeServer = clientInfo[-3:]
		
        print("[RS]: Type of server is: {}".format(typeServer))

        if clientInfo in rootServerDict:
            print("[RS]: Host Found")
            flag = rootServerDict[clientInfo][1]
            ipAddress = rootServerDict[clientInfo][0]
            dataToClient = clientInfo + " " + ipAddress + " " + flag
            #print("[RS]: Sending hostname to client: Root", dataToClient)
            #clientSocket.send(dataToClient.encode('utf-8'))
        elif typeServer == "edu":
            print("[RS]: Host not found. Redirect to EDU")
            #flag = "NS"
            #dataToEDU = eduServerHostName + " - " + flag
            eduSocketServer.send(clientInfo.encode('utf-8'))
            dataToClient = eduSocketServer.recv(1024).decode('utf-8')
            #print("[RS]: Sending hostname to client: EDU", dataToClient)
            #clientSocket.send(dataToClient.encode('utf-8'))
        elif typeServer == "com":
            print("[RS]: Host not found. Redirect to COM")
            #flag = "NS"
            #dataToCOM = comServerHostName + " - " + flag
            comSocketServer.send(clientInfo.encode('utf-8'))
            dataToClient = comSocketServer.recv(1024).decode('utf-8')
            #print("[RS]: Sending hostname to client, COM: ", dataToClient)
            #clientSocket.send(dataToClient.encode('utf-8'))
        else:
            print("[RS]: Host type is not familiar to us. Error!")
            dataToClient = clientInfo + " - Error:Host not Found"
		
        print("[RS]: Sending hostname to client: ", dataToClient)
        clientSocket.send(dataToClient.encode('utf-8'))
    
    comSocketServer.shutdown(aSocket.SHUT_RDWR)
    eduSocketServer.shutdown(aSocket.SHUT_RDWR)
    comSocketServer.close()
    eduSocketServer.close()
    time.sleep(5)
    clientSocketServer.close()

RootServer()
