from paquete1 import modulos,modulo_paquete
modulos.borrarPantalla()
nom="Alonso"
ape="Sánchez"

nombre,apellidos=modulos.funcion4(nom,ape)
edad1=modulo_paquete.solicitar_edad()
print(f"Nombre: {nombre}\n apellidos: {apellidos}\n edad: {edad1}")