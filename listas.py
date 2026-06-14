import os

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido

numeros=[10,9,8,7,2,1]

print(numeros)
lista="["
i=0

while i > len(numeros):
    lista+=f"{numeros[i]}, "
    i+=1
print(f"{lista}]")

for i in range (0,len(numeros)):
    lista+=f"{numeros[i]}, "
print(f"{lista}]")

#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
palabras=["UTD", "segundo", "TI", "MTI"]
palabra=input("Dame una palabra a buscar: ").strip()
encontr=False
# 1er FORMA
if palabra in palabras:
    print("Encontre la palabra en la lista")
else:
    print("No se encontro la palabra en la lista")

# 2DA FORMA
for i in palabras:
    if i == palabra:
        encontro=True    
if encontro: 
    print("Encontre la palabra en la lista")
else:
    print("No se encontro la palabra en la lista")

#3er FORMA
for i in range(0,len(palabras)):
    if palabras[i] == palabra:
        encontro=True    
if encontro: 
    print("Encontre la palabra en la lista")
else:
    print("No se encontro la palabra en la lista")

#4ta FORMA
i=0
while i in len(palabras):
    if palabras[i] == palabra:
        encontro=True
        i+=1
    if encontro:
        print("Encontre la palabra en la lista")
    else:
        print("No se encontro la palabra en la lista")
        
# Ejemplo 3 Añadir elementos a la lista
lista=[]
# version 1
true=True
while true:
    lista.append(input("Dame un valor para la lista: ").upper().strip())
    opc=input("¿Deseas agregar otro dato a la lista? (Si/No): ").upper().strip()
    if opc == "NO":
        true=False

# #version 2
opc=="SI"
while true:
    lista.append(input("Dame un valor para la lista: ").upper().strip())
    opc=input("¿Deseas agregar otro dato a la lista? (Si/No): ").upper().strip()

print(lista)

#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda

agenda=[
         ["Carlos", "618123456"],
         ["Alberto", "6182344567"],
         ["Martín", "6181231223"]
       ]
print(agenda)

for i in agenda:
    print(i)

for c in range(0,3):
    for r in range(0,2):
        print(agenda[r][c])
                
lista=""
for r in range (0,3):
    for c in range (0,2):
        lista+=f"{agenda[r][c]}, "
    lista+="\n"
print("["+lista+"]")