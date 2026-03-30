import json  # Para guardar y cargar datos en archivo .json
import os    # Para verificar si el archivo existe

# ─────────────────────────────────────────────
# CONSTANTES
# ─────────────────────────────────────────────
ARCHIVO = "clientes.json"  # Nombre del archivo donde se guardan los datos
PLANES_VALIDOS = ["mensual", "trimestral", "anual"]  # Opciones de plan permitidas

# ─────────────────────────────────────────────
# PERSISTENCIA: Guardar y Cargar
# ─────────────────────────────────────────────

def cargar_clientes():
    """Carga los clientes desde el archivo JSON al iniciar el programa."""
    if os.path.exists(ARCHIVO):          # Si el archivo ya existe...
        with open(ARCHIVO, "r") as f:    # Ábrelo en modo lectura
            return json.load(f)          # Conviértelo de JSON a lista de diccionarios
    return []                            # Si no existe, retorna lista vacía

def guardar_clientes(clientes):
    """Guarda la lista de clientes en el archivo JSON."""
    with open(ARCHIVO, "w") as f:        # Abre (o crea) el archivo en modo escritura
        json.dump(clientes, f, indent=4) # Convierte la lista a JSON con formato bonito

# ─────────────────────────────────────────────
# FUNCIÓN 1: Crear cliente
# ─────────────────────────────────────────────

def crear_cliente(clientes):
    """Registra un nuevo cliente y lo agrega a la lista."""
    print("\n── Registrar nuevo cliente ──")

    # Generar ID automático: busca el mayor ID existente y le suma 1
    nuevo_id = max([c["id"] for c in clientes], default=0) + 1

    nombre = input("Nombre: ").strip()          # .strip() elimina espacios al inicio/fin
    if not nombre:                              # Validación: nombre no puede estar vacío
        print("❌ El nombre no puede estar vacío.")
        return

    try:
        edad = int(input("Edad: "))             # Intenta convertir a entero
        if edad <= 0 or edad > 120:             # Validación de rango lógico
            print("❌ Edad inválida.")
            return
    except ValueError:                         # Si el usuario escribe letras, captura el error
        print("❌ La edad debe ser un número.")
        return

    print(f"Planes disponibles: {', '.join(PLANES_VALIDOS)}")
    plan = input("Tipo de plan: ").strip().lower()  # .lower() convierte a minúsculas
    if plan not in PLANES_VALIDOS:             # Verifica que el plan sea válido
        print("❌ Plan inválido.")
        return

    # Crear diccionario con los datos del cliente
    cliente = {
        "id": nuevo_id,
        "nombre": nombre,
        "edad": edad,
        "plan": plan,
        "estado": "activo"   # Por defecto, todo cliente nuevo es activo
    }

    clientes.append(cliente)           # Agrega el diccionario a la lista
    guardar_clientes(clientes)         # Guarda los cambios en el archivo
    print(f"✅ Cliente '{nombre}' registrado con ID {nuevo_id}.")

# ─────────────────────────────────────────────
# FUNCIÓN 2: Listar clientes
# ─────────────────────────────────────────────

def listar_clientes(clientes):
    """Muestra todos los clientes registrados."""
    print("\n── Lista de clientes ──")

    if not clientes:                           # Si la lista está vacía...
        print("No hay clientes registrados.")
        return

    # Recorre cada cliente (diccionario) en la lista
    for c in clientes:
        print(f"ID: {c['id']} | Nombre: {c['nombre']} | Edad: {c['edad']} | "
              f"Plan: {c['plan']} | Estado: {c['estado']}")

# ─────────────────────────────────────────────
# FUNCIÓN 3: Buscar cliente
# ─────────────────────────────────────────────

def buscar_cliente(clientes):
    """Busca un cliente por ID o por nombre."""
    print("\n── Buscar cliente ──")
    termino = input("Ingresa ID o nombre a buscar: ").strip().lower()

    # Busca en toda la lista usando comprensión de listas
    # Compara si el término coincide con el ID (convertido a string) o está en el nombre
    resultados = [
        c for c in clientes
        if termino == str(c["id"]) or termino in c["nombre"].lower()
    ]

    if not resultados:                         # Si no encontró nada...
        print("❌ No se encontraron clientes.")
    else:
        for c in resultados:                   # Muestra cada resultado encontrado
            print(f"ID: {c['id']} | Nombre: {c['nombre']} | Edad: {c['edad']} | "
                  f"Plan: {c['plan']} | Estado: {c['estado']}")

# ─────────────────────────────────────────────
# FUNCIÓN 4: Actualizar cliente
# ─────────────────────────────────────────────

