# Un módulo es simplemente un archivo con extensión .py que contiene código de Python (funciones, clases, variables, etc.).

def borrarPantalla():
    print("\033c")
def funcion1():
   nombre=input("Nombre: ").strip().upper()
   apellido=input("Apellidos: ").strip().upper()
   print(f"El Nombre del alumno es: {nombre} {apellido}")

 #3.- Funcion que recibe parametros y no regresa valor 
def funcion3(nom,ape):
   nombre=nom
   apellido=ape
   print(f"El Nombre del alumno es: {nombre} {apellido}")
   
 #2.- Funcion que no recibe parametros y regresa valor
def funcion2():
   nombre=input("Nombre: ").strip().upper()
   apellido=input("Apellidos: ").strip().upper()
   return nombre, apellido

 #4.- Funcion que recibe parametros y regresa valor
def funcion4(nom,ape):
   nombre=nom
   apellido=ape
   return nombre, apellido


borrarPantalla()