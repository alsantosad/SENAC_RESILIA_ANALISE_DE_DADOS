# Recebe um número positivo do usuário
numero = int(input("Digite um número positivo: "))

# Verifica se o número é positivo
if numero < 0:
    print("Por favor, digite um número positivo.")
else:
    # Inicializa a variável de contagem com o número inserido
    contador = numero

    # Inicia o loop while
    while contador >= 0:
        # Exibe o número atual da sequência
        print(contador)
        
        # Decrementa o contador em 1 para a próxima iteração
        contador -= 1
