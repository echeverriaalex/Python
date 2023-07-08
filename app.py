# para ejecutar el codigo:
# abrir consola cmd y escribir python app.py y enter

numeros = [1,2,3,4,5,6,7,8,9,0]

for numero in numeros:
    print(numero, end="_")



nombre = "Alex"
segundo = "Nahuel"
apellido = "Echeverria"

print("\n", nombre, segundo, apellido, sep="-")

print(nombre.upper())
print(nombre.lower())
print(nombre.find("x"))

string = "soy un string"

print(string.capitalize())

print(string.replace("string", "Programador"))
print(string.replace("str", "Programador"))
print("str" in string)

print(20 + 5)
print(20 * 3)
print(30 ** 3)
print(10 % 3)

n1 = 10
n2 = 15
print(n1 < n2)
print(n1 >= 10)


resultado = input("Ingresa tu edad: ")
print(resultado)
print(type(resultado))
numero = int(resultado)
print(numero  + 3)
str(22)
float("22.34")
bool("un string")
bool(False)
bool(0)
bool(1)
bool("")
bool(None)

edad = 25
print(edad > 18 and edad <30)
print(edad > 18 or edad <30)
print(not True)
print(not(edad > 18))

puntaje = 97
if puntaje >= 95:
    print("Aprobaste con honores")
elif puntaje >= 50:
    print("Alumno aprobado")
else:
    print("Desaprobado")

print("Fuera del if")
    

if (puntaje >= 95 and edad > 18) or edad < 40:
    print("probando varias condiciones para el if")