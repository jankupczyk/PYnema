import imutils
import cv2
import os
import numpy as np
import base64
import socket



BUFFOR_SIZE_DATA = 65507

# CLIENT SETTINGS
client_socket_main = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket_main.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFFOR_SIZE_DATA)

client_name = socket.gethostname()
client_ip_adress = ' '
client_port = 1337

welcomemessage = "HELLO " + client_name

client_socket_main.sendto(welcomemessage.encode(), (client_ip_adress, client_port))

while True:
    packet,_ = client_socket_main.recvfrom(BUFFOR_SIZE_DATA)
    data = base64.b85decode(packet,' /')
    npdata = np.fromstring(data, dtype=np.unit8)
    frame = cv2.imdecode(npdata, 1)
    cv2.imshow('Currently watching - ', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('c'):
        client_socket_main.close()
        break
