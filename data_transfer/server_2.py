import socket
s = socket.socket()
host = "172.16.98.182"
port = 8080
s.bind((host, port))
s.listen(1)
print(host)
print("waiting...")
conn, addr = s.accept()
print(addr, "connected")
filename = "dog2.jpeg"
file = open(filename, "wb")
while True:
    file_data = conn.recv(4096)
    file.write(file_data)
    if not file_data:
        break
conn.close()
print("file downloaded")