bruce = {
    "nombre": "Bruce Banner",
    'trabajos':[80, 50, 40, 20],
    'test': [75,75],
    'practicas':[78.20, 77.20]
    }
harry = {
    "nombre": "Harry Potter",
    'trabajos':[82, 56, 44, 30],
    'test': [80, 80],
    'practicas':[67.90, 78.72]
    }
hermione = {
    "nombre": "Hermione Ranger",
    'trabajos':[95, 100, 100, 100],
    'test': [99, 100],
    'practicas':[95.0, 80.5]
    }
peter = {
    "nombre": "Peter Parker",
    'trabajos':[30, 10, 100, 100],
    'test': [90, 10],
    'practicas':[50.0, 50.0]
    }
mario = {
    'nombre': "Super Mario",
    'trabajos':[77, 82, 23, 39],
    'test': [18, 60],
    'practicas':[80.6, 59.3]
    }

alumnos = [bruce, harry, hermione, peter, mario]
nota_alumnos = {}
evaluacion = ""
sobresaliente = "Sobresaliente"
notable = "Notable"
bien = "Bien"
suficiente = "Suficiente"
necesitas_mejorar = "Necesitas mejorar"
entrada = input("Desea filtrar por calificación? (S/N): ").upper()
if entrada == "S":
    print("Introduzca uno de los diguientes valores")
    entrada_calificacion = input("Sobresaliente - Notable - Bien - Suficiente - Necesita mejorar - Mostrar todo: ").upper()

for alumno in alumnos:
    trabajos = alumno['trabajos']
    test = alumno['test']
    practicas = alumno['practicas']
    nota_trabajos = (trabajos[0] + trabajos[1] + trabajos[2] + trabajos[3]) / 4 
    nota_test = (test[0] + test[1]) / 2
    nota_practicas = (practicas[0] + practicas[1]) / 2
    nota_final = (0.1*nota_trabajos) + (0.5*nota_test) + (0.4*nota_practicas)
    
    if nota_final >= 90:
        evaluacion = sobresaliente
    elif nota_final >= 70:
        evaluacion = notable
    elif nota_final >= 60:
        evaluacion = bien
    elif nota_final >= 50:
        evaluacion = suficiente
    else:
        evaluacion = necesitas_mejorar
    #paraMeter = {'nombre': alumno['nombre'], ["nota"] : nota_final, ["evaluacion"]: evaluacion}
    #nota_alumnos[alumno['nombre']] = paraMeter

    #Filtrado de notas
    
    if entrada == 'S':
        if entrada_calificacion == evaluacion.upper() or entrada_calificacion == "MOSTRAR TODO":
            print(alumno['nombre'])
            print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
            print(f"Nota media final para {alumno['nombre']}: {nota_final:.2f}")
            print(f"Calificación final de {alumno['nombre']}: {evaluacion}")
            print()
    elif entrada == 'N': 
        print(alumno['nombre'])
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
        print(f"Nota media final para {alumno['nombre']}: {nota_final:.2f}")
        print(f"Calificación final de {alumno['nombre']}: {evaluacion}")
        print()
    else:
        print("Entrada no válida, saliendo...")
        break
            
"""seguir = True
while seguir:
    entrada = input("Desea filtrar por calificación? (S/N): ").upper()
    if entrada == 'S':
        print("introduzca uno de los siguientes valores")
        calificacion_entrada = input(f"{sobresaliente.upper} - {notable.upper} - {bien.upper}, {suficiente.upper}, {necesitas_mejorar.upper} ")
        for alumno in nota_alumnos.values():
            for nombre, nota, evaluacion1 in alumno.items():
                if evaluacion1.upper() == calificacion_entrada.upper():
                    print(nombre)
                    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
                    print(f"Nota media final para {nombre}: {nota:.2f}")
                    print(f"Calificación final de {nombre}: {evaluacion1}")
                    print()
        seguir = False
    elif entrada == 'N':
        for nombre, nota in nota_alumnos.items():
            print(nombre)
            print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
            print(f"Nota media final para {nombre}: {nota}")
            print(f"Calificación final de {nombre}: {nota_alumnos['evaluacion']}")
            print()
        seguir = False    
"""


