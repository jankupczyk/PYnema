import socket
from datetime import datetime
import youtube_dl
import cv2

HOST = '127.0.0.1'
PORT = 1337


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

clients = []

def download_video(url):
    ydl_opts = {
        'outtmpl': 'video.%(ext)s'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    cap = cv2.VideoCapture('video.mp4')
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def play_video(client_socket, file_path):
    cap = cv2.VideoCapture(file_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        client_socket.send(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

while True:
    client_socket, address = server_socket.accept()
    client_socket.send("#$#$#$#$#$#$#$#$ Welcome to the PYNEMA movie server! #$#$#$#$#$#$#$#$".encode())
    print(f"New connection - {address[0]}:{address[1]} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    clients.append(client_socket)
    url = client_socket.recv(1024).decode()
    download_video(url)
    file_path = "video.mp4"
    play_video(client_socket, file_path)
