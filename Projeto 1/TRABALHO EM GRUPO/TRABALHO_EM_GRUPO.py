# Tela de apresentação do nosso chat bot
def apresentacao():
    '''Aqui temos a funcão de apresentação. Monstamos um quadro com 
    strings multiplicadas para um design melhor do aplicativo.'''
    print("-" * 40)
    saudacao = "\n " + "~" * 3 + "  O MELHOR SANDUÍCHE DA CIDADE  " + "~" * 3
    print("~" * 8, "BEM VINDO AO SANDUREI", "~" * 8, saudacao)
    print("-" * 40)

# Aqui temos os nossos menus com as opcoes para nossos Clientes


def menu1():
    ''' Essa função serve para apresentar os primeiros menus e os submenus.
utilizamos o loop de repetiçao while e tambem as condicionais if para estruturar melhor o
nosso codigo e tambem para ser facil de ser lido.'''

    opcao = 0
    sanduiche = ""
    bebida = ""
    pagamento = ""

    while opcao != "5":
        print("É um prazer " + nome, "vamos continuar com o seu atendimento!")
        print("1. Escolha seu Sanduiche. \n2. Escolha sua Bebida. \n3. Qual a Forma de Pagamento? \n4. Finalizar Pedido. \n5. Sair")
        opcao = input("Qual opção deseja? ")

        if opcao == "5":
            print("Muito Obrigado! Volte sempre.")
            break
        elif opcao == "4":
            print("\n" * 10)
            print("Finalizado...")
            endereco(sanduiche, bebida, pagamento)
        elif opcao == "3":
            print("\n" * 10)
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
                print("Opção inválida, digite corretamente.")
        elif opcao == "2":
            print("\n" * 10)
            print("1. Suco de limão. \n2. Suco de limão com morango. \n3. Coca cola")
            bebida = input("Qual opção deseja? ")
            if bebida == "1":
                bebida = "Suco de Limão"
            elif bebida == "2":
                bebida = "Suco de Limão com Morango"
            elif bebida == "3":
                bebida = "Coca Cola"
            else:
                print("Opção inválida, digite corretamente.")
        elif opcao == "1":
            print("\n" * 10)
            print(
                "1. Sanduiche de Carne Assada. \n2. Sanduiche de Pernil. \n3. Sanduiche de Rosbife")
            sanduiche = input("Qual opção deseja? ")
            if sanduiche == "1":
                sanduiche = "Sanduiche de Carne Assada"
            elif sanduiche == "2":
                sanduiche = "Sanduiche de Pernil"
            elif sanduiche == "3":
                sanduiche = "Sanduiche de Rosbife"
            else:
                print("Opção inválida, digite corretamente.")
        else:
            print("\n" * 10)
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
    print("Montando o seu pedido...")
    fechamento(endereco1, bairro, referencia, sanduiche, bebida, pagamento)

# Apos coletarmos o endereço, apresentamos o pedido completo para o cliente conferir.


def fechamento(endereco1, bairro, referencia, sanduiche, bebida, pagamento):
    '''Com todas as nossas informações reunidas, nesta funcao nos apresentamos 
    tudo que foi salvo nas variaveis até agora para o cliente conferir se esta
    tudo conforme foi selecionado para finalizar o pedido.'''
    print("\n"*10)
    print(f"Nome: {nome}")
    print(f"Endereço: {endereco1}\nBairro: {bairro}\nReferencia: {referencia}")
    print(f"Sanduíche: {sanduiche}")
    print(f"Bebida: {bebida}")
    print(f"Forma de Pagamento: {pagamento}")
    finalizar = input("Correto?[s/n] ")
    if finalizar == "s":
        print("\n"*10)
        print("Pedido feito com Sucesso.")
        print("\n"*2)
    elif finalizar == "n":
        menu1()
    else:
        print("Opção inválida, Digite corretamente")
        return


# Inicio do nosso chat Bot
apresentacao()
nome = input("Seja bem vindo! Qual o seu nome? ")
menu1()
