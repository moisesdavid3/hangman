#turnos=input('Ingrese el numero de turnos:')
palabra = input('Ingrese la palabra a adivinar:')
while len(palabra) < 5:
    print('Hey, palabra minimo de 5 letras pelagato!')
    palabra = input('Ingrese la palabra a adivinar:')
intento = 5
acumu = ""
completas = []


def imprima_palabra():
    acierto = True
    for letra in palabra:
        if letra in acumu:
            print(letra, end=' '),
        else:
            print('.', end=' ')
            acierto = False
    return acierto


def quitar_intentos():
    intento -= 1
    print(f'\nPalabra no encontrada, te quedan {intento} intentos')
    return
    if intento == 0:
        print('Perdiste')
        return


while(intento > 0):
    completa = ""
    adiv = input("\nIngrese letra o palabra:")
    if len(adiv) > 1:
        completa += adiv
        if adiv == palabra:
            print("\nAdivinaste la palabra completa!")
            break
        elif completa in completas:
            print('\nYa mencionaste esa palabra!')
        else:
            completas.append(completa)
            imprima_palabra()
            quitar_intentos()

    elif adiv in acumu:
        print('Ya mencionaste esa letra!')
    else:
        acumu = acumu + adiv
        if adiv in palabra:
            result = imprima_palabra()
            if result:
                print("\nAcertaste a todas las letras, muy bien!")
                break
        else:
            imprima_palabra()
            intento -= 1
            print(f'\nLetra no encontrada, te quedan {intento} intentos')
            if intento == 0:
                print('Perdiste')
