from server import *
from cliente import *
from constant import *


def user_name():
    while True:
        user_name = input("Por favor, ingresa tu nombre de usuario: ")
        if len(user_name) > 0:
            return user_name
        else:
            print("El nombre de usuario no puede estar vacío. Por favor, intenta de nuevo.")


def main():
    while True:
        print("=================================")
        print("1. Crear sala de chat")
        print("2. Unirse a sala de chat")
        print("3. Salir")
        print("=================================")

        option = input("Por favor, selecciona una opción: ")

        if option == "1":
            run_server()
            if not start_client(user_name()):
                continue
            break
            print("Creando sala de chat...")
        elif option == "2":
            if not start_client(user_name()):
                continue
            break
            print("Uniendo a sala de chat...")
        elif option == "3":
            exit_program()
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


def exit_program():
    print("Saliendo...")
    exit(0)


if __name__ == "__main__":
    main()