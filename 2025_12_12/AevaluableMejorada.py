bruce = {"nombre": "Bruce Banner",'trabajos':[80, 50, 40, 20],'test': [75,75],'practicas':[78.20, 77.20]}
harry = {"nombre": "Harry Potter",'trabajos':[82, 56, 44, 30],'test': [80, 80],'practicas':[67.90, 78.72]}
hermione = {"nombre": "Hermione Ranger",'trabajos':[95, 100, 100, 100],'test': [99, 100],'practicas':[95.0, 80.5] }
peter = {"nombre": "Peter Parker",'trabajos':[30, 10, 100, 100],'test': [90, 10],'practicas':[50.0, 50.0]}
mario = {'nombre': "Super Mario",'trabajos':[77, 82, 23, 39],'test': [18, 60],'practicas':[80.6, 59.3]}
alumnos = [bruce, harry, hermione, peter, mario]
def clasificar(nota):
    rangos = [
        (90, "Sobresaliente"),
        (70, "Notable"),
        (60, "Bien"),
        (50, "Suficiente")
    ]
    for minimo, nombre in rangos:
        if nota >= minimo:
            return nombre
    return "Necesitas mejorar"

def sacarPorPantalla(nombre, nota, evaluacion):
    print()
    print(nombre)
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
    print(f"Nota media final para {nombre}: {nota:.2f}")
    print(f"Calificación final de {nombre}: {evaluacion}")
    print()

contador = 0
limite = 3
while True:
    entrada = input("Desea filtrar por calificación? (S/N): ").upper()
    if entrada[0] == "S" or entrada[0] == "N":
        break
    contador += 1
    if contador == limite:
        print("Has introducido el número máximo de opciones incorrectas, saliendo...")
        break
    else:
        restantes = limite - contador
        print("No has introducido un valor pedido")
        print(f"Quedan {restantes} intentos")

evaluacion = ""

if entrada == "S":
    print("Introduzca uno de los diguientes valores")
    entrada_calificacion = input("Sobresaliente - Notable - Bien - Suficiente - Necesita mejorar - Mostrar todo: ").upper()

for alumno in alumnos:
    nota_final = (0.1*(sum(alumno['trabajos']) / len(alumno['trabajos']))) + (0.5*(sum(alumno['test']) / len(alumno['test']))) + (0.4*(sum(alumno['practicas']) / len(alumno['practicas'])))
    evaluacion = clasificar(nota_final)

    if entrada == 'S':
        if entrada_calificacion == evaluacion.upper() or entrada_calificacion == "MOSTRAR TODO":
            sacarPorPantalla(alumno["nombre"], nota_final, evaluacion)
    elif entrada == 'N': 
        sacarPorPantalla(alumno["nombre"], nota_final, evaluacion)