'''# Definindo uma função para calcular a média de três números
def calcular_media(num1, num2, num3):
    soma = num1 + num2 + num3
    media = soma / 3
    return media

# Solicitando três números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Chamando a função para calcular a média
resultado = calcular_media(numero1, numero2, numero3)

# Exibindo o resultado
print(f"A média dos números {numero1}, {numero2} e {numero3} é: {resultado:.2f}")'''

def maior_numero(valor1, valor2, valor3):
    maior = max(valor1, valor2, valor3)
    return maior

# Pedir 3 números para o usuário
valor1 = float(input("Digite o primeiro número: "))
valor2 = float(input("Digite o segundo número: "))
valor3 = float(input("Digite o terceiro número: "))

maior = maior_numero(valor1, valor2, valor3)

print(f"O maior número entre os números digitados é {maior}")