# Variáveis dos produtos com seus valores
fone_ouvido = 10
mouse = 25
teclado = 30

# Entrada de dados para saber qual produto o cliente quer.
print(f"1. Fone de ouvido = R$ {fone_ouvido}")
print(f"2. Mouse = R$ {mouse}")
print(f"3. Teclado = R$ {teclado}")
produto = float(input("Qual o valor do Produto? "))

# Criando uma condição para verificar a porcentagem
if produto < 20.00:
    margem_lucro = 0.45
else:
    margem_lucro = 0.30

# Dentro da condição, realize o cálculo necessário
lucro = produto * margem_lucro

# Imprima as informações para o usuário
print(f"Para um produto de R$ {produto}:")
print(f"Margem de lucro: {margem_lucro * 100}%")
print(f"Lucro estimado: R$ {lucro}")







produto = int(input("Qual o valor do produto? "))

if produto <=20:
    margem_lucro = 0.45
else:
    margem_lucro = 0.30

lucro = produto * margem_lucro

print(f"Lucro estimado: R$ {lucro}")