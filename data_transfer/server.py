import threading

import socket
import time

import cv2
from picamera2 import Picamera2

def SERVER():
    s = socket.socket()
    host = "172.16.98.38"
    port = 8080
    s.bind((host, port))
    s.listen(1)
    print(host)
    print("waiting...")
    conn, addr = s.accept()
    print(addr, "connected")
    filename = "image.jpeg"
    file = open(filename, "rb")
    # while for sending
    while True:
        file_data = file.read(4096)
        conn.send(file_data)
        if not file_data:
            break
    conn.close()
    print("file sended")

def image_reader():
    # Grab images as numpy arrays and leave everything else to OpenCV.

    picam2 = Picamera2()
    picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
    picam2.start()
    
    time_now = time.time()

    while time.time() - time_now >= 1:

        im = picam2.capture_array()

        grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        # cv2.imshow("Camera", im)
        # cv2.waitKey(1)
        time_now = time.time()
        cv2.imwrite("image.jpeg", im)

# init events
e1 = threading.Event()
e2 = threading.Event()

# init threads
t1 = threading.Thread(target=SERVER, args=())
t2 = threading.Thread(target=image_reader, args=())

# start threads
t1.start()
t2.start()

e1.set() # initiate the first event

# join threads to the main thread
t1.join()
t2.join()