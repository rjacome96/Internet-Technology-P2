import socket as aSocket
import time

def EduServer():
    try:
        rootServerSocket = aSocket.socket(aSocket.AF_INET, aSocket.SOCK_STREAM)
        print("[EDU]: Successfully created sockets")
    except aSocket.error as err:
        print("Socket open error: {0} \n".format(err))

    # Create Dictionary data structure as DNS table
    edu_Dict = {}
    # Read lines from file
    with open("PROJ2-DNSEDU.txt", "r") as dnsTableFile:
        # Populate Dict data structure with hostname as key
        # And IP address and flags as values

        # Bool variable to help identify server name

        for fieldLine in dnsTableFile:
            dictKey = fieldLine.rstrip()
            recordString = dictKey.rsplit()

            # From a given line in file, store host name, IP address, and flag respectively
            hostName = recordString[0]
            ipAddress = recordString[1]
            flag = recordString[2].rstrip()

            # Key is host name, value is a tuple of IP address and flag
            edu_Dict[hostName] = (ipAddress, flag)

    port = 6500
    serverBinding = ('', port)
    rootServerSocket.bind(serverBinding)
    print("[EDU]: Socket is binded to port: ", port)

    rootServerSocket.listen(1)
    print("[EDU]: Listening for one connection on port 5000...")

    rootConnection = rootServerSocket.accept()

    rootSocket = rootConnection[0]
    
    while True:
        serverInfo = rootSocket.recv(1024).decode('utf-8')
		
        if not serverInfo: 
            break
		
        dataToServer = None
		
        if serverInfo in edu_Dict:
            print("[EDU]: Host Found")
            flag = edu_Dict[serverInfo][1]
            ipAddress = edu_Dict[serverInfo][0]
            dataToServer = serverInfo + " " + ipAddress + " " + flag
        else:
            print("[COM]: Host Not Found. Error")
            dataToServer = serverInfo + " - Error:Host not Found"
		
        rootSocket.send(dataToServer.encode('utf-8'))

    # Debug statement to be deleted
    #print(rootSocket)

    time.sleep(15)

    rootServerSocket.close()


EduServer()
