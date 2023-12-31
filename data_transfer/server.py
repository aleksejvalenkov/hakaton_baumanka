import threading

import socket
import time

import cv2
from picamera2 import Picamera2

from esp_uart import serial_reader

# global variables
Magnet = '0'
Led = '0'
Voice = '0'
People = False

sonic_dist = 1000000
flame = False




def SERVER():
    global Magnet
    global Led
    global Voice
    global People

    picam2 = Picamera2()
    picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
    picam2.start()

    s = socket.socket()
    host = "172.16.98.38"
    # host = "192.168.1.84"
    # host = "192.168.14.103"
    # host = "10.42.0.34"

    port = 8080
    s.bind((host, port))
    s.listen(1)
    print(host)
    print("waiting...")
    conn, addr = s.accept()
    print(addr, "connected")
    filename = "image.jpeg"
    while True:
        data = conn.recv(40).decode("utf8")
        if not data:
            break
        print("__________________________________________________")
        print(f"Reseivde : \t {data}")

        if data == 'getim':

            print("cast")
            im = picam2.capture_array()
            im = cv2.rotate(im, cv2.ROTATE_180)
            cv2.imwrite(filename, im)


            file = open(filename, "rb")
            # while for sending
            while True:
                file_data = file.read(4096)
                conn.send(file_data)
                if not file_data:
                    break
            conn.send("@".encode('utf8'))
            print("file sended")

        elif data == 'PTrue':
            print("")
            People = True
            Led = '1'
            Voice = '7'
            print(f'People on image: {People}')

        elif data == 'PFals':
            print("")
            People = False
            Led = '0'
            Voice = '0'
            print(f'People on image: {People}')

        elif data == 'StrtM':
            print("")
            # TO_DO
            # print(f'People on image: {People}')

        elif data == 'Magnt':
            print("")
            Magnet = '0'
            print(f'Droping rescue kit')

        elif data == 'LedOn':
            print("")
            Led == '1'
            
            print(f'Led  : {Led}')
            

        elif data == 'close':
            conn.close()
            print("connection close")
            break
    
        
    

def image_reader():
    # Grab images as numpy arrays and leave everything else to OpenCV.
    pass
    # picam2 = Picamera2()
    # picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
    # picam2.start()

    # sleep = 1

    # while True:
    #     print("cast")
    #     im = picam2.capture_array()

    #     grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    #     # cv2.imshow("Camera", im)
    #     # cv2.waitKey(1)
    #     time_now = time.time()
    #     cv2.imwrite("image.jpeg", im)
    #     time.sleep(sleep)

def serial_prot():
    # pass
    global Magnet 
    global Led
    global Voice
    global flame
    global sonic_dist

    sleep = 0.1
    esp = serial_reader()

    while True:
        # flame, Magnet_status, sonic_dist = esp.esp_reader(Voice, Magnet, Led)
        print(Voice, Magnet, Led)
        esp.esp_reader(Voice, Magnet, Led)
        time.sleep(sleep)

def logic():
    # global Magnet 
    # global Led
    # global Voice
    # global People

    # if People:
    #     Led = '1'
    #     Voice = '3'
    # else:
    #     Led = '0'
    #     Voice = '0'
    pass


# init events
e1 = threading.Event()
e2 = threading.Event()
e3 = threading.Event()

# init threads
t1 = threading.Thread(target=SERVER, args=())
t2 = threading.Thread(target=logic, args=())
t3 = threading.Thread(target=serial_prot, args=())

# start threads
t1.start()
t2.start()
t3.start()

e1.set() # initiate the first event

# join threads to the main thread
t1.join()
t2.join()
t3.join()