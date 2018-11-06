import socket as aSocket

def connectClient():

    try:
        rsClientSocket = aSocket.socket(aSocket.AF_INET, aSocket.SOCK_STREAM)
        print("[C]: Successfully created sockets")
    except aSocket.error as err:
        print("Socket open error: {0} \n".format(err))

    """
    host = aSocket.gethostname()
    print("[C]: got host name: %s" %host)
    print("[C]: got host by name: %s" %aSocket.gethostbyname(host))
    print("[C]: got host by addr: ", aSocket.gethostbyaddr(host))
    """

    rsPort = 6000
    rsHostName = "facade.cs.rutgers.edu"
    rsAddr = aSocket.gethostbyname(rsHostName)
    rsSocketConnection = (rsAddr, rsPort)

    rsClientSocket.connect(rsSocketConnection)

    with open("PROJ2-HNS.txt", "r") as readFile:
        with open("RESOLVED.txt", "w") as writeFile:
            for hostName in readFile:
                # Stripping the new line at the end
                hostName = hostName.rstrip()
                print(hostName)
                # First contact to RS server
                rsClientSocket.send(hostName.encode('utf-8'))

                # Get resulting String from server
                serverResult = rsClientSocket.recv(1024).decode('utf-8')
                print(serverResult)
                # Write result to file
                writeFile.write(serverResult + "\n")


    rsClientSocket.shutdown(aSocket.SHUT_RDWR)
    rsClientSocket.close()


connectClient()