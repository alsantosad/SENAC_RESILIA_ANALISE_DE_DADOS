'''quantidade_pacientes = int(input("Digite a quantidade de pacientes: "))

# Loop para coletar os dados de cada paciente e calcular o IMC
for i in range(quantidade_pacientes):
    # Coleta os dados do paciente
    nome = input("Digite o nome do paciente: ")
    altura = float(input("Digite a altura do paciente (em metros): "))
    peso = float(input("Digite o peso do paciente (em quilogramas): "))
    
    # Calcula o IMC (Índice de Massa Corporal)
    imc = peso / (altura ** 2)
    
    # Imprime os dados do paciente e o IMC calculado
    print(f"Nome: {nome}")
    print(f"Altura: {altura} metros")
    print(f"Peso: {peso} quilogramas")
    print(f"IMC: {imc:.2f}")
    print()'''

quantidade_pacientes = int(input("Qual a quantidade de pacientes?"))

for i in range(quantidade_pacientes):
    nome = (str(input("Qual o nome do paciente? ")))
    altura = (float(input("Qual a altura? ")))
    peso = (float(input("Qual o seu peso?[Kg] ")))

    imc = peso / (altura ** 2)

    print(f"Nome: {nome}")
    print(f"Altura: {altura} metros")
    print(f"Peso: {peso} quilogramas")
    print(f"IMC: {imc:.2f}")
    print()
