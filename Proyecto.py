# Import's
import random
import matplotlib.pyplot as plt

# Menú
def menu():
    print('''
1 - Jugar Piedra, papel, tijera
        
2 - Adivinar el número contra la computadora
    
3 - Tirar un dado
        
4 - Graficar una función matemática
    ''')

# Clase
class Juegos:
    """
        ///// PPT /////
        El usuario ingresará un elemento de opciones, si no lo ingresa o ingresa de otra manera, tendrá que ingresarlo nuevamente
        el bot es el método .choice de la libreria random que elije un elemento de opciones
        la entrada del usuario se les quitará los espaciós y se ordenará las mayúsuculas y minúsculas
        Hay un sistema de condiciones donde se define cual es el ganador

        
        ///// num_random /////
        el bot es el método .randint de la libreria random que elige un número del 1 al 5
        el user, tendra que eligir un número del 1 al 5 si ingresa otra cosa, imprimirá que debe ingresar el número estimado
        y deberá a volver ingresar.
        Mediante una condición, se define cual es el ganador.

        dado: la cara es el método .choice de la libreria random, donde eligirá un número del 1 al 6
        y se imprimirá el número 

        
        ///// grafico /////
        Hay 2 bloques de código:
        
        - Eje Y: El usuario tendrá que escribir uno por uno los ejes que pueden ser enteros o flotantes, si escribe otra cosa
        imprimirá que tiene que elegir los números adecuados.

        Si en la entrada del usuario tiene un punto, será un número flotante, 
        si da error, se le dirá que escriba un número correspondiente      
        Caso contrario, si no tiene punto la entrada del usuario, será un entero, 
        si da error, se le avisará que escriba un número correspondiente.
        
        Una vez que el usuario ingreso un eje, se le dirá que puede no escribir más ejes escribiendo "salir" para pasar a la sección
        de eje X.

        - Eje X: El usuario se le dará la opción si escribir los ejes X o no, si no lo quiere, los ejes X serán los índices de 
        los elementos de Y. Caso contrario, el usuario tendrá que escribir uno por uno los ejes que pueden ser enteros o flotantes, 
        si escribe otra cosa imprimirá que tiene que elegir los números adecuados.
        
        El usuario solo puede escribir el total de ejes Y. Una vez que el usuario haya escrito los ejes, se abrirá el gráfico.

    """
    
    def PPT(self):
        print("\n/////   Piedra   /   Papel  /    Tijera   /////\n")
        opciones = ["Piedra", "Papel", "Tijera"]
        
        # Computadora
        bot = random.choice(opciones)
        
        # Usuario
        while True:
            user = input("Escoja entre Piedra / Papel / Tijera: ").replace(" ", "").capitalize()
 
            if user in opciones:
                break

        # Match
        if user == bot:
            print(f"\nBot: {bot} / Usuario: {user} -> ¡Es empate!\n")
        else:
            if (user == "Piedra" and bot == "Tijera") or (user == "Tijera" and bot == "Papel") or (user == "Papel" and bot == "Piedra"):
                print(f"\nBot: {bot} / Usuario: {user} -> ¡Gana el usuario!\n")                    
            else:
                print(f"\nBot: {bot} / Usuario: {user} -> ¡Gana el bot!\n")      


    def num_random(self):
        print("\n¡Adivina el número del bot! El rango de números: 1 - 5\n")
        
        # Número computadora
        bot = random.randint(1, 5)
        
        # Número usuario
        while True:
            user = input("Ingrese su número: ")
            
            try:
                user = int(user)
            except ValueError:
                pass

            if user in [1, 2, 3, 4, 5]:
                break           
            else:
                print("\nError: Ingrese un número entero del 1 al 5")

        # Match
        if user == bot:
            print(f"\nBot: {bot} / Usuario: {user} -> ¡Número adivinado!")
        else:
            print(f"\nBot: {bot} / Usuario: {user} -> ¡Número no adivinado!")

    
    def dado(self):
        cara = random.choice([1, 2, 3, 4, 5, 6])
        print(f"\nTiraste el dado... ¡La cara del dado es: {cara}!\n")

    
    def grafico(self):
        print("\nCreación de una función gráfica:")
        print("Escriba el eje de Y / Al terminar, escriba salir.\n")

        # Eje Y
        y = []
        while True:                
            if len(y) > 1:
                eje_y = input("Ingrese un eje de Y o salir: ") 
            else:   
                eje_y = input("Ingrese un eje de Y: ")
            
            if eje_y == "salir":
                break
            else:          
                if "." in eje_y:
                    try:
                        y.append(float(eje_y))
                    except ValueError:
                        print("Error: Ingrese un número entero (1) o flotante (1.5) ")

                else:
                    try:
                        y.append(int(eje_y))
                    except ValueError:
                        print("Error: Ingrese un número entero (1) o flotante (1.5)")

        # Eje X
        validacion_x = input("Quiere agregar ejes X? S/N: ").upper()
        
        if len(y) == 0:
            print("Ningún eje ingresado.")
        else:
            if validacion_x == "S":
                print(f"Escriba {len(y)} ejes de X")
                
                x = []
                while True:
                    if len(x) == len(y):
                        break
                    else:
                        eje_x = input("Ingrese un eje de X: ")

                    if "." in eje_x:
                        x.append(float(eje_x))
                    else:
                        try:
                            x.append(int(eje_x))
                        except ValueError:
                            print("Error: Ingrese un número entero (1) o flotante (1.5)")
                    
                # Gráfica X / Y
                print("Función gráfica creada.")
                
                plt.plot(x, y)
                plt.title("Función Gráfica")
                plt.show()

            else:
                # Gráfica Y
                print("Función gráfica creada.")
                
                plt.plot(y)
                plt.title("Función Gráfica")
                plt.show()
usuario = Juegos()
menu()

# Usuario escoje el método de la clase
while True:
    try:
        user = int(input("\nEscriba un número: "))
    except ValueError:
        print("Ingrese un número entero")
    
    if (user > 4) or (user < 1):
        print("Número fuera de rango: Ingrese un número del 1 al 4")
    else:
        break
if user == 1:
    usuario.PPT()
elif user == 2:
    usuario.num_random()
elif user == 3:
    usuario.dado()
elif user == 4:
    usuario.grafico()
else:
    print("\nNúmero fuera de rango: Ingrese un número del 1 al 4")
    user



