'''- Criar um novo arquivo .py.
1. Utilize o seguinte código em Python que guarda uma string:
str = 'X-DSPAM-Confidence:0.8475'
2. Use a função find e o fatiamento de strings para extrair a porção da string
depois do sinal de dois pontos, converta a string extraída em um número e
multiplique por 100. Exiba o resultado em tela.'''


'''str = 'X-DSPAM-Confidence:0.8475'
encontrar_indice = str.find('0.8475')
print(f"O elemento que procura está no indice {encontrar_indice}")
y = float(str[19:25])
a = (y*100)
print(a)'''









'''str = 'X-DSPAM-Confidence:0.8475' 
encontrar_indice = str.find('0')
print(f"O indice está a partir do {encontrar_indice}.")
indice_encontrado = float(str[19:25])
resultado = indice_encontrado*100
print(f"O resultado é {resultado}")'''







str = 'X-DSPAM-Confidence:0.8475'
achar_indice = str.find('0')
print(achar_indice)
indice_encontrado = str[19:25]
print("O tipo de indice encontrado é ", + type(indice_encontrado))
indice_encontrado = float(str[19:25])
