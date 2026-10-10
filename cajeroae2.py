# cajero_ae2.py
# Uso un diccionario donde la clave es el PIN y el valor es el saldo
base_datos = {
    1111: 50000.0,
    2222: 15000.0,
    3333: 500.0
}

# Uso una lista para guardar el historial de movimientos
historial_sesion = []

print("-Cajero automático-")
pin = int(input("Ingrese su PIN de cuenta: "))

# validación del pin
if pin in base_datos:
    print("\nAcceso concedido.")
    opcion = 0
    # estructura de control repetitiva
    while opcion != 5:
        print("\n¿Qué desea hacer?")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Ver historial")
        print("5. Salir")
        opcion = int(input("Ingrese una opción: "))
        # estructura de control selectiva
        if opcion == 1:
            print(f"Saldo disponible: ${base_datos[pin]}")
            
        elif opcion == 2:
            monto = float(input("Ingrese el monto a depositar: $"))
            if monto > 0:
                base_datos[pin] += monto # Se actualiza el diccionario
                historial_sesion.append(f"Depósito: +${monto}") # Se inserta en la lista
                print(f"Depósito exitoso. Su nuevo saldo disponible es: ${base_datos[pin]}")
            else:
                print("Monto inválido.")
                
        elif opcion == 3:
            monto = float(input("Ingrese el monto a retirar: $"))
            if monto <= base_datos[pin]:
                base_datos[pin] -= monto
                historial_sesion.append(f"Retiro: -${monto}")
                print(f"Retiro exitoso. Su nuevo saldo disponible es: ${base_datos[pin]}")
            else:
                print("Fondos insuficientes.")
                
        elif opcion == 4:
            print("\n- Historial -")
            if len(historial_sesion) == 0:
                print("No hay movimientos registrados.")
            else:
                # estructura repetitiva for para recorrer la lista de datos
                for movimiento in historial_sesion:
                    print(movimiento)
            print("-----")
            
        elif opcion == 5:
            print("Saliendo del sistema...")
        else:
            print("Opción inválida.")
else:
    print("Esta cuenta no existe")