def actualizar_cliente(clientes):
    """Modifica los datos de un cliente existente."""
    print("\n── Actualizar cliente ──")

    try:
        id_buscar = int(input("ID del cliente a actualizar: "))
    except ValueError:
        print("❌ El ID debe ser un número.")
        return

    # Busca el cliente en la lista comparando IDs
    cliente = next((c for c in clientes if c["id"] == id_buscar), None)
    # next() retorna el primer elemento que cumpla la condición, o None si no encuentra

    if not cliente:                            # Si no existe ese ID...
        print("❌ Cliente no encontrado.")
        return

    print(f"Cliente actual: {cliente}")
    print("(Presiona Enter para mantener el valor actual)")

    # Para cada campo, si el usuario no escribe nada, se conserva el valor anterior
    nuevo_nombre = input(f"Nuevo nombre [{cliente['nombre']}]: ").strip()
    if nuevo_nombre:                           # Solo actualiza si escribió algo
        cliente["nombre"] = nuevo_nombre

    nueva_edad = input(f"Nueva edad [{cliente['edad']}]: ").strip()
    if nueva_edad:
        try:
            cliente["edad"] = int(nueva_edad)
        except ValueError:
            print("❌ Edad inválida, se mantiene la anterior.")

    print(f"Planes: {', '.join(PLANES_VALIDOS)}")
    nuevo_plan = input(f"Nuevo plan [{cliente['plan']}]: ").strip().lower()
    if nuevo_plan and nuevo_plan in PLANES_VALIDOS:
        cliente["plan"] = nuevo_plan
    elif nuevo_plan:                           # Si escribió algo pero no es válido
        print("❌ Plan inválido, se mantiene el anterior.")

    nuevo_estado = input(f"Nuevo estado (activo/inactivo) [{cliente['estado']}]: ").strip().lower()
    if nuevo_estado in ["activo", "inactivo"]:
        cliente["estado"] = nuevo_estado
    elif nuevo_estado:
        print("❌ Estado inválido, se mantiene el anterior.")

    guardar_clientes(clientes)                 # Guarda los cambios
    print("✅ Cliente actualizado correctamente.")

# ─────────────────────────────────────────────
# FUNCIÓN 5: Eliminar cliente
# ─────────────────────────────────────────────

def eliminar_cliente(clientes):
    """Elimina un cliente de la lista por su ID."""
    print("\n── Eliminar cliente ──")

    try:
        id_eliminar = int(input("ID del cliente a eliminar: "))
    except ValueError:
        print("❌ El ID debe ser un número.")
        return

    # Busca el cliente por ID
    cliente = next((c for c in clientes if c["id"] == id_eliminar), None)

    if not cliente:
        print("❌ Cliente no encontrado.")
        return

    confirmacion = input(f"¿Seguro que deseas eliminar a '{cliente['nombre']}'? (s/n): ").lower()
    if confirmacion == "s":                    # Solo elimina si confirma con "s"
        clientes.remove(cliente)               # Elimina el diccionario de la lista
        guardar_clientes(clientes)             # Guarda los cambios
        print("✅ Cliente eliminado.")
    else:
        print("Operación cancelada.")

# ─────────────────────────────────────────────
# MENÚ PRINCIPAL
# ─────────────────────────────────────────────

def mostrar_menu():
    """Imprime las opciones del menú."""
    print("\n╔══════════════════════════════╗")
    print("║   🏋️  GIMNASIO - CLIENTES   ║")
    print("╠══════════════════════════════╣")
    print("║  1. Crear cliente            ║")
    print("║  2. Listar clientes          ║")
    print("║  3. Buscar cliente           ║")
    print("║  4. Actualizar cliente       ║")
    print("║  5. Eliminar cliente         ║")
    print("║  6. Salir                    ║")
    print("╚══════════════════════════════╝")

def main():
    """Función principal: carga datos, ejecuta el menú en bucle."""
    clientes = cargar_clientes()               # Carga los clientes al iniciar
    print(f"📂 {len(clientes)} cliente(s) cargado(s).")

    while True:                                # Bucle infinito hasta que el usuario salga
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            crear_cliente(clientes)
        elif opcion == "2":
            listar_clientes(clientes)
        elif opcion == "3":
            buscar_cliente(clientes)
        elif opcion == "4":
            actualizar_cliente(clientes)
        elif opcion == "5":
            eliminar_cliente(clientes)
        elif opcion == "6":
            print("👋 ¡Hasta luego!")
            break                              # Sale del while y termina el programa
        else:
            print("❌ Opción inválida. Elige entre 1 y 6.")

# ─────────────────────────────────────────────
# PUNTO DE ENTRADA
# ─────────────────────────────────────────────

# Esto asegura que main() solo se ejecute si corres este archivo directamente
# (no si lo importas desde otro archivo)
if __name__ == "__main__":
    main()
