# Estrutura de repetição, com entrada de dados do usuario, condições e finalização.

'''Leia a entrada com temperatura de um usuário até que ele digite sair.
Exiba na tela: “Você está com febre. Tome um remédio e repouse”
quando a temperatura estiver entre 38 e 39 graus; “Você está com febre.
Tome um remédio, procure um médico.” para qualquer temperatura acima disso; e “Nada de febre” caso contrário.'''



# Criamos a estrutura de repetição com as condicionais
while True:
    temperatura = float(input("Qual a temperatura deu no termometro? "))
    if temperatura > float(39):
        print("Você está com muita febre, tome um remédio e procure um médico")
    elif temperatura > float(37):
        print("você está com febre. Tome um Remédio e repouse")
    else:
        print("Nada de febre")

    resposta = str(input("Deseja medir novamente?[s/n] "))
    if resposta == "n":
        break
    elif resposta == "s":
        temperatura
    else:
        print("Inválido, digite novamente.")