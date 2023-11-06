from data_transfer.client import Client
import time



def main():
    counter = 0
    client = Client()
    while True:
        client.read_sock("image.jpeg")
        if counter == 10:
            break
    counter += 1
    time.sleep(0.2)
    client.make_req("close")


if __name__ == "__main__":
    main()