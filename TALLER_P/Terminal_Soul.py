import random

# =========================
# VARIABLES GLOBALES
# =========================
hp_heroe = 100
hp_enemigo = 120
pociones = 3


# =========================
# FUNCIONES 
# =========================

def generar_daño(minimo, maximo):
    daño = random.randint(minimo, maximo)

    # 10% probabilidad de crítico
    if random.randint(1, 10) == 1:
        daño *= 2
        print("💥 ¡GOLPE CRÍTICO!")

    return daño


def mostrar_estado(nombre_h, hp_h, nombre_e, hp_e):
    barras_heroe = "#" * max(0, hp_h // 10)
    barras_enemigo = "#" * max(0, hp_e // 10)

    print("\n===== ESTADO =====")
    print(f"{nombre_h}: [{barras_heroe:<10}] {hp_h} HP")
    print(f"{nombre_e}: [{barras_enemigo:<10}] {hp_e} HP")
    print(f"🧪 Pociones: {pociones}")
    print("==================\n")


# =========================
# TURNOS
# =========================

def turno_jugador():
    global hp_heroe, hp_enemigo, pociones
    
    while True:
        print("1. Atacar")
        print("2. Curar")
        print("3. Habilidad especial")

        opcion = input("Tu acción: ").strip()

        # ATAQUE NORMAL
        if opcion == "1":
            daño = generar_daño(10, 25)
            hp_enemigo -= daño
            print(f"⚔️ El héroe golpea por {daño} de daño!")
            break

        # CURACIÓN
        elif opcion == "2":
            if pociones <= 0:
                print("❌ No tienes pociones.")
            elif hp_heroe >= 100:
                print("❌ Ya tienes la vida completa.")
            else:
                hp_heroe += 20
                pociones -= 1
                print(f"🩹 Te curaste 20 HP. Pociones restantes: {pociones}")
                break

        # HABILIDAD ESPECIAL
        elif opcion == "3":
            if random.randint(1, 2) == 1:
                daño = generar_daño(30, 50)
                hp_enemigo -= daño
                print(f"🔥 Habilidad especial hace {daño} de daño!")
            else:
                print("❌ La habilidad falló.")
            break

        else:
            print("⚠️ Opción inválida. Intenta de nuevo.")


def turno_enemigo():
    global hp_heroe, hp_enemigo

    # IA básica: se cura si está bajo de vida (20%)
    if hp_enemigo <= 24:
        hp_enemigo += 20
        print("🩹 El enemigo se cura 20 HP")

    else:
        daño = generar_daño(15, 20)
        hp_heroe -= daño
        print(f"⚔️ El enemigo ataca por {daño} de daño")


# =========================
# VERIFICAR GANADOR
# =========================

def verificar_ganador():
    global hp_heroe, hp_enemigo

    if hp_heroe <= 0:
        print("\n💀 El héroe ha muerto. El enemigo gana.")
        return True

    elif hp_enemigo <= 0:
        print("\n🏆 El enemigo ha muerto. ¡El héroe gana!")
        return True

    return False


# =========================
# MAIN (BUCLE PRINCIPAL)
# =========================

def main():
    jugando = True

    while jugando:
        mostrar_estado("Héroe", hp_heroe, "Enemigo", hp_enemigo)

        turno_jugador()

        if verificar_ganador():
            break

        turno_enemigo()

        if verificar_ganador():
            break


# =========================
# EJECUCIÓN
# =========================

if __name__ == "__main__":
    main()