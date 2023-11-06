from data_transfer.client import Client
from people_det import Net
import cv2
import time



def main():
    counter = 0
    client = Client()
    net = Net()
    while True:
        client.read_sock("image.jpeg")
        if counter == 100:
            break
        counter += 1
        # Place to NET
        output_image, marker = net.detect()
        print(f"People on image: {marker}")
        if marker:
            client.make_req("PTrue")
        else:
            client.make_req("PFals")

        # # visualize the image
        cv2.imshow('Keypoint image', output_image)
        k = cv2.waitKey(1)
        if k == 27: # Esc
            print('Esc pressed')
            break

        elif k == 13: # Enter
            print('Enter pressed')
            
            print('Started mission')
            break

        elif k == 32: # Space
            print('Space pressed')

            print('Dropped')
            pass

        time.sleep(0.1)
    client.make_req("close")


if __name__ == "__main__":
    main()