import random


def main():
    print("Bienvenido a Camel!\n"
          "Has robado un camello en el desierto y te han descubierto y ahora tienes que hiur de ellos\n"
          "Al mismo tiempo tienes que controlar tu sed,\n"
          "el cansancio del camello y cuanta distancia le sacas a los nativos")

    opciones = "A. Correr a toda velocidad.\n" \
               "B. Correr a velocidad moderada.\n" \
               "C. Beber de tu cantimplora.\n" \
               "D. Parar y descansar durante la noche.\n" \
               "E. Mirar status.\n" \
               "Q. Salir :( \n" \
               "Elige una opción: "

    done = False
    kilometros_recorridos = 0
    kilometros_avanzados = 0
    sed = 0
    cansancio_camello = 0
    kilometros_recorridos_de_los_nativos = -20
    numero_cantimploras = 3

    while not done:
        print(opciones, end="")
        respuesta = input()
        respuesta = respuesta.upper()
        if respuesta == "Q":
            done = True
            print("Has salido del juego exitosamente")
        elif respuesta == "E":
            print("Status: \n""Kilometros recorridos: ", kilometros_recorridos, "\n""Cantimploras: ",
                  numero_cantimploras,
                  "\n""Los nativos están a {} kilometros detrás de ti".format(
                      abs(kilometros_recorridos_de_los_nativos)))
        elif respuesta == "D":
            print("El camello se siente aliviado y te escupe")
            cansancio_camello = 0
            kilometros_recorridos_de_los_nativos += random.randint(7, 15)
        elif respuesta == "A":
            kilometros_avanzados += random.randint(10, 21)
            print("Kilometros avanzados: ", kilometros_avanzados)
            kilometros_recorridos += kilometros_avanzados
            sed += 1
            cansancio_camello += random.randint(1, 4)
            kilometros_recorridos_de_los_nativos += random.randint(7, 15)
        elif respuesta == "B":
            kilometros_avanzados += random.randint(5, 12)
            print("Kilometros avanzados: ", kilometros_avanzados)
            kilometros_recorridos += kilometros_avanzados
            sed += 1
            cansancio_camello += 1
            kilometros_recorridos_de_los_nativos += random.randint(7, 15)
        elif respuesta == "C":
            if numero_cantimploras == 0:
                print("No tienes cantimploras")
            else:
                print("Bebes de tu sucia cantimplora saboreando hasta la última gota ")
                numero_cantimploras -= 1
                sed = 0
        else:
            print("Eso no es una opción válida, mete una maldita letra del menú")
        if not done:
            if 4 <= sed < 6:
                print("\nEstás sediento...\n")
            if sed >= 6:
                print("\nHas muerto de sed!!\n")
                done = True
        if not done:
            if 5 <= cansancio_camello < 8:
                print("\nEl camello se está cansando...\n")
            elif cansancio_camello >= 8:
                print("\nEl camello se ha muerto\n")
                done = True
        if not done:
            if kilometros_recorridos <= kilometros_recorridos_de_los_nativos:
                print("\nLos nativos te han pillado!!\n")
                done = True
            elif -15 <= kilometros_recorridos - abs(kilometros_recorridos_de_los_nativos) < 0:
                print("\nLos nativos te pisan los talones!!\n")
        if not done:
            if kilometros_recorridos >= 200:
                print("Enhorabuena, has escapado :D!!!")
                done = True


main()
