import socket
s = socket.socket()
host = "172.16.98.182"
port = 8080
s.connect((host, port))
print("connected")
filename = "dog"
file = open(filename, "rb")
while True:
    file_data = file.read(4096)
    s.send(file_data)
    if not file_data:
        break
file.close()
print("file sended")