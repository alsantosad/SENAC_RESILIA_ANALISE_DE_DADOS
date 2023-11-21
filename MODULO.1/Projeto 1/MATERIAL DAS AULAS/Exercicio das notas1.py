# Identificação do aluno
identificacao_aluno = input("Digite um número de identificação? ")

# Informe as 3 notas do aluno
nota1 = float(input("Qual o resultado da primeira prova? "))
nota2 = float(input("Qual o resultado da segunda prova? "))
nota3 = float(input("Qual o resultado da terceira nota? "))

# Média das notas
me = float(input("Informe a média dos exercicios? "))

# Informar a média de aproveitamento
media_das_notas = (nota1 + nota2 * 2 + nota3 * 3 + me)/7

while media_das_notas > 0:
    if media_das_notas >= 9.0:
        resultado_final = "A"
    elif media_das_notas >= 7.5:
        resultado_final = "B"
    elif media_das_notas >= 6.0:
        resultado_final = "C"
    elif media_das_notas >= 4.0:
        resultado_final = "D"
    elif media_das_notas < 4.0:
        resultado_notas = "E"
    else:
        print("Inválido, digite o valor correto.")
        

print(f"Número de identificação do Aluno: {identificacao_aluno}")
print(f"O Conceito do Aluno é {resultado_final}")