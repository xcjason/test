import socket

HOST, PORT = '', 8888
listenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listenSocket.bind((HOST, PORT))
listenSocket.listen(1)
print 'Serving HTTP on port %s ...' % PORT
while True:
	clientConnection, clientAddr = listenSocket.accept()
	request = clientConnection.recv(1024)
	print request
	httpResp = """
	HTTP/1.1 200 OK

	Hello App!
	"""
	clientConnection.sendall(httpResp)
	clientConnection.close()