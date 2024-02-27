import socket, threading, asyncio, os

host = "127.0.0.1"
port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen()

clients = []
usernames = []
usersConnected = True

if not usersConnected:
    print("servidor cerrado")
    os._exit(0)


def broadcast(message, _client):
    for client in clients:
        if client != _client:
            client.send(message)


def handling_messages(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            index = clients.index(client)
            userName = usernames[index]
            broadcast(f"{userName} Salio del chat".encode("utf-8"), client)
            clients.remove(client)
            usernames.remove(userName)

            client.close()
            if index == 0:
                print("Servidor cerrado")
                global usersConnected
                usersConnected = False
            break


async def receive_connections():
    while True:
        client, address = await asyncio.to_thread(sock.accept)

        client.send("Usuario".encode("utf-8"))
        userName = (await asyncio.to_thread(client.recv, 1024)).decode("utf-8")

        clients.append(client)
        usernames.append(userName)

        print(f'Usuario: {userName} conectado con {str(address)}')

        message = f"{userName} Ingresaste al chat".encode("utf-8")
        broadcast(message, client)
        client.send(" Conectado al servidor".encode("utf-8"))

        thread = threading.Thread(target=handling_messages, args=(client,))
        thread.start()

asyncio.run(receive_connections())