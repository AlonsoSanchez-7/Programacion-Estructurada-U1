#   TAREA
opc="S"
capturas = 0
caja = 0
aumento = 0
while opc == "S":
    nombre = input("Nombre Completo: ")
    time = float(input("No. De horas que trabajo: "))
    sueldo = float(input("Sueldo por hora: "))
    
    if time == 10:
        aumento = 0.20
    elif time == 15:
        aumento = 0.30
    elif time == 20:
        aumento = 0.15
    elif time >= 25:
        aumento = 0.08
    
    aumento_sueldo=sueldo*aumento
    sueldo_neto=sueldo+aumento_sueldo
        
    total_trabajadores+=1
    total_sueldos+=sueldo_neto
    
    print(f"El sueldo neto del trabajador ya con el aumento es de {sueldo_neto}")
    opc=input("¿Deseas capturar otra? (S/N) ").upper()
    
print(f"Se ingresaron {capturas} trabajadores")
print(f"La sumatoria de los sueldos netos de todos los trabajadores ingresados es de {caja}")
