sanduiches = [
    {"nome": "Sanduiche de Pernil", "preco": 25.0},
    {"nome": "Sanduiche de Carne Assada", "preco": 25.0},
    {"nome": "Sanduiche de Rosbife", "preco": 25.0},
]

bebidas = [
    {"nome": "Suco de Limão com Morango", "preco": 12.0},
    {"nome": "Suco de Limão", "preco": 10.0},
    {"nome": "Coca Cola", "preco": 6.0}
]

pagamento = [
    {"nome": "Dinheiro", "valor": 0},
    {"nome": "Credito", "valor": 0},
    {"nome": "Débito", "valor": 0},
    {"nome": "Pix", "valor": 0}
]

pedido = []

opcao = 0

def menu():
    print("Ações:")
    print("1. Adicionar sanduíche ao pedido")
    print("2. Bebidas")
    print("3. Formas de pagamento")
    print("4. Finalizar pedido")
    print("5. Sair")
    opcao = int(input("Escolha uma Opção? "))
    return opcao

while opcao != 5:
    opcao = menu()

    if opcao == 1:
        print("Menu de Sanduíches:")
        for i, sanduiche in enumerate(sanduiches, start=1):
            print(f"{i}. {sanduiche['nome']} - R$ {sanduiche['preco']}")
        
        escolha = int(input("Escolha o seu Sanduíche: "))
        if 1 <= escolha <= len(sanduiches):
            sanduiche_escolhido = sanduiches[escolha - 1]
            pedido.append(sanduiche_escolhido)
            print(f"{sanduiche_escolhido['nome']} adicionado ao pedido!")
        else:
            print("Opção inválida. Escolha um número válido.")
    elif opcao == 2:
        total = sum(item['preco'] for item in pedido)
        print("Pedido:")
        for item in pedido:
            print(f"{item['nome']} - R$ {item['preco']}")
        print(f"Total do pedido: R$ {total}")
    elif opcao == 3:
        print()
        total = sum(item['preco'] for item in pedido)
        print("Valor total:")


    elif opcao == 5:
        print("Obrigado por fazer seu pedido!")
    else:
        print("Opção inválida. Escolha uma opção válida.")