import socket
import threading
from urllib import response
import test
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 32567  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        data = conn.recv(1024)
        print("=> "+data[:-1].decode("utf-8"))
        text = data[:-1].decode("utf-8")
        print(text)
        response = test.request_sentiment_keywords(text)
        message_to_send = response.encode("UTF-8")
        conn.send(len(message_to_send).to_bytes(2, byteorder='big'))
        conn.send(message_to_send)

