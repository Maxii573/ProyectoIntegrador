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
        user = input("Escoja el objeto: ")



        # Match
        if user == bot:
            print(f"\nBot: {bot} / Usuario: {user}\n¡Es empate!")
        else:
            if (user == "Piedra" and bot == "Tijera") or (user == "Tijera" and bot == "Papel") or (user == "Papel" and bot == "Piedra"):
                print(f"\nBot: {bot} / Usuario: {user}\n¡Gana el usuario!")
            else:
                print(f"\nBot: {bot} / Usuario: {user}\n¡Gana el bot!")      


    def num_random(self):
        print("¡Adivina el número del bot! El rango de números: 1 - 5\n")
        # Número computadora
        bot = random.randint(1, 5)
        
        # Número usuario
        user = int(input("Ingrese su número: "))

        # Match
        if user == bot:
            print(f"\n¡Número adivinado! Bot: {bot} / Usuario: {user}")
        else:
            print(f"\n¡Número no adivinado! Bot: {bot} / Usuario: {user}")

    
    def dado(self):
        cara = random.choice([1, 2, 3, 4, 5, 6])
        print(f"Tiraste el dado! La cara es: {cara}")

    
    def grafico(self):
        pass    

usuario = Juegos()
usuario.dado()