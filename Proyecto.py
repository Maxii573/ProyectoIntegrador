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
        pass

    
    def dado(self):
        pass

    
    def grafico(self):
        pass    

usuario = Juegos()
