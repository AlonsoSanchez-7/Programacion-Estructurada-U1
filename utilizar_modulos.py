# 1er utilizar los modulos
import modulos

modulos.borrarPantalla()
modulos.funcion1()
n="Alonso"
a="Sánchez"

nombre, apellidos=modulos.funcion4(n,a)
print(f"Nombre completo es {nombre} {apellidos}")

# 2da forma de utilizar modulos
from modulos import *
from modulos import borrarPantalla, funcion3, funcion4

modulos.borrarPantalla()
n="Alonso"
a="Sánchez"
funcion3(n,a)

nombre, apellidos=funcion4(n,a)
print(f"Nombre completo es {nombre} {apellidos}")