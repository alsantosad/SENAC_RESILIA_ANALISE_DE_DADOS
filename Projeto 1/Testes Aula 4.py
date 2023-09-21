
# Teste 1
nota1 = float(input("Informe sua nota: "))
if nota1 >= 7:
    print("Aprovado")
else:
    print("Reprovado")

#Teste 2
x = int(input("Digite um Número: "))
resultado = x % 2
if resultado == 0:
    print("Numero é Par")
else:
    print("Número é par")

# Teste 3
y = float(input("Digite um número: "))

if y >= 7:
    print("Aprovado")
elif y >=4:
    print("Prova Final")
else:
    print("Reprovado")

# Atividade 1 
# Na próxima black friday quero comprar uma televisão, mas tenho algumas limitações e restrições. São elas:
# A TV deve ter no mínimo 32 polegadas;
# A TV deve custar no máximo R$1900,00.

#Compra na Black Friday
valor_maximo_tv = 1900
tv = 1700
polegada_tv = 32
if valor_tv <= valor_maximo_tv and polegada_tv <=32:
    print("Posso Comprar essa TV!")




# Atividade 2 É febre?
# Implementar um detector de febre.
# Criar um arquivo termometro.py
# Declarar uma variável chamada temperatura com os valores: 36.5, 38, 99.
# Utilizando if e else, exibir na tela: “Você está com febre” quando a temperatura formaior que 38 graus e “Nada de febre” caso contrário
# Avaliar os resultados obtidos
# Compartilhar as etapas, os resultados e as dificuldades enfrentadas pelo grupo, com a turma.



# Atividade 3
# Implementar um programa (algoritmo) que analisa a diferença de preço nos alimentos de uma semana para outra em uma feira.
# Utilize 3 variáveis:
# Uma terá o nome dos alimentos (tomate, laranja, abacaxi e limão)
# Uma terá o valor do alimento na semana anterior
# Uma terá o valor do alimento na semana atual
# Caso um aumento de preço tenha ocorrido, sua aplicação deve exibir: “O <alimento> aumentou: <aumento> reais”
# Caso uma diminuição de preço tenha ocorrido, sua aplicação deve exibir: “O <alimento> diminuiu: <diminuição> reais”