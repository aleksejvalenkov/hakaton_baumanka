import socket
sock = socket.socket()
host = "172.16.98.182"
port = 8080
sock.bind((host, port))
sock.listen(1)
print(host)
print("waiting...")
conn, addr = sock.accept()
print(addr, "connected")
filename = "dog2.jpeg"
file = open(filename, "wb")
while True:
    file_data = conn.recv(4096)
    # print(file_data)
    file.write(file_data)
    if not file_data:
        break
conn.close()
print("file downloaded")