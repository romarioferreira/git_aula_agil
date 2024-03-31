from messages import display_messages
import random
import time


time.sleep(2)

print("Starting project again in 3... 2... 1...")

while True:
    resposta = input("deseja receber um concelho? S/N")
    if (resposta == "S" or resposta == "s"):
        mensagem = random.choice(display_messages)
        print(mensagem)
        print()









if __name__ == '__main__':
    print_hi('PyCharm')
