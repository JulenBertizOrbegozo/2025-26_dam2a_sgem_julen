import random
numeroEntrada = 0
rawStudentNames = ["Ana", "Luis", "Carlos", "María", "Jorge", "Sofía", "Pedro", "Lucía", "Miguel", "Elena",
                   "Diego", "Carmen", "Javier", "Isabel", "Alberto", "Marta", "Sergio", "Laura", "Fernando", "Patricia"]
listaGenerada = []
intentos = 0
maxIntentos = 3

numeroEntrada = input("Ingrese un número entero positivo no superior a 20: ")
if numeroEntrada.isdigit():
    numeroEntrada = int(numeroEntrada)
elif not numeroEntrada.isdigit():
    numeroEntrada = -1
    intentos += 1
    
while numeroEntrada < 0 or numeroEntrada > 20 :
    if intentos >= maxIntentos:
        print("Has intentado introducir un valor incorrecto muchas veces, saliendo...")
        exit()
    print("El número no es positivo o es superior a 20.")
    numeroEntrada = input("Ingrese un número entero positivo: ")
    if numeroEntrada.isdigit():
        numeroEntrada = int(numeroEntrada)
        break
    elif not numeroEntrada.isdigit():
        numeroEntrada = -1
    intentos += 1

for i in range(numeroEntrada):
    nombreAleatorio = random.choice(rawStudentNames)
    listaGenerada.append(nombreAleatorio)
    
print(f"Lista generada de {numeroEntrada} alumnos:")
print(listaGenerada)
