import socket
s = socket.socket()
host = "172.16.98.38"
port = 8080

s.connect((host, port))
print("connected")
filename = "dog2.jpeg"

def make_req(sock):
    sock.send("get_im".encode('utf8'))



make_req(s)
file = open(filename, "wb")
while True:
    file_data = s.recv(4096)
    file.write(file_data)
    if not file_data:
        break

file.close()
print("file downloaded")

print(file_data)
# cv2.imshow("Camera", im)
# cv2.waitKey(1)

