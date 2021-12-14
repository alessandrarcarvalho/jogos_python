import random


def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = retorna_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    #Condições para início do jogo:

    enforcou = False
    acertou = False
    erros = 0
    tentativas = 7

    while (not enforcou and not acertou):
        
        chute = pede_chute()

        index = 0
        tentativas -= 1
        if chute in palavra_secreta:
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            print("Você errou. Tentativas restantes: {}".format(tentativas))
            desenha_forca(erros)
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
    if acertou:
        imprime_mensagem_vencendor()
    elif enforcou:
        imprime_mensagem_perdedor(palavra_secreta)


    print("*"*35)
    print("*"*11,"Fim de jogo","*"*11)
    print("*"*35)



def imprime_mensagem_abertura():
    print("*" * 35)
    print("Bem vindo ao jogo de Forca")
    print("*" * 35)

def carrega_palavra_secreta():
    # Abre o arquivo que contém as palavras e cria uma lista para elas
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()  # retira o \n
        palavras.append(linha)
    arquivo.close()
    print(palavras)

    # Escolhe de forma aleatória a palavra

    palavra_secreta = str(palavras[random.randrange(0, len(palavras))]).upper()
    return palavra_secreta

def retorna_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra?").strip().upper() #O usuário insere o chute
    return chute


def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = chute  # Preenche os espaços
            print(letras_acertadas)
        index += 1


def imprime_mensagem_vencendor():
    print("ACERTOU!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print(f'ENFORCOU! Palavra: {palavra_secreta}')
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if (__name__ == "__main__"): #makes the program run only if it is the main program
    jogar()