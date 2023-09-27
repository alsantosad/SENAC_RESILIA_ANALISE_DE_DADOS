import os
import time


# Tela de apresentação do nosso chat bot
def apresentacao():
    '''Aqui temos a funcão de apresentação. Monstamos um quadro com 
    strings multiplicadas para um design melhor do aplicativo.'''
    os.system('cls')
    print("-" * 40)
    saudacao = "\n " + "~" * 3 + "  O MELHOR SANDUÍCHE DA CIDADE  " + "~" * 3
    print("~" * 8, "BEM VINDO AO SANDUREI", "~" * 8, saudacao)
    print("-" * 40)

# Aqui temos os nossos menus com as opcoes para nossos Clientes

def menu1():  # Essa função serve para apresentar os primeiros menus e os submenus.
    # utilizamos o loop de repetiçao while e tambem as condicionais if para
    # estruturar melhor onosso codigo e tambem para ser facil de ser lido.

    # Temos aqui as variáveis apresentando nosso
    opcao = "0"
    sanduiche = ""
    bebida = ""
    pagamento = ""

    while opcao != "5": # Iniciamos o nosso menu com o Loop while, para sempre retornar aqui se o cliente ainda não terminou o atendimento dele.
        os.system('cls')
        print("É um prazer " + nome, "vamos continuar com o seu atendimento!")
        time.sleep(1)
        print("1. Escolha seu Sanduiche. \n2. Escolha sua Bebida. \n3. Qual a Forma de Pagamento? \n4. Finalizar Pedido. \n5. Sair")
        opcao = input("Qual opção deseja? ")

        if opcao == "5":
            os.system('cls')
            print("Muito Obrigado! Volte sempre.")
            time.sleep(0.5)
            break
        elif opcao == "4":
            os.system('cls')
            print("Montando o seu pedido.")
            time.sleep(0.5)
            os.system('cls')
            print("Montando o seu pedido..")
            time.sleep(0.5)
            os.system('cls')
            print("Montando o seu pedido...")
            time.sleep(0.9)
            os.system('cls')
            endereco(sanduiche, bebida, pagamento)
        elif opcao == "3":
            os.system('cls')
            print("1. Débito. \n2. Crédito. \n3. Pix. \n4. Dinheiro.")
            pagamento = input("Qual opção deseja? ")
            if pagamento == "1":
                pagamento = "Débito"
            elif pagamento == "2":
                pagamento = "Crédito"
            elif pagamento == "3":
                pagamento = "Pix"
            elif pagamento == "4":
                pagamento = "Dinheiro"
            else:
                os.system('cls')
                print("Opção inválida, digite corretamente.")
        elif opcao == "2":
            os.system('cls')
            print("1. Suco de limão \n2. Suco de limão com morango \n3. Coca cola")
            bebida = input("Qual opção deseja? ")
            if bebida == "1":
                bebida = "Suco de Limão"
            elif bebida == "2":
                bebida = "Suco de Limão com Morango"
            elif bebida == "3":
                bebida = "Coca Cola"
            else:
                print("Opção inválida, digite corretamente.")
                time.sleep(0.5)
        elif opcao == "1":
            os.system('cls')
            print("1. Sanduiche de Carne Assada com Gorgonzola,\nBacon, Queijo e Cream Cheese na Baguete Australiana\n \n2. Sanduiche de Carne Assada com Gorgonzola, \nBacon, Queijo e Cream Cheese na Baguete Australiana\n \n3. Sanduiche de Salmão com Picles de Cebola Roxa, \nQueijo e Cream Cheese na Baguete Ciabatta\n")
            sanduiche = input("Qual opção deseja? ")
            if sanduiche == "1":
                sanduiche = "Sanduiche de Carne Assada com Gorgonzola, Bacon, \nQueijo e Cream Cheese na Baguete Australiana"
            elif sanduiche == "2":
                sanduiche = "Sanduiche de Pernil com Abacaxi Agridoce, Bacon, \nQueijo e Cream Cheese na Baguete de Brioche"
            elif sanduiche == "3":
                sanduiche = "Sanduiche de Salmão com Picles de Cebola Roxa, \nQueijo e Cream Cheese na Baguete Ciabatta"
            else:
                print("Opção inválida, digite corretamente.")
        else:

            print("Opção inválida, selecione as opções.")

# Apos finalizar o pedido, pedimos o endereco para então finalizarmos o pedido
def endereco(sanduiche, bebida, pagamento):
    '''Trazemos as variaveis 'sanduiche', 'bebida' e 'pagamento' para encaminhar para o fechamento
    junto com as novas variaveis, 'endereco1', 'bairro' e 'referencia' para então apresentarmos 
    na funcao fechamento'''
    print("Agora precisamos saber o seu endereço.")
    endereco1 = input("Qual o seu endereço? ")
    bairro = input("Qual o seu Bairro? ")
    referencia = input("Qual o Ponto de Referencia? ")
    os.system('cls')
    print("Finalizando o seu pedido.")
    time.sleep(0.5)
    os.system('cls')
    print("Finalizando o seu pedido..")
    time.sleep(0.5)
    os.system('cls')
    print("Finalizando o seu pedido...")
    time.sleep(0.9)
    os.system('cls')
    fechamento(endereco1, bairro, referencia, sanduiche, bebida, pagamento) #

# Apos coletarmos o endereço, apresentamos o pedido completo para o cliente conferir.
def fechamento(endereco1, bairro, referencia, sanduiche, bebida, pagamento):
    '''Com todas as nossas informações reunidas, nesta funcao nos apresentamos 
    tudo que foi salvo nas variaveis até agora para o cliente conferir se esta
    tudo conforme foi selecionado para finalizar o pedido.'''
    os.system('cls')
    print(f"Nome: {nome}")
    print(f"Endereço: {endereco1}\nBairro: {bairro}\nReferencia: {referencia}")
    print(f"Sanduíche: {sanduiche}")
    print(f"Bebida: {bebida}")
    print(f"Forma de Pagamento: {pagamento}")
    finalizar = input("Correto?[s/n] ")
    if finalizar == "s":
            print("Pedido feito com Sucesso.")
            print("\n"*2)
    elif finalizar == "n":
        menu1() # Ao selecionar o não, retornamos para o primeiro menu novamente
    else:
        print("Opção inválida, Digite corretamente")
        return


# Inicio do nosso chat Bot
apresentacao()
nome = input("Seja bem vindo! Qual o seu nome? ")
menu1()
