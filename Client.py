import socket as aSocket
import sys

def connectClient():

    try:
        rsClientSocket = aSocket.socket(aSocket.AF_INET, aSocket.SOCK_STREAM)
        print("[C]: Successfully created sockets")
    except aSocket.error as err:
        print("Socket open error: {0} \n".format(err))

    rsPort = 6000
    rsHostName = "facade.cs.rutgers.edu"
    #rsHostName = ""
    rsAddr = aSocket.gethostbyname(rsHostName)
    rsSocketConnection = (rsAddr, rsPort)

    rsClientSocket.connect(rsSocketConnection)

    hnsFile = sys.argv[1]

    with open(hnsFile, "r") as readFile:
        with open("RESOLVED.txt", "w") as writeFile:
            for hostName in readFile:
                # Stripping the new line at the end
                hostName = hostName.rstrip()
                # First contact to RS server
                rsClientSocket.send(hostName.encode('utf-8'))

                # Get resulting String from server
                serverResult = rsClientSocket.recv(1024).decode('utf-8')

                # Write result to file
                writeFile.write(serverResult + "\n")


    rsClientSocket.shutdown(aSocket.SHUT_RDWR)
    rsClientSocket.close()

connectClient()