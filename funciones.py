"""
Puede escribir aqui las funciones del codigo
Se importaran de forma automatica al 'main.py'
"""
# ------ NO BORRAR -----
import time
from funciones import *

def test () -> None:
    """
        Funcion para probar el archivo
    """
    import herramientas
    menu = herramientas.load_items('menu.csv')
    print(menu)

# esto es para que test solo corra si es ejecutado directamente
if __name__ == '__main__':
    test()
# ------ NO BORRAR -----

#Escribir Funciones desde aqui hacia abajo ------------

#ejemplo de funcion
def foo () -> any:
    ...


def comprar (carrito:list):
    if len(carrito) > 0:
        precio_final = 0
        for i in carrito:
            precio_final = precio_final + i['precio']

        print("Usted tiene", len(carrito), "en el carro, haciendo un total de", precio_final)
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
        user_in = input("Y/N >> ")
        if user_in == "y":
            carrito = []
            print("Muchas gracias!!")
            time.sleep(1)
            return carrito
        elif user_in == "n":
            return carrito
    else:
        print("No tiene elementos agregados al carrito")
        time.sleep(1)

def agregar_carrito (items:list, carrito:list):
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
            break
            
        else:
             print("Número ingresado fuera de rango, intente nuevamente. ")
             time.sleep(2)
             continue
    return carrito

def mostrar_carrito (carrito:list):
    print("Esto es lo que tiene actualmente en el carrito: ")
    contador = 0
    if len(carrito) > 0:
        for i in carrito:
            contador += 1
            print(contador, '-', i['nombre'], 'con valor de', i['precio'])
    else:
        print("No tiene elementos seleccionados en su carrito. ")