temperatura = float(input("Ingrese temperatura: "))
escala = input("Es Fahrenheit(F) o es Celsius(C) ? : ").lower()

if escala == "f":
    celsius = (temperatura - 32) * 5/9
    print("La temperatura ", temperatura, "ºF equivale a ", celsius , "ºC (grados Celsius)")
elif escala == "c":
    fahrenheit = temperatura * 1.8 + 32
    print("La temperatura ", temperatura, "ºC equivale a ", fahrenheit, "ºF (grados Fahrenheit)")
else:
    print("Error: la escala es incorrecta, reintente con ingresar F o C")
