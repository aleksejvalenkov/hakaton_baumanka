import socket

# host = "172.16.98.38"

class Client:
    def __init__(self, host = "192.168.14.104", port = 8080) -> None:
        self.s = socket.socket()

        self.s.connect((host, port))
        print("connected")

    def make_req(self, com):
        self.s.send(com.encode('utf8'))

    def read_sock(self, filename):

        # filename = "image.jpeg"
        self.make_req("getim")
        # s.send("get_im".encode('utf8'))

        file = open(filename, "wb")
        while True:
            file_data = self.s.recv(4096)
            file.write(file_data)
            if file_data[-1] == 64:
                break
        file.close()
        print("file downloaded")






# print(file_data)
# cv2.imshow("Camera", im)
# cv2.waitKey(1)

