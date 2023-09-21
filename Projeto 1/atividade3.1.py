produto = float(input("Qual o valor do produto? "))

if produto <=20:
    margem_lucro = 0.45
else:
    margem_lucro = 0.30

lucro = produto * margem_lucro

print("Lucro estimado: R$", lucro)
print("Para um produto de R$", produto)
print("Margem de lucro", margem_lucro * 100)
#print(f"Lucro estimado: R$ {lucro}")
#print(f"Para um produto de R$ {produto}:")
#print(f"Margem de lucro: {margem_lucro * 100}%")