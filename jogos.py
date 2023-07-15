from forca import jogo_forca
from adivinhacao import jogo_adivinhacao

def jogar():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if jogo == 1:
        print("Jogando forca")
        jogo_forca()
    elif jogo == 2:
        print("Jogando adivinhação")
        jogo_adivinhacao()

if __name__ == "__main__":
    jogar()