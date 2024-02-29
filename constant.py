import os, subprocess


def run_server():
    os.chdir(r".")
    subprocess.Popen(["start", "cmd", "/k", "py server.py"], shell=True)
    print("Servidor ejecutado correctamente.")

#colores
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'