import socket
import threading
import asyncio
import os
from time import sleep


HOST = "127.0.0.1"
PORT = 60688

clients = []
usernames = []
users_connected = True

async def handle_client(client, address):
    try:
        client.send("Usuario".encode("utf-8"))
        while True:
            try:
                username = client.recv(1024).decode("utf-8")
            except BlockingIOError:
                await asyncio.sleep(0.01)  # wait for 10ms before trying again
                continue
            break

        with threading.Lock():
            clients.append(client)
            usernames.append(username)

        print(f'Usuario: {username} conectado desde {str(address)}')

        message = f"{username} se ha unido al chat".encode("utf-8")
        broadcast(message, client)

        while True:
            try:
                message = client.recv(1024)
            except BlockingIOError:
                await asyncio.sleep(0.01)  # wait for 10ms before trying again
                continue
            if not message:
                break
            broadcast(message, client)

    except Exception as e:
        print(f"Error en la conexión con {address}: {e}")

    finally:
        with threading.Lock():
            if client in clients:
                index = clients.index(client)
                username = usernames[index]
                broadcast(f"{username} ha salido del chat".encode("utf-8"), client)
                clients.remove(client)
                usernames.remove(username)
                client.close()

def broadcast(message, sender):
    with threading.Lock():
        for client in clients:
            if client != sender:
                try:
                    client.send(message)
                except Exception as e:
                    print(f"Error al enviar mensaje: {e}")

async def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    server.setblocking(False)

    loop = asyncio.get_event_loop_policy().get_event_loop()

    while users_connected:
        try:
            client, address = await loop.run_in_executor(None, server.accept)
        except BlockingIOError:
            continue
        print(f"Conexión establecida con {str(address)}")
        task = asyncio.create_task(handle_client(client, address))

async def main():
    await start_server()

if __name__ == "__main__":
    asyncio.run(main())
