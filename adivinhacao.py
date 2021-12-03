
def jogar(): #creates the function to start the game

    print("*"*35)
    print("Bem vindo ao jogo de Adivinhação")
    print("*"*35)

    import random #imports the library random for generating random numbers

    numero_secreto = round(random.randrange(1,101)) #only int numbers between 1 and 100
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("1 - Fácil / 2 - Médio 3 / - Difícil")

    nivel = int(input('Defina o nível: ')) #the user needs to choose the the level of the game
    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    elif nivel == 3:
        total_de_tentativas = 5

    for rodada in range(1,total_de_tentativas+1): #loop that controls the amount of attempts
        print("Tentativa: {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite um número entre 1 e 100"))

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue #returns to the loop

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Parabéns, você acertou!")
            break
        else:
            if (maior):
                print("Você errou. O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou. O seu chute foi menor que o número secreto.")
            pontos = pontos - (abs(numero_secreto-chute)) #Subtracts lost points


        #else
    print(numero_secreto) #ends the game
    print("*"*15)
    print(f'Pontos: {pontos}')
    print("Fim de jogo")
    print("*"*15)

if (__name__ == "__main__"): #makes the program run only if it is the main program
    jogar()



