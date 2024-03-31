from messages import display_messages
import random

print("Starting project again")

while True:
    resposta = input("deseja receber um concelho? S/N")
    if (resposta == "S" or resposta == "s"):
        mensagem = random.choice(display_messages)
        print(mensagem)
        print()









if __name__ == '__main__':
    print_hi('PyCharm')
