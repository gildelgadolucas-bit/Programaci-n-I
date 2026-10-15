alumnos = [
    { "nombre": "Juan", "notas": [7, 8, 9, 6], "asistencia": 90 },
    { "nombre": "Maria", "notas": [5, 6, 4, 7], "asistencia": 60 },
    { "nombre": "Pedro", "notas": [1, 9, 4, 7], "asistencia": 95 },
    { "nombre": "Ana", "notas": [6, 5, 7, 8], "asistencia": 85 }
]

def calcular_promedio(notas):
    """Calcula el promedio de un arreglo de notas."""
    if len(notas) == 0:
        return 0
    suma = sum(notas)
    return suma / len(notas)

def es_regular(alumno):
    """
    Evalua si un alumno es regular por su registro.
    Criterios: Promedio >= 6 y Asistencia >= 75.
    """
    promedio = calcular_promedio(alumno["notas"])
    
    if promedio >= 6.0 and alumno["asistencia"] >= 75:
        return True
    else:
        return False

def verificar_estado_alumno(nombre_buscado, lista_alumnos):
    """
    Busca a un alumno por su nombre en el arreglo y verifica su estado.
    """
    for alumno in lista_alumnos:
        if alumno["nombre"].lower() == nombre_buscado.lower():
            if es_regular(alumno):
                return f"El alumno {alumno['nombre']} si esta regular."
            else:
                return f"El alumno {alumno['nombre']} no esta regular."
                
    return f"El alumno '{nombre_buscado}' no se encontró en el sistema."

print("- Consulta de Regularidad -")
print(verificar_estado_alumno("Juan", alumnos))  
print(verificar_estado_alumno("Maria", alumnos))  
print(verificar_estado_alumno("Pedro", alumnos))  
print(verificar_estado_alumno("Ana", alumnos))   
