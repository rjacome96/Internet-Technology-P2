import socket as aSocket
import time

def ComServer():

    try:
        rootServerSocket = aSocket.socket(aSocket.AF_INET, aSocket.SOCK_STREAM)
        print("[COM]: Successfully created sockets")
    except aSocket.error as err:
        print("Socket open error: {0} \n".format(err))


    port = 7000
    serverBinding = ('', port)
    rootServerSocket.bind(serverBinding)

    rootServerSocket.listen(1)

    rootConnection = rootServerSocket.accept()

    rootSocket = rootConnection[0]

    # Debug statement to be deleted
    print(rootSocket)

    time.sleep(15)

    rootServerSocket.close()


ComServer()