import socket
s = socket.socket()
host = "172.16.98.38"
port = 8080
s.bind((host, port))
s.listen(1)
print(host)
print("waiting...")
conn, addr = s.accept()
print(addr, "connected")
filename = "dog"
file = open(filename, "rb")
while True:
    file_data = file.read(4096)
    conn.send(file_data)
    if not file_data:
        break
conn.close()
print("file sended")