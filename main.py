import os

CLIENT_FOLDER = "clientes"

def create_client():
    """Crea un nuevo archivo para un cliente."""
    name = input("Nombre del cliente: ")
    info = input("Información del cliente: ")
    filename = os.path.join(CLIENT_FOLDER, f"{name}.txt")

    with open(filename, "w") as file:
        file.write(info)
    print(f"Cliente {name} creado con éxito.")

def read_client():
    """Lee la información de un cliente existente."""
    name = input("Nombre del cliente: ")
    filename = os.path.join(CLIENT_FOLDER, f"{name}.txt")

    try:
        with open(filename, "r") as file:
            info = file.read()
        print(f"Información de {name}:\n{info}")
    except FileNotFoundError:
        print(f"Cliente {name} no encontrado.")

def modify_client():
    """Modifica la información de un cliente existente."""
    name = input("Nombre del cliente: ")
    filename = os.path.join(CLIENT_FOLDER, f"{name}.txt")

    try:
        with open(filename, "w") as file:
            new_info = input("Nueva información del cliente: ")
            file.write(new_info)
        print(f"Cliente {name} modificado con éxito.")
    except FileNotFoundError:
        print(f"Cliente {name} no encontrado.")

def delete_client():
    """Elimina el archivo de un cliente existente."""
    name = input("Nombre del cliente: ")
    filename = os.path.join(CLIENT_FOLDER, f"{name}.txt")

    try:
        os.remove(filename)
        print(f"Cliente {name} eliminado con éxito.")
    except FileNotFoundError:
        print(f"Cliente {name} no encontrado.")

def list_clients():
    """Lista todos los clientes."""
    if not os.path.exists(CLIENT_FOLDER):
        print("No hay clientes registrados.")
        return

    clients = [f[:-4] for f in os.listdir(CLIENT_FOLDER) if f.endswith('.txt')]
    if clients:
        print("Lista de clientes:")
        for client in clients:
            print(client)
    else:
        print("No hay clientes registrados.")

def main():
    """Función principal del programa."""
    os.makedirs(CLIENT_FOLDER, exist_ok=True)

    while True:
        print("\nOpciones:")
        print("1. Crear cliente")
        print("2. Leer cliente")
        print("3. Modificar cliente")
        print("4. Eliminar cliente")
        print("5. Listar clientes")
        print("6. Salir")

        option = input("Seleccione una opción: ")

        if option == "1":
            create_client()
        elif option == "2":
            read_client()
        elif option == "3":
            modify_client()
        elif option == "4":
            delete_client()
        elif option == "5":
            list_clients()
        elif option == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()