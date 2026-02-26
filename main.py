print("=================")
print("PROMEDIO DE NOTAS")
print("=================")

while True:
    nombre_estudiante = input("Ingrese nombre del estudiante: ")
    print("\n")
    if nombre_estudiante.replace(" ", "").isalpha():
        break
        
    else:
        print ("ERROR: Solo puedes ingresar letras!\n")
    

print("Ingresa tus notas escala de 1 a 10 (ej. 3.5 - 5.0): \n")

while True:
    try:
        nota_1 = float (input(f"Primera Nota: " ))
        if nota_1 >= 10.1:
            print ("La nota debe ser menor de 10\n")
            continue
        break
    except ValueError:
        print("ERROR: Debes ingresar solo numeros\n")
        continue


while True:
    try:
        nota_2 = float (input(f"Segunda Nota: " ))
        if nota_2 >= 10.1:
            print ("La nota debe ser menor de 10\n")
            continue
        break
    except ValueError:
        print("ERROR: Debes ingresar solo numeros\n")
        continue


while True:
    try:
        nota_3 = float (input(f"Tercera Nota: " ))
        if nota_3 >= 10.1:
            print ("La nota debe ser menor de 10\n")
            continue
        break
    except ValueError:
        print("ERROR: Debes ingresar solo numeros\n")
        continue






promedio_notas = (nota_1 + nota_2 + nota_3) / 3


print(f"Tu promedio de notas es: {(promedio_notas):.1f}") 