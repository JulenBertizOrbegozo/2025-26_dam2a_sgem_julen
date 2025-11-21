entrada = input("Introduce un texto: ")
entrada = entrada.replace(" ", "")
if entrada.isalpha():
    ordenado = sorted(entrada)
    print(ordenado)
else:
    print("No es una entrada válida")