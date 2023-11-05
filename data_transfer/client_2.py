import socket
sock = socket.socket()
host = "172.16.98.182"
port = 8080
sock.connect((host, port))
print("connected")

sock.send('hello, Raspberry!')

filename = "dog"
file = open(filename, "rb")

file_data = file.read(4096)
sock.send(file_data)
if not file_data:
    print("file is empty")

file.close()
print("file sended")