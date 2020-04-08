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
    print("|      5      |   Salir                             |")
    print("|_____________|_____________________________________|")
    print(" ")
    var=int(input("Seleccione una actividad: "))
    return var

def int_view():
    print(" ____________________________")
    print("|          OPCIONES          |")
    print("|                            |")
    print("| 1. Ver producto especifico |")
    print("| 2. Ver todos los productos |")
    print("|                            |")
    print("|____________________________|")
    print(" ")
    var_2=int(input("Seleccione una opción: "))
    return var_2

#Funciones

stock={}
crud = True

def add():
    add_product=input("Ingrese el nombre del producto: ")
    add_quantity=int(input("Ingrese la cantidad a agregar: "))
    stock[add_product]=add_quantity

def view():
    var_2=int_view()
    if var_2==1:
        product=str(input("Escriba el nombre del producto: ").lower())
        print("Hay",stock[str(product)])
        comeback=input("Presione Enter para regresar")
    elif var_2==2:
        for item,quantity in stock.items():
            print(item,":",quantity)
        comeback=input("Presione Enter para regresar")
    elif var_2==3:
        print("ok")
    #else:                                      NO ME FUNCIONA ESTA MONDA
    #    print("No es una opción válida")

def modify():
    for num,item in enumerate(stock):
        print(num+1,".",item,":",stock[item])
    it_to_modify=str(input("Escriba el nombre del producto que desea modificar"))
    new_quantity=int(input("Escriba la nueva cantidad"))
    stock[it_to_modify]=new_quantity
    return stock
    
def delete():
    for num,item in enumerate(stock):
        print(num+1,".",item,":",stock[item])
    item_to_del=str(input("Escriba el nombre del producto que desea eliminar: ").lower())
    del stock[item_to_del]
    return stock

while crud==True:
    user=interfaz()
    if user==1:
        add()
    elif user==2:
        view()
    elif user==3:
        modify()
    elif user==4:
        delete()
    elif user==5:
        break