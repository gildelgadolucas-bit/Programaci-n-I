def mostrar_menu():
    print("\n- TORNEOS - LITORAL -")
    print("1. Inscribir pareja")
    print("2. Registrar resultado de partido")
    print("3. Ver tabla de posiciones")
    print("4. Salir")
    return input("Seleccione una opción: ")

def inicializar_equipo():
    return {
        "puntos": 0,
        "partidos_jugados": 0,
        "sets_favor": 0,
        "sets_contra": 0
    }

def main():
    # Base de datos en memoria
    grupos = {"Grupo A": {}, "Grupo B": {}}
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            nombre = input("Nombre de la pareja (Ej: fulano/mengano): ")
            grupo = input("Asignar al Grupo (A o B): ").upper()
            
            grupo_key = f"Grupo {grupo}"
            if grupo_key in grupos:
                grupos[grupo_key][nombre] = inicializar_equipo()
                print(f" Pareja {nombre} anotada en el {grupo_key}.")
            else:
                print(" Grupo no válido.")
                
        elif opcion == "2":
            grupo = input("Grupo del partido (A o B): ").upper()
            grupo_key = f"Grupo {grupo}"
            
            if grupo_key in grupos and len(grupos[grupo_key]) >= 2:
                eq1 = input("Pareja 1: ")
                eq2 = input("Pareja 2: ")
                
                if eq1 in grupos[grupo_key] and eq2 in grupos[grupo_key]:
                    sets_eq1 = int(input(f"Sets ganados por {eq1}: "))
                    sets_eq2 = int(input(f"Sets ganados por {eq2}: "))
                    
                    # Lógica de puntuación: 3 puntos al ganador
                    if sets_eq1 > sets_eq2:
                        grupos[grupo_key][eq1]["puntos"] += 3
                    else:
                        grupos[grupo_key][eq2]["puntos"] += 3
                        
                    # Actualización de estadísticas
                    grupos[grupo_key][eq1]["sets_favor"] += sets_eq1
                    grupos[grupo_key][eq1]["sets_contra"] += sets_eq2
                    grupos[grupo_key][eq1]["partidos_jugados"] += 1
                    
                    grupos[grupo_key][eq2]["sets_favor"] += sets_eq2
                    grupos[grupo_key][eq2]["sets_contra"] += sets_eq1
                    grupos[grupo_key][eq2]["partidos_jugados"] += 1
                    
                    print(" Resultado registrado con éxito.")
                else:
                    print(" Alguna de las parejas no existe en ese grupo.")
            else:
                print(" No hay suficientes equipos en el grupo.")
                
        elif opcion == "3":
            grupo = input("¿Qué grupo desea ver? (A o B): ").upper()
            grupo_key = f"Grupo {grupo}"
            
            if grupo_key in grupos:
                print(f"\n--- TABLA DE POSICIONES {grupo_key} ---")
                print(f"{'Pareja':<15} | {'PTS':<4} | {'PJ':<3} | {'SF':<3} | {'SC':<3} | {'DIF':<4}")
                print("-" * 45)
                
                # Ordenar por puntos (de mayor a menor)
                equipos_ordenados = sorted(
                    grupos[grupo_key].items(), 
                    key=lambda x: (x[1]["puntos"], x[1]["sets_favor"] - x[1]["sets_contra"]), 
                    reverse=True
                )
                
                for nombre, stats in equipos_ordenados:
                    dif = stats["sets_favor"] - stats["sets_contra"]
                    print(f"{nombre:<15} | {stats['puntos']:<4} | {stats['partidos_jugados']:<3} | {stats['sets_favor']:<3} | {stats['sets_contra']:<3} | {dif:<4}")
            else:
                print("Grupo no válido.")
                
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print(" Opción incorrecta.")

if __name__ == "__main__":
    main()
