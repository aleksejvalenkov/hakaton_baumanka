import socket

def make_req(com):
    global s
    s.send(com.encode('utf8'))


s = socket.socket()
host = "172.16.98.38"
port = 8080

s.connect((host, port))
print("connected")
filename = "dog2.jpeg"

make_req("getim")
# s.send("get_im".encode('utf8'))

file = open(filename, "wb")
while True:
    file_data = s.recv(4096)
    print(file_data)
    file.write(file_data)
    if not file_data or file_data == b'' or file_data[-1] == '@':
        break
file.close()
print("file downloaded")

make_req("close")



# print(file_data)
# cv2.imshow("Camera", im)
# cv2.waitKey(1)

