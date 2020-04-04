from datetime import datetime
hoy=datetime.now()
año=hoy.year
mes=hoy.month
dia=hoy.day

# INTERFAZ

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("         C O N T R O L    C O M E R C I A L ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Fecha: " +     str(dia)+"/"+str(mes)+"/"+str(año))
print(" ___________________________________________________")
print("|             |                                     |")
print("|  Actividad  |               Función               |")
print("|_____________|_____________________________________|")
print("|             |                                     |")
print("|      1      |   Agregar producto a STOCK          |")
print("|      2      |   Ver productos                     |")
print("|      3      |   Modificar productos               |")
print("|      4      |   Eliminar productos                |")
print("|_____________|_____________________________________|")

# CODIGOOOOOOO

print(" ")
selection=int(input("Seleccione una actividad: "))

#Funciones
#Función para agregar productos al stock
stock={}

def add():
    add_product=input("Ingrese el nombre del producto: ")
    add_quantity=int(input("Ingrese la cantidad a agregar: "))
    stock[add_product]=add_quantity
    return

if selection==1:
    add()
    ask=(input("Desea agregar más productos?:").lower())
    while ask=="si":
        add()
        ask=(input("Desea agregar más productos?:").lower())
    

print(stock)