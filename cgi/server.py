import socket
import re

import sys

from engine import Engine

port = 0
if len(sys.argv) == 1:
	port = 3600
else:
	port = int(sys.argv[1])
print "Server starting on port " + str(port)

host = '' 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1) 

engine = Engine()

while True:
    csock, caddr = sock.accept()
    print "Connection from: " + `caddr`
    req = csock.recv(1024) 
    
    lines = req.split('\n')
    
    message = ""
    arrived = False
    for line in lines:
    	if line == "\r":
    		arrived = True
    	line += '\n' 
    	if arrived:
    		message += line

    engine.process_message(message) 

    csock.sendall("""HTTP/1.0 200 OK
		Content-Type: text/html
		<html>
			<head>
				<title>Success</title>
			</head>
			<body>
				Success
			</body>
		</html>
	""")
