#turnos=input('Ingrese el numero de turnos:')
# palabra = input('Ingrese la palabra a adivinar:')
# while len(palabra) < 5:
#     print('Hey, palabra minimo de 5 letras pelagato!')
#     palabra = input('Ingrese la palabra a adivinar:')

import random

f = open('words.txt')
lines = f.readlines()
palabra = random.choice(lines).strip()

print(f'\nTu palabra es de {len(palabra)} letras')
intento = 5
acumu = ""
completas = []


def ingresar_palabra():
    while True:
        pal = input("\nIngrese letra o palabra:")
        if pal.isalpha():
            return pal
        else:
            print("Solo se permiten letras")


def imprimir_palabra():
    acierto = True
    for letra in palabra:
        if letra in acumu:
            print(letra, end=' '),
        else:
            print('.', end=' ')
            acierto = False
    return acierto


while(intento > 0):
    completa = ""
    adiv = ingresar_palabra()
    if len(adiv) > 1:
        completa += adiv
        if adiv == palabra:
            print("\nAdivinaste la palabra completa!")
            break
        elif completa in completas:
            print('\nYa mencionaste esa palabra!')
        elif adiv in palabra:
            acumu += adiv
            result = imprimir_palabra()
            if result:
                print('\nAcertaste a todas las letras, muy bien!')
                break
        else:
            completas.append(completa)
            imprimir_palabra()
            intento -= 1
            print(f'\nPalabra no encontrada, te quedan {intento} intentos')
            if intento == 0:
                print('Perdiste')

    elif adiv in acumu:
        print('Ya mencionaste esa letra!')
    else:
        acumu = acumu + adiv
        if adiv in palabra:
            result = imprimir_palabra()
            if result:
                print("\nAcertaste a todas las letras, muy bien!")
                break
        else:
            imprimir_palabra()
            intento -= 1
            print(f'\nLetra no encontrada, te quedan {intento} intentos')
            if intento == 0:
                print('Perdiste')
