# ------ NO BORRAR -----
from funciones import *
from herramientas import *
# ------ NO BORRAR -----
import time

print("Bienvenido a nuestro restaurante\nAntes de empezar le preguntaremos un par de cosas:")
time.sleep(1)
nombre = input("Ingrese nombre: >> ")
fav_food = input("Ingrese comida favorita: >> ")
alergias = input("Ingrese alergias que tenga: >> ")

user = {
    "nombre":nombre,
    "comida_favorita":fav_food,
    "alergias":alergias
}
menu = load_items("menu.csv")
carrito = []

#menu principal
while (True):

    print("INGRESE ACCIÓN DESEADA:\n1-Agregar comida al carrito.\n2-Mirar tu carrito.\n3- Comprar")

    user_in= int(input(">> "))
    ...
    #escribir menu con funciones aqui

    if user_in == 1:
        agregar_carrito(menu,carrito)


    elif user_in == 2:
        mostrar_carrito(carrito)
        time.sleep(1)
    
    elif user_in == 3:
        comprar(carrito)