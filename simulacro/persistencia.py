import json   # Para leer y escribir archivos JSON
import os     # Para verificar si el archivo existe

ARCHIVO = "clientes.json"  # Nombre del archivo donde se guardan los datos

def cargar_clientes():
    """Carga los clientes desde el archivo JSON."""
    if os.path.exists(ARCHIVO):         # Si el archivo ya existe...
        with open(ARCHIVO, "r") as f:   # Ábrelo en modo lectura
            return json.load(f)         # Conviértelo a lista de diccionarios
    return []                           # Si no existe, retorna lista vacía

def guardar_clientes(clientes):
    """Guarda la lista de clientes en el archivo JSON."""
    with open(ARCHIVO, "w") as f:       # Crea o sobreescribe el archivo
        json.dump(clientes, f, indent=4) # Guarda con formato legible
