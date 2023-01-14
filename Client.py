import socket

HOST = '127.0.0.1'
PORT = 1337

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print(client_socket.recv(1024).decode())

url = input("Enter the video url you wanna watch: ")
client_socket.send(url.encode())

while True:
    audio_data = client_socket.recv(1024)
    if not audio_data:
        break
    # play audio here

client_socket.close()
