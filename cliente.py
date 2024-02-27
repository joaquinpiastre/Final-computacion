import socket, threading
from main import main
from constant import *
from autocorrector import *

def start_client(username):
    host = "127.0.0.1"
    port = 8080

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, port))
    except socket.error as e:
        print("No se pudo conectar al servidor")
        return False

    def receive_messages():
        while True:
            try:
                receivedMessage = client.recv(1024).decode("utf-8")
                if receivedMessage == "USER":
                    client.send(username.encode("utf-8"))
                else:
                    print(f"\n{receivedMessage}\n")
            except:
                print("ocurrio un error al recibir el mensaje.")
                main()
                client.close()
                break

    def write_messages():
        while True:
            writedMessage = correct_word(input(""))
            if writedMessage == "cerrar":
                client.close()
                break
            else:
                client.send((f"{username}: {writedMessage}").encode("utf-8"))
    
    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

    write_thread = threading.Thread(target=write_messages)
    write_thread.start()

    return True