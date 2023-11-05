import socket
sock = socket.socket()
host = "172.16.98.18"
port = 8080
sock.connect((host, port))
print("connected")

# sock.send('hello, Raspberry!')

filename = "dog"
file = open(filename, "rb")
counter = 0
while True:
    file_data = file.read(4096)
    sock.send(file_data)
    print(counter)
    counter += 1
    if not file_data:
        print("file is empty")
        break

file.close()
print("file sended")