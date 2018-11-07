# Internet-Technology-P2
Create a recursive DNS between a root server, two specialized servers, and a client.

Project 2

Novemeber 12, 2018

Professor Badri Nath

Roy Jacome & Kishan Patel

Python version used across all programs: Python 3

Ilabs/Machines used: ComServer.py is running on grep.cs.rutgers.edu, EduServer.py is running on kill.cs.rtugers.edu, RootServer.py is running on facade.cs.rutgers.edu, Client.py can be run on any machine.

NOTE: As per the announcement, All programs will be expecting input. Specifically: COM and EDU server will always expect to be given their respecitve DNS text files. Root server expects to be given the names of the COM and EDU server (in that order) and then finally its DNS text file. Client expects to be first given the name of the Root server and then the file of host names to give to Root server to look up.

How to run our project: First run EduServer.py with EDU's DNS text file, then run ComServer.py with COM's DNS text file, then run RootServer.py with COM's, EDU's host names and then its DNS text file (in that order), and finally Client.py with the name that the Root server is running on and then the HNS text file.

Client will send each line in the "PROJ2-HNS.txt" to the Root server and awaits for a response. Root server then looks up the client's request, returns IP if it is in its DNS table or sends it to either EDU or COM server if the ending of the request matches the server type. If no match is found, an error message is returned, else the host name with the appropiate IP address is returned to the root and then sent to the client and client prints the result to a file named "RESOLVED.txt".