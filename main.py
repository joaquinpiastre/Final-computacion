from server import *
from client import *




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
            if not run_client(get_user_name()):
                continue
            break
            print("Creando sala de chat...")
        elif option == "2":
            if not run_client(get_user_name()):
                continue
            break
            print("Uniendo a sala de chat...")
        elif option == "3":
            exit_program()
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")