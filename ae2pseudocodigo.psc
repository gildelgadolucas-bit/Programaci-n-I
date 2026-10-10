Algoritmo CajeroAutomatico_AE2
	Definir cuentas, saldos Como Real
	Definir historial Como Cadena
	Dimensionar cuentas(3), saldos(3), historial(100)
	Definir cant_movimientos, pin, i, indice, opc Como Entero
	Definir monto Como Real
	Definir usuario_valido Como Lógico
	// Carga de datos en la estructuraa
	cuentas[1] <- 1111
	saldos[1] <- 50000
	cuentas[2] <- 2222 // Se usan los arreglos paralelos (solo para el pseudocodigo) asignando valores a cada posición
	saldos[2] <- 15000
	cuentas[3] <- 3333
	saldos[3] <- 500
	cant_movimientos <- 0
	usuario_valido <- Falso
	Escribir 'Ingrese su PIN de cuenta: '
	Leer pin
	// Búsqueda secuencial
	Para i<-1 Hasta 3 Con Paso 1 Hacer
		Si cuentas[i]==pin Entonces
			indice <- i
			usuario_valido <- Verdadero
		FinSi
	FinPara
	Si usuario_valido==Verdadero Entonces
		opc <- 0
		Mientras opc<>5 Hacer
			Escribir '1. consultar saldo / 2. depositar / 3. retirar / 4. ver historial / 5. salir'
			Leer opc
			Según opc Hacer
				1:
					Escribir 'Saldo: $', saldos[indice]
				2:
					Escribir 'Monto a depositar: $'
					Leer monto
					saldos[indice] <- saldos[indice]+monto
					cant_movimientos <- cant_movimientos+1
					historial[cant_movimientos] <- 'Depósito: $'+ConvertirATexto(monto)
					Escribir 'depósito realizado. Su nuevo saldo disponible es: $', saldos[indice]
				3:
					Escribir 'Monto a retirar: $'
					Leer monto
					Si monto<=saldos[indice] Entonces
						saldos[indice] <- saldos[indice]-monto
						cant_movimientos <- cant_movimientos+1
						historial[cant_movimientos] <- 'Retiro: $'+ConvertirATexto(monto)
						Escribir 'Extracción exitosa. Su nuevo saldo disponible es: $', saldos[indice]
					SiNo
						Escribir 'Fondos insuficientes'
					FinSi
				4:
					Escribir '-Historial-'
					Para i<-1 Hasta cant_movimientos Con Paso 1 Hacer
						Escribir historial[i]
					FinPara
			FinSegún
		FinMientras
	SiNo
		Escribir 'Esta cuenta no existe.'
	FinSi
FinAlgoritmo
