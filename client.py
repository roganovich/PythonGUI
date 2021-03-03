import socket

SERVER_ADRESS = ('localhost', 55555)
client = socket.socket()
client.connect(SERVER_ADRESS)
client.send(bytes("Text", encoding="UTF-8"))
data = client.recv(4096)
print(data)