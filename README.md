# Internet-Technology-P2
Create a recursive DNS between a root server, two specialized servers, and a client.

Project 2

Novemeber 12, 2018

Professor Badri Nath

Roy Jacome & Kishan Patel

Python version used across all programs: Python 3

Ilabs/Machines used: ComServer.py is running on grep.cs.rutgers.edu, EduServer.py is running on kill.cs.rtugers.edu, RootServer.py is running on facade.cs.rutgers.edu, Client.py can be run on any machine.

NOTE: facade.cs.rutgers.edu is hardcoded as the root server that client will connect to. However, servers grep.cs.rtugers.edu and kill.cs.rutgers.edu are used by us for testing and are fed through "PROJ2-DNSRS.txt". In other words, Root server can connect to whatever servers are used for COM and EDU so long as they are labeled respectively and the given IP addresses are appropiately listed as NS servers in its DNS text file.

How to run our project: First run EduServer.py, then, ComServer.py, then RootServer.py and finally Client.py.

All programs assume that 4 test files will be within the same directory as the programs specifically called "PROJ2-DNSEDU.txt", "PROJ2-DNSCOM.txt", "PROJ2-DNSRS.txt", and "PROJ2-HNS.txt" that EduServer.py, ComServer.py, RootServer.py and Client.py will read in respectively to fill up their DNS tables.

Client will send each line in the "PROJ2-HNS.txt" to the Root server and awaits for a response. Root server then looks up the client's request, returns IP if it is in its DNS table or sends it to either Edu or Com server if the ending of the request matches the server type. If no match is found, an error message is returned, else the host name with the appropiate IP address is returned to the client and client prints the result to a file named "RESOLVED.txt".