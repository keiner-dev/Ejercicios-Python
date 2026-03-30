from persistencia import guardar_clientes  # Importa solo la función de guardar

PLANES_VALIDOS = ["mensual", "trimestral", "anual"]

# ─────────────────────────────────────────────
# FUNCIÓN 1: Crear cliente
# ─────────────────────────────────────────────

def crear_cliente(clientes):
    print("\n── Registrar nuevo cliente ──")

    nuevo_id = max([c["id"] for c in clientes], default=0) + 1  # ID automático

    nombre = input("Nombre: ").strip()
    if not nombre:
        print("❌ El nombre no puede estar vacío.")
        return

    try:
        edad = int(input("Edad: "))
        if edad <= 0 or edad > 120:
            print("❌ Edad inválida.")
            return
    except ValueError:
        print("❌ La edad debe ser un número.")
        return

    print(f"Planes disponibles: {', '.join(PLANES_VALIDOS)}")
    plan = input("Tipo de plan: ").strip().lower()
    if plan not in PLANES_VALIDOS:
        print("❌ Plan inválido.")
        return

    cliente = {
        "id": nuevo_id,
        "nombre": nombre,
        "edad": edad,
        "plan": plan,
        "estado": "activo"
    }

    clientes.append(cliente)
    guardar_clientes(clientes)         # Llama a la función del otro módulo
    print(f"✅ Cliente '{nombre}' registrado con ID {nuevo_id}.")

# ─────────────────────────────────────────────
# FUNCIÓN 2: Listar clientes
# ─────────────────────────────────────────────

def listar_clientes(clientes):
    print("\n── Lista de clientes ──")

    if not clientes:
        print("No hay clientes registrados.")
        return

    for c in clientes:
        print(f"ID: {c['id']} | Nombre: {c['nombre']} | Edad: {c['edad']} | "
              f"Plan: {c['plan']} | Estado: {c['estado']}")

# ─────────────────────────────────────────────
# FUNCIÓN 3: Buscar cliente
# ─────────────────────────────────────────────

def buscar_cliente(clientes):
    print("\n── Buscar cliente ──")
    termino = input("Ingresa ID o nombre: ").strip().lower()

    resultados = [
        c for c in clientes
        if termino == str(c["id"]) or termino in c["nombre"].lower()
    ]

    if not resultados:
        print("❌ No se encontraron clientes.")
    else:
        for c in resultados:
            print(f"ID: {c['id']} | Nombre: {c['nombre']} | Edad: {c['edad']} | "
                  f"Plan: {c['plan']} | Estado: {c['estado']}")

# ─────────────────────────────────────────────
# FUNCIÓN 4: Actualizar cliente
# ─────────────────────────────────────────────

def actualizar_cliente(clientes):
    print("\n── Actualizar cliente ──")

    try:
        id_buscar = int(input("ID del cliente a actualizar: "))
    except ValueError:
        print("❌ El ID debe ser un número.")
        return

    cliente = next((c for c in clientes if c["id"] == id_buscar), None)

    if not cliente:
        print("❌ Cliente no encontrado.")
        return

    print(f"Cliente actual: {cliente}")
    print("(Presiona Enter para mantener el valor actual)")

    nuevo_nombre = input(f"Nuevo nombre [{cliente['nombre']}]: ").strip()
    if nuevo_nombre:
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
    elif nuevo_plan:
        print("❌ Plan inválido, se mantiene el anterior.")

    nuevo_estado = input(f"Estado (activo/inactivo) [{cliente['estado']}]: ").strip().lower()
    if nuevo_estado in ["activo", "inactivo"]:
        cliente["estado"] = nuevo_estado
    elif nuevo_estado:
        print("❌ Estado inválido, se mantiene el anterior.")

    guardar_clientes(clientes)
    print("✅ Cliente actualizado.")

# ─────────────────────────────────────────────
# FUNCIÓN 5: Eliminar cliente
# ─────────────────────────────────────────────

def eliminar_cliente(clientes):
    print("\n── Eliminar cliente ──")

    try:
        id_eliminar = int(input("ID del cliente a eliminar: "))
    except ValueError:
        print("❌ El ID debe ser un número.")
        return

    cliente = next((c for c in clientes if c["id"] == id_eliminar), None)

    if not cliente:
        print("❌ Cliente no encontrado.")
        return

    confirmacion = input(f"¿Eliminar a '{cliente['nombre']}'? (s/n): ").lower()
    if confirmacion == "s":
        clientes.remove(cliente)
        guardar_clientes(clientes)
        print("✅ Cliente eliminado.")
    else:
        print("Operación cancelada.")
