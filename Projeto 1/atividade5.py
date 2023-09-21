
numeros_divisiveis = []
for numero in range(2000, 3201):
    
    if numero % 7 == 0 and numero % 5 != 0:
        
        numeros_divisiveis.append(numero)
print("Números divisíveis por 7, mas não múltiplos de 5, entre 2000 e 3200:")
for numero in numeros_divisiveis:
    print(numero)