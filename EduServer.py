import socket as aSocket
import time

def EduServer():
    try:
        rootServerSocket = aSocket.socket(aSocket.AF_INET, aSocket.SOCK_STREAM)
        print("[EDU]: Successfully created sockets")
    except aSocket.error as err:
        print("Socket open error: {0} \n".format(err))

    # Create Dictionary data structure as DNS table
    comServerDict = {}
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
            comServerDict[hostName] = (ipAddress, flag)

    port = 6500
    serverBinding = ('', port)
    rootServerSocket.bind(serverBinding)

    rootServerSocket.listen(1)

    rootConnection = rootServerSocket.accept()

    rootSocket = rootConnection[0]

    # Debug statement to be deleted
    print(rootSocket)

    time.sleep(15)

    rootServerSocket.close()


EduServer()