from herramientas import *

from funciones import *


'''Revisar Menu (Obligatorio) [20]
Muestra el menú de comidas, con el precio. También permite seleccionar un
item del menú para agregarlo al “carrito”'''

import time
items = load_items("menu.csv")

'''carrito = []
while(True):
        print("Este es nuestro menu disponible:\n")
        contador = 0
        for i in items:
            contador+=1
            print(contador, "-", i['nombre'], "- con precio de", i['precio'], "pesos")


        try:
            user_in = int(input("Seleccione número de item que quiera agregar al carrito: >> "))
        except:
            print("VALOR INGRESADO NO VÁLIDO. INTÉNTELO NUEVAMENTE")
        if user_in in range(len(items)+1):
            carrito.append(items[user_in-1])
            print(carrito)
            break
            
        else:
             print("Número ingresado fuera de rango, intente nuevamente. ")
             time.sleep(2)
             continue
'''

'''- Revisar Carrito (Obligatorio) [20]
Muestra el carrito de comidas seleccionadas.'''


'''carrito = load_items("menu.csv")
print("Esto es lo que tiene actualmente en el carrito: ")
contador = 0
if len(carrito) > 0:
    for i in carrito:
        contador += 1
        print(contador, '-', i['nombre'], 'con valor de', i['precio'])
'''




'''- Pagar (Obligatorio) [20]
Muestra el costo total y cantidad de ítems del carrito. Luego sugiere la
propina (10%). El usuario puede:
- Aceptar: (se asume que paga) y se vacía el carrito.
- Seguir Comprando: Se vuelve al menú principal'''

'''precio_final = 0
for i in items:
    precio_final = precio_final + i['precio']

print(precio_final)'''
'''print("Usted tiene", len(items), "en el carro, haciendo un total de", precio_final)
print("¿Quiere agregar la propina?")
while(True):
    user_in = input("Y/N >> ")

    if user_in.lower() == "y":
        precio_final = precio_final +(precio_final*0.10)
        print(precio_final)
        break
    elif user_in.lower() =="n":
        break
    else:
        print("Carácter(es) no válido(s), intente de nuevo. ")
        continue
print("El percio final es", precio_final, "\n¿desea pagar?")
user_in = si_no()

if user_in == "y":
    carrito = []
elif user_in == "n":'''

'''Quitar Ítem de Carrito [10]
Saca un objeto del carrito.'''

'''carro = items

print("Seleccione con un número el elemento que quiera eliminar del carrito: ")
contador = 0
for i in carro:
            contador += 1
            print(contador, '-', i['nombre'], 'con valor de', i['precio'])

try:
    user_in = int(input(">> "))
except:
    print("NÚMERO NO VÁLIDO")
    #continue
if user_in in range((len(carro))+1):
    carro.pop(user_in-1)
else:
    print("Numero fuera de rango. ")'''

'''Guardar Carrito [20]
Se guarda el carrito y el dueño del carrito en un archivo que sea
“<nombre_usuario>.carrito”'''
'''- Buscar ítem en carrito, por nombre [10]
Se debe buscar un item en el carrito según el nombre.'''
contador = 0
nombre = input(">> ")
for i in items:
    if nombre.lower() in i['nombre']:
        contador+=1
        print(contador, "-", i["nombre"])
