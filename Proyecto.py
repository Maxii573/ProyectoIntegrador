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

    def PPT(self):
        print("\nPiedra   /   Papel  /    Tijera\n")
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
            print(f"\nBot: {bot} / Usuario: {user}\n¡Es empate!")
        else:
            if (user == "Piedra" and bot == "Tijera") or (user == "Tijera" and bot == "Papel") or (user == "Papel" and bot == "Piedra"):
                print(f"\nBot: {bot} / Usuario: {user}\n¡Gana el usuario!")
            else:
                print(f"\nBot: {bot} / Usuario: {user}\n¡Gana el bot!")      


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
                    print("\nError: Ingrese un número entero del 1 al 5")

            if user in [1, 2, 3, 4, 5]:
                break
            else:
                print("\nError: Ingrese un número entero del 1 al 5")

        # Match
        if user == bot:
            print(f"\n¡Número adivinado! Bot: {bot} / Usuario: {user}")
        else:
            print(f"\n¡Número no adivinado! Bot: {bot} / Usuario: {user}")

    
    def dado(self):
        cara = random.choice([1, 2, 3, 4, 5, 6])
        print(f"Tiraste el dado! La cara es: {cara}")

    
    def grafico(self):
        print("\nCreación de una función gráfica:")
        print("Escriba el eje de Y.\nAl terminar, escriba salir\n")

        # Eje Y
        y = []
        while True:
            eje_y = input("Ingrese un eje de Y: ")
            if eje_y == "salir":
                break
            else:          
                if "." in eje_y:
                    y.append(float(eje_y))

                else:
                    try:
                        y.append(int(eje_y))
                    except ValueError:
                        print("Error: Ingrese un número entero (1) o flotante (1.5)")

        # Eje X
        validacion_x = input("Quiere agregar ejes X? S/N: ").upper()

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
            plt.show()

        else:
            # Gráfica Y
            plt.plot(y)
            plt.show()
        

usuario = Juegos()
usuario.num_random()



