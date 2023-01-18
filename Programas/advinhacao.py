import random

def jogo_advinhacao():

    print("\n*************************************")
    print("Bem-vinde ao Jogo de Advinhação! Wow!")
    print("*************************************\n")

    num_secreto = random.randrange(1, 101)
    num_tentativas = 0
    tentativa = 1
    pontos = 1000
    menu = 1

    while menu != 0:
        nivel = int(input("Qual o nível de dificuldade?\n1 - Fácil\n2 - Médio\n3 - Difícil\n"))

        if(nivel == 1):
            num_tentativas = 20
            menu = 0
        elif(nivel == 2):
            num_tentativas = 10
            menu = 0
        elif(nivel == 3):
            num_tentativas = 5
            menu = 0
        else:
            print("Digite o seu nível de dificuldade.\n")

    for tentativa in range(1, num_tentativas + 1):
        print(f"\nTentativa {tentativa} de {num_tentativas}:\n")
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou", chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        if(num_secreto == chute):
            print(f"Você acertou e fez {pontos} pontos!")
            break
        else:
            pontos_perdidos = abs((num_secreto - chute) * 4)
            pontos = pontos - pontos_perdidos
            if(num_secreto < chute):
                print("Seu chute foi maior que o número secreto!")
            elif(num_secreto > chute):
                print("Seu chute foi menor que o número secreto!")

    print(f"\nO número secreto era {num_secreto}!\nFim do jogo.")

if __name__ == "__main__":
    jogo_advinhacao()

