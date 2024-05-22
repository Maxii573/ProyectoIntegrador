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



