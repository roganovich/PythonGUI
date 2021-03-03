import socket

SERVER_ADRESS = ('localhost', 55555)
server = socket.socket()
server.bind(SERVER_ADRESS)
server.listen(1)
print("Wait")
while True:
    connection, socet = server.accept()
    data = connection.recv(4096)
    print("Get: ", data )
    data = data.upper()
    connection.send(data)
    connection.close()