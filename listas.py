# Tutorial con https://www.youtube.com/watch?v=IimBRwHhW54
lenguajes = ["Python", "Ruby", "PHP", "JavaScript", "Java"]
print(lenguajes)
print(lenguajes[1])

lenguajes[1] = "GO"
print(lenguajes)

print(lenguajes[-1]) # imprime java
print(lenguajes[-2]) # imprime JavaScript
#print(lenguajes[-9]) # imprime error

print(lenguajes[1:3]) # no incluye el indice 3
print(lenguajes[:3]) # desde el principio al 3 incluido
print(lenguajes[1:]) # desde el indice 1 al final incluido

lenguajes2 = ["Python", "Ruby", "PHP", "JavaScript", "Java"]
lenguajes2.insert(3, "GO") # se inserta en el indice 3
print(lenguajes2)
lenguajes2.insert(0, "C") 
lenguajes2.remove("Ruby")
print(lenguajes2)
print(len(lenguajes2))
print("PHP" in lenguajes2)
print("HTML" in lenguajes2)
lenguajes2.clear()
print(lenguajes2)

print("\n\nRecorro array lenguajes3 con while: ")
lenguajes3 = ["Python", "Ruby", "PHP", "JavaScript", "Java"]

i = 0
while i < len(lenguajes3):
    print(lenguajes3[i])
    i +=1 # es lo mismo que i = i+1

print("\n\nRecorro array lenguajes3 con for: ")
for lenguaje in lenguajes3:
    print(lenguaje)

print("\n\nAlgo raro: ")
i = 0
while i < 5:
    print(i * "El weta ")
    i +=1

print("\n\nImprimo un string: ")
i = 0
while i < 5:
    print( "El weta ")
    i +=1