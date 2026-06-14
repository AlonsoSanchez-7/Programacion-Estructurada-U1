"""
  Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
print("\033c")

# Set1
set1={"Python", "SQL", "Estructurado"}
print(set1)

for i in set1:
  print(i)

#Set2
set2={"Hola", True, 33, 3.1416}
print(set2)

set2_respaldo=set2.copy()
set2.clear()
print(set2)
print(set2_respaldo)

#Set3
set3={""}
print(set3)
set3.clear()

set3.add("UTD")
set3.add(3)
set3.add(10.0)
set3.add("3")
print(set3)
set3.add(3)
print(set3)

set3.pop()
set3.pop()
print(set3)
set3.clear()
set3.add(10)

lista=[10,9.5,8.5,3.4,8.5,10]
conjunto=set(lista)
lista=list(conjunto)
print(lista)

#ejemplo Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados

#Solucion 1
emails=[]

opc="SI"
while opc=="SI":
    emails.append(input("Dame un email: ").upper().strip())
    opc=input("¿Deseas agregar otro dato a la lista? (Si/No): ").upper().strip()
    
conjunto=set(emails)
emails=list(conjunto)
print(emails)

#Solucion 2
emails=[]

true=True
while true:
    emails.instert(0, input("Email: ").strip())
    opc=input("¿Deseas agregar otro dato a la lista? (Si/No): ").upper().strip()
    if opc == "NO":
        true=False
        
conjunto=set(emails)
emails=list(conjunto)
print(emails)