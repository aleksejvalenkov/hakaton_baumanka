import socket
s = socket.socket()
host = "172.16.98.38"
port = 8080
s.connect((host, port))
print("connected")
filename = "dog.jpeg"
file = open(filename, "wb")
while True:
    file_data = s.recv(4096)
    file.write(file_data)
    if not file_data:
        break
file.close()
print("file downloaded")