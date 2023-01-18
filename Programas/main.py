import advinhacao
import forca

def escolhe_jogo():

    print("Escolha o seu jogo!")

    menu = 1

    while menu != 0:
        opt = int(input("1 - Advinhação\n2 - Forca:\n"))

        if(opt == 1):
            advinhacao.jogo_advinhacao()
            menu = 0
        elif(opt == 2):
            forca.jogo_forca()
            menu = 0
        else:
            print("Digite o número do jogo!\n")

if __name__ == "__main__":
    escolhe_jogo()
