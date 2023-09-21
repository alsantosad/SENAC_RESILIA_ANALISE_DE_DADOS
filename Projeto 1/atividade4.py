# Solicita ao usuário a quantidade de números a serem somados
quantidade_numeros = int(input("Digite a quantidade de números que você deseja somar: "))

# Inicializa a variável de soma com zero
soma = 0

# Criando um loop para obter os números e somá-los
for i in range(quantidade_numeros):
    numero = float(input(f"Digite o número {i + 1}: "))
    soma += numero

# Exibe o resultado da soma
print(f"A soma dos {quantidade_numeros} números é igual a: {soma}")