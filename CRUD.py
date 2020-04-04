from datetime import datetime
hoy=datetime.now()
año=hoy.year
mes=hoy.month
dia=hoy.day

# INTERFAZ
def interfaz():
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
    print(" ")
    var=int(input("Seleccione una actividad: "))
    return var

user=interfaz()

#Funciones
#Función para agregar productos al stock
stock={}

def add():
    add_product=input("Ingrese el nombre del producto: ")
    add_quantity=int(input("Ingrese la cantidad a agregar: "))
    stock[add_product]=add_quantity
    return

if user==1:
    add()
    ask=(input("Desea agregar más productos?:").lower())
    while ask=="si":
        add()
        ask=(input("Desea agregar más productos?:").lower())
    interfaz()

if user==2:
    print(" ____________________________")
    print("|          OPCIONES          |")
    print("|                            |")
    print("| 1. Ver producto especifico |")
    print("| 2. Ver todos los productos |")
    print("| 3. Volver                  |")
    print("|____________________________|")
    print(" ")
ask_two=int(input("Seleccione una opción: "))

if ask_two==1:
    product=str(input("Escriba el nombre del producto: ").lower())
    print(stock[str(product)])
elif ask_two==2:
    print(stock)