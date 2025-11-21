entrada = input("introduce la capital, los años y el interes: ")
capital, anios, interes = entrada.split(",")
final = capital * (1 + interes) ** anios
print(f"Ganancias + capital = {final}")