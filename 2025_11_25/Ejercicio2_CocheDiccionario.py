carFeatures = [("brand", "Lanborghini"), ("model", "Huracan"),("hp", 750),("Gasoil", False)]
diccionarioCoche = {}
for feature in carFeatures:
    diccionarioCoche[feature[0]] = feature[1]
for clave, valor in diccionarioCoche.items():
    print(f"La etiqueta {clave} tiene el valor {valor}")