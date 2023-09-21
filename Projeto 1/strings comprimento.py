'''# A função len retorna a quantidade de caracteres contidos em uma string, ou seja, seu comprimento.

sentenca = 'Está é uma string'
print(len(sentenca))'''

'''# Exercicio, inserir uma palavra e usar a sentenca len para contar os caracteres.
sentenca = input("Informe uma palavra para contarmos quantos caracteres tem? ")
print(len(sentenca))

# Strings percorrendo um laço
for i in range(len(sentenca)):
    print(sentenca[i])

for caractere in sentenca:
    print(caractere)'''

# String de segmentação - Slice
'''sentenca = 'Esta é uma string'
print(sentenca[0:5])'''


'''#O QUE FAZER?
Criar um novo arquivo .py.
1. Escreva um loop que inicia no último caractere da string e caminha para o
primeiro caractere, imprimindo cada letra em uma linha separada;
2. Dado que a variável sentenca é uma string, qual o resultado de sentenca[:]?
3. Teste alterar o valor de um caractere de uma string.
➔ COMO FAZER?
Em grupos (3-4 pessoas). Avalie com diferentes entradas e diferentes valores de slice.
➔ FECHAMENTO
Ouvir a linha de raciocínio e dúvida dos grupos.'''

'''caracteres = "Futuro analista Dev"
for i in range(len(caracteres)):
    print(caracteres[-i -1])

caracteres = "f" + caracteres[1:]
print(caracteres)'''

'''# Strings são imutáveis
nova_sentenca = 'Aquela' + sentenca[5:]
print(nova_sentenca)'''

sentenca = "Grandes poderes, grande responsabilidade"
nova_sent = "Aquela " + sentenca[5:]

'''for i in range(len(sentenca):
    print(sentenca[i])

for caractere in sentenca:
    print(caractere)'''

print(nova_sent)
print(sentenca.replace(" ","*"))
print(sentenca.lower())
print(sentenca.upper())
indice = nova_sent.find("poderes")
print(indice)