import socket
import re

host = '' 
port = 3600
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1) 

while True:
    csock, caddr = sock.accept()
    print "Connection from: " + `caddr`
    req = csock.recv(1024) 
    
    print req

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
