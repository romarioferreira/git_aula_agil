import random




display_messages = [
    "seja feliz",
    "fique tranquilo",
    "tudo vai acabar bem"
    "não mataras",
    "não roubaras"
]


while True:
    resposta = input("deseja receber um concelho? S/N")
    if (resposta == "S" or resposta == "s"):
        mensagem = random.choice(display_messages)
        print(mensagem)
        print()









if __name__ == '__main__':
    print_hi('PyCharm')
