# Atividade 2 É febre?
# Implementar um detector de febre.
# Criar um arquivo termometro.py
# Declarar uma variável chamada temperatura com os valores: 36.5, 38, 99.
# Utilizando if e else, exibir na tela: “Você está com febre” quando a temperatura formaior que 38 graus e “Nada de febre” caso contrário
# Avaliar os resultados obtidos
# Compartilhar as etapas, os resultados e as dificuldades enfrentadas pelo grupo, com a turma.

# Variaveis para Temperaturas
temperatura_normal = 36.5
temperatura_alta = 38
temperatura_torrada = 99

# Entrada de dados para o termometro
float(input("Qual a temperatura qe deu no termometro? "))

# funcionamento do Termometro
if temperatura_alta > temperatura_normal:
    print("Você esta com febre")
elif temperatura_alta < temperatura_torrada:
    print("Você está torrando")
else:
    print("Nada de Febre")