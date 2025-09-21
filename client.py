import socket
import threading

SERVER_IP = input("Enter server IP: ")  # E.g., 192.168.1.2
PORT = 12345

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if not msg:
                break
            print(f"\nFriend: {msg}")
        except:
            break

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))
print("Connected to the server.")

threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

while True:
    msg = input("You: ")
    client.send(msg.encode())