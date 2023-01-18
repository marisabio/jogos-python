import random

def jogo_forca():

    print("\n*************************************")
    print("   Bem-vinde ao Jogo de Forca! Wow!  ")
    print("*************************************\n")

    palavra_secreta = retornar_palavra()

    letras_acertadas = ["_" for letra in palavra_secreta]     
    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        
        chute = input("Chute uma letra:\n").strip().upper()

        if(chute in palavra_secreta):
            i = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[i] = letra
                i += 1
        else:
            erros += 1
        
        desenha_forca(erros)
        
        enforcou = letras_acertadas == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas, "\n")

    if(acertou):
        print("Você ganhou!!\n")
    else:
        print("Você perdeu...\n")

    print("Fim do jogo.")

def retornar_palavra():
    arquivo = open("Programas/palavras.txt", "r")
    palavras =[]

    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()

    num = random.randrange(0, len(palavras))
    palavra_secreta = palavras[num].upper()
    return palavra_secreta
    
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
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

if __name__ == "__main__":
    jogo_forca()

