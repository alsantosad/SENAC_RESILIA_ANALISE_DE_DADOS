# Inicialize uma lista para armazenar as informações do pedido
pedidos = []

# Função para mostrar tudo o que foi feito no pedido
def mostrar_pedido():
    print(pedidos)

# Função para registrar um pedido
def registrar_pedido():
    pedido = input("Digite o seu pedido: ")
    pedidos.append(pedido)
    print("Pedido registrado com sucesso!")

# Função para atender pedidos
def atender_pedidos():
    if pedidos:
        print("Pedidos em espera:")
        for i, pedido in enumerate(pedidos, start=1):
            print(f"{i}. {pedido}")
        
        numero_pedido = int(input("Digite o número do pedido que deseja atender: "))
        
        if 1 <= numero_pedido <= len(pedidos):
            pedido_atendido = pedidos.pop(numero_pedido - 1)
            print(f"Você atendeu o pedido: {pedido_atendido}")
        else:
            print("Número de pedido inválido.")
    else:
        print("Não há pedidos em espera.")

# Loop principal para o sistema de atendimento em chat
while True or opcao <= str(5):
    print("\nOlá! Bem vindo ao Sandurei!" + "\nO melhor Sanduiche da Cidade!")
    print("\nOpções:")
    print("1. Registrar pedido")
    print("2. Atender pedidos")
    print("3. Rastrear Pedido")
    print("4. Resumo do Pedido")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        registrar_pedido()
    elif opcao == "2":
        atender_pedidos()
    elif opcao == "4":
        mostrar_pedido()
    elif opcao == "5":
        print("Encerrando o sistema de atendimento.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
