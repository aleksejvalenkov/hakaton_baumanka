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
        try:
            output_image, marker = net.detect()
        except:
            print('image BED')
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
            client.make_req("StrtM")
            print('Started mission')
            break

        elif k == 32: # Space
            print('Space pressed')
            client.make_req("Magnt")
            print('Dropped')
            pass

        elif k == 113: # q
            print('q pressed')
            client.make_req("LedOn")
            print('Dropped')
            pass

        time.sleep(1)
    client.make_req("close")


if __name__ == "__main__":
    main()