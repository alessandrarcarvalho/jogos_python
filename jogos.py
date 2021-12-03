import forca #imports the game Forca
import adivinhacao #imports the game Adivinhacao

def escolhe_jogo(): #Creates the fuction to choose the game
    print("*"*35)
    print("Escolha o seu jogo")
    print("*"*35)

    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Qual jogo?"))  #the user chooses the game

    if (jogo == 1):
        print("Jogando FORCA")
        forca.jogar() #executes the game Forca
    elif (jogo == 2):
        print("Jogando ADIVINHAÇÃO")
        adivinhacao.jogar() #executes the game Adivinhacao
    print("*"*15)
    
    print("*"*15)

if (__name__ == "__main__"): #makes the program run only if it is the main program
    escolhe_jogo()

