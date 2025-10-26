import json
import os

clientes = {}  # Diccionario para simular la tabla hash

def cargar_clientes():
    """Carga los clientes desde archivos en el directorio actual."""
    for filename in os.listdir("."):
        if filename.endswith(".json"):
            nombre_cliente = filename[:-5]  # Elimina la extensión ".json"
            clientes[nombre_cliente] = filename
    print("Clientes cargados:", list(clientes.keys()))


def crear_cliente():
    """Crea un nuevo cliente y guarda su información en un archivo JSON."""
    nombre = input("Nombre del cliente: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")  # Permite ingresar texto libre
    email = input("Email: ")
    servicio_solicitado = input("Servicio solicitado: ")

    cliente_info = {
        "nombre": nombre,
        "direccion": direccion,
        "telefono": telefono,
        "email": email,
        "servicio_solicitado": servicio_solicitado,
    }

    filename = f"{nombre}.json"
    try:
        with open(filename, "w") as f:
            json.dump(cliente_info, f, indent=4)  # Guarda como JSON con indentación
        clientes[nombre] = filename
        print(f"Cliente {nombre} creado y guardado en {filename}")
    except Exception as e:
        print(f"Error al crear el cliente: {e}")


def leer_cliente(nombre_cliente):
    """Lee la información de un cliente desde un archivo JSON."""
    if nombre_cliente in clientes:
        filename = clientes[nombre_cliente]
        try:
            with open(filename, "r") as f:
                cliente_info = json.load(f)
                print("\nInformación del Cliente:")
                for key, value in cliente_info.items():
                    print(f"{key}: {value}")
        except FileNotFoundError:
            print(f"Error: El archivo {filename} no se encuentra.")
        except json.JSONDecodeError:
            print(f"Error: El archivo {filename} no contiene JSON válido.")
        except Exception as e:
            print(f"Error al leer el cliente: {e}")
    else:
        print(f"Error: No se encontró el cliente {nombre_cliente}.")


def modificar_cliente(nombre_cliente):
    """Modifica la información de un cliente existente en un archivo JSON."""
    if nombre_cliente in clientes:
        filename = clientes[nombre_cliente]
        try:
            with open(filename, "r") as f:
                cliente_info = json.load(f)
        except FileNotFoundError:
            print(f"Error: El archivo {filename} no se encuentra.")
            return
        except json.JSONDecodeError:
            print(f"Error: El archivo {filename} no contiene JSON válido.")
            return
        except Exception as e:
            print(f"Error al modificar el cliente (lectura): {e}")
            return

        print("\nInformación actual del cliente:")
        for key, value in cliente_info.items():
            print(f"{key}: {value}")

        print("\n¿Qué información desea modificar? (Deje en blanco para no modificar)")
        for key in cliente_info.keys():
            nuevo_valor = input(
                f"Nuevo valor para {key} (actual: {cliente_info[key]}): "
            )
            if nuevo_valor:
                cliente_info[key] = nuevo_valor

        try:
            with open(filename, "w") as f:
                json.dump(cliente_info, f, indent=4)
            print(f"Cliente {nombre_cliente} modificado y guardado en {filename}")
        except Exception as e:
            print(f"Error al modificar el cliente (escritura): {e}")
    else:
        print(f"Error: No se encontró el cliente {nombre_cliente}.")


def borrar_cliente(nombre_cliente):
    """Borra el archivo JSON de un cliente."""
    if nombre_cliente in clientes:
        filename = clientes[nombre_cliente]
        try:
            os.remove(filename)
            del clientes[nombre_cliente]
            print(f"Cliente {nombre_cliente} y su archivo {filename} han sido borrados.")
        except FileNotFoundError:
            print(f"Error: El archivo {filename} no se encuentra.")
        except OSError as e:
            print(f"Error al borrar el archivo {filename}: {e}")
        except Exception as e:
            print(f"Error al borrar el cliente: {e}")
    else:
        print(f"Error: No se encontró el cliente {nombre_cliente}.")


def listar_clientes():
    """Lista todos los clientes registrados."""
    if clientes:
        print("\nLista de clientes:")
        for nombre_cliente in clientes.keys():
            print(nombre_cliente)
    else:
        print("No hay clientes registrados.")


# Cargar clientes al inicio
cargar_clientes()

# Menú principal
while True:
    print("\n--- Menú ---")
    print("1. Crear cliente")
    print("2. Leer cliente")
    print("3. Modificar cliente")
    print("4. Borrar cliente")
    print("5. Listar clientes")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crear_cliente()
    elif opcion == "2":
        nombre = input("Nombre del cliente a leer: ")
        leer_cliente(nombre)
    elif opcion == "3":
        nombre = input("Nombre del cliente a modificar: ")
        modificar_cliente(nombre)
    elif opcion == "4":
        nombre = input("Nombre del cliente a borrar: ")
        borrar_cliente(nombre)
    elif opcion == "5":
        listar_clientes()
    elif opcion == "6":
        break
    else:
        print("Opción inválida.")

#todo esta excelente gracias