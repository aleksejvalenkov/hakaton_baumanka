from data_transfer.client import Client



client = Client()
client.read_sock("image.jpeg")

client.make_req("close")

