nombre = "Jai"
apellido = "Prasadh"
nombre_completo = (nombre + " " + apellido)

print(nombre_completo)
print(nombre_completo[3])

term = "ai"
result = nombre_completo.find(term)

if result == -1:
    print("Not found")
else:
    print("Term found in " + str(result) + "th position.")
