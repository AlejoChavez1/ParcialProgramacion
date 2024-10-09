pacientes = []

def menu():
    """Muestra las opciones del menú
    Args = None
    Return = None
    """
    print("""
----------------------------
  Sistema de gestión de la clínica
          
 [1] Cargar pacientes
 [2] Mostrar Pacientes
 [3] Buscar paciente por número de Historia Clinica
 [4] Ordernar pacientes por número de Historia Clínica
 [5] Mostrar paciente con más días de internación          
 [6] Mostrar paciente con menos días de internación  
 [7] Cantidad de pacientes con más de 5 dias de internacíon
 [8] Promedio día de internación de los pacientes
 [9] Salir

----------------------------
""")
    seleccion = int(input("| "))
    return seleccion

def cargar_pacientes (pacientes : list) -> None:
    """Agrega pacientes al array pacientes
    Args = pacientes : list
    Return = pacientes : list
    """
    contador = 0
    cantidad = int(input("Cuántos pacientes desea ingresar?: "))
    while contador < cantidad:
        historial = int(input("Número de historial clínico: "))
        nombre = input("Nombre del paciente: ").capitalize()
        edad = int(input("Edad del paciente: "))
        diagnostico = input("Diagnostico del paciente: ").capitalize()
        dias_internado = int(input("Cantidad de días internados: "))
        agregar_paciente = [historial,nombre,edad,diagnostico,dias_internado]
        pacientes.append(agregar_paciente)
        contador += 1
    return pacientes

def mostrar_pacientes (pacientes : list) -> None:
    """Muestra las opciones del menú
    Args = pacientes : list
    Return = None
    """
    print(f"PACIENTES\nHisto | Nomb | Edad | Sintoma | DI \n --------------------------------")
    for i in pacientes:
        print(i)

def busqueda_pacientes (pacientes : list) -> None:
    """Funcion para buscar al paciente por el numero de historial ingresado
    Args = pacientes : list
    Return = None
    """
    numero = int(input("Ingrese el numero de historial clinico del paciente que desea buscar: "))
    estado = None

    for i in range(len(pacientes)):  
        if numero == pacientes[i][0]:
            print(F"Paciente encontrado \n {pacientes[i]}")
        else:
            estado = False
    if estado == False:
            print(" - - - - - - - >\nNo se ha encontrado ningún paciente con ese número de historial clínico \n - - - - - - - - - - - >")
        
def ordenar_pacientes(pacientes : list) -> None:
    """Funcion para ordenar los pacientes de forma ascendente
    Args = pacientes : list
    Return = None
    """
    for i in range(len(pacientes) -1):
        for j in range(len(pacientes) -1 -i):
            if pacientes[j][0] > pacientes [j+1][0]:
                auxiliar = pacientes[j]
                pacientes[j] = pacientes[j+1]
                pacientes[j+1] = auxiliar
    print(f" -------------------------\n  Pacientes ordenados \n{pacientes}")

def mayor_internado (pacientes : list) -> None: 
    """Funcion que muestra en pantalla el paciente con mas dias internado
    Args = pacientes : list
    Return = None
    """
    mas_internado = ""
    dias = 0
    for i in range(len(pacientes)):
        if pacientes[i][4] > dias:
            mas_internado = pacientes[i]
    print(f" -------------------------\n  Paciente con más tiempo internado \n{mas_internado}")

def menor_internado (pacientes : list) -> None: 
    """Funcion para mostrar el paciente con menos dias internados
    Args = pacientes : list
    Return = None
    """
    menor_internado = ""
    dias = 9999999
    for i in range(len(pacientes)):
        if pacientes[i][4] < dias:
            menor_internado = pacientes[i]
    print(f" -------------------------\n  Paciente con más tiempo internado \n{menor_internado}")

def internacion_mayor_cinco (pacientes : list) -> None:
    """Funcion que imprime la cantidad de pacientes con tiempo internado mayor a 5 dias
    Args = pacientes : list
    Return = None
    """
    contador = 0
    for i in range(len(pacientes)):
        if pacientes[i][4] > 5:
            contador += 1
    print(f"La cantidad total de pacientes con más de 5 días internados es de {contador}")

def promedio_dias_internados(pacientes : list) -> None:
    """Funcion que imprime el promedio de la cantidad de dias entre los pacientes
    Args = pacientes : list
    Return = None
    """
    suma_dias = 0
    cantidad_pacientes = len(pacientes)
    for i in range(len(pacientes)):
        suma_dias += pacientes[i][4]
    promedio = 0
    promedio = suma_dias / cantidad_pacientes
    print(F"El promedio de días internados de todos los pacientes es de: {promedio}")

def seleccion_menu()-> None:
    """Funcion para la seleccion de la funcion que desea usar
    Args = None
    Return = None
    """
    seguir = "s"
    while seguir == "s":
        num = menu()
        match num:
            case 1: cargar_pacientes(pacientes)
            case 2: mostrar_pacientes(pacientes)
            case 3: busqueda_pacientes (pacientes)
            case 4: ordenar_pacientes(pacientes)
            case 5: mayor_internado(pacientes)
            case 6: menor_internado(pacientes)
            case 7: internacion_mayor_cinco(pacientes)
            case 8: promedio_dias_internados(pacientes)
            case 9: seguir = "n"
            case _: print("Ingresar una opcion valida")
