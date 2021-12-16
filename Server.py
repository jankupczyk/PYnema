import imutils
import cv2
import os
import numpy as np
import base64
import socket
import time
from colorama import Fore


BUFFOR_SIZE_DATA = 65507

# SERVER SETTINGS
server_socket_main = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket_main.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFFOR_SIZE_DATA)

print(Fore.RED + 'UDP Server | '+ socket.getfqdn())
host_name = socket.gethostname()
print('HOST NAME:',host_name)
host_ip_adress = '' # Provide the valid IP address
print('HOST IP:',host_ip_adress)
host_port = 1337
print('PORT:',host_port)
socket_adress_main = (host_ip_adress, host_port)
server_socket_main.bind(socket_adress_main)
print('BUFFER:',BUFFOR_SIZE_DATA, 'kB')
avg_tmt = socket.getdefaulttimeout()
print('TIMEOUT:',avg_tmt)
print('INTERFACES:')
addr_info = socket.if_nameindex()
print(Fore.YELLOW + '',addr_info)
print(Fore.WHITE + ' ')
print(Fore.GREEN + 'Server is listening > > > >')
print(Fore.WHITE + ' ')
print(Fore.WHITE + 'Connected devices: ')

# VIDEO U WANT TO WATCH TOGETHER
server_video_main = cv2.VideoCapture('H:\VSC\PROJEKTY\PYnema\movies\Me_at_the_zoo.mp4')

# MAIN LOOP
while True:
    msg, client_addres_obligatory = server_socket_main.recvfrom(BUFFOR_SIZE_DATA)
    print('Connected from ', client_addres_obligatory)
    WIDTH = 1024
    while(server_video_main.isOpened()):
        _,frame = server_video_main.read()
        frame = imutils.resize(frame, width=WIDTH)
        encoded, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
        message = base64.b64encode(buffer)
        server_socket_main.sendto(message, client_addres_obligatory)
        cv2.imshow('HOST | Currently hosting for', frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('\x1b'): # ESC key
            server_socket_main.close()
            break

# AUTHOR: Jan Kupczyk
# https://github.com/jankupczyk