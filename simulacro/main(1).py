from persistencia import cargar_clientes   # Importa función de carga
from clientes import (                     # Importa todas las funciones CRUD
    crear_cliente,
    listar_clientes,
    buscar_cliente,
    actualizar_cliente,
    eliminar_cliente
)

def mostrar_menu():
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
    clientes = cargar_clientes()            # Carga datos al iniciar
    print(f"📂 {len(clientes)} cliente(s) cargado(s).")

    while True:
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
            break
        else:
            print("❌ Opción inválida. Elige entre 1 y 6.")

if __name__ == "__main__":
    main()
