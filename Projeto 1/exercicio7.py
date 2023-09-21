
'''dia = 'quarta' or 'sabado'
sabor_pizza = "marguerita"

if sabor_pizza == "marguerita" and dia == 'quarta' or dia == 'sabado':
    print("[PROMO]: Pizza em dobro!")
    print("Começando a fazer DUAS pizzas marguerita")'''

nota1 = float(input("Qual sua nota em matemática: "))
nota2 = float(input("Qual sua nota em português: "))
nota3 = float(input("Qual sua nota em Conhecimentos gerais: "))
Me = (nota1 + nota2 + nota3)/3
Ma = (nota1 + nota2 * 2 + nota3 * 3 + Me)/7
print(Ma)

if Ma < 4:
    print("Você obteve um conceito E. REPROVADO")
elif Ma > 4 and Ma < 6:
    print("Você obteve um conceito D. REPROVADO")
elif Ma > 6 and Ma < 7.5:
    print("Você obteve um conceito C. APROVADO")
elif Ma > 7.5 and Ma < 9:
    print("Você obteve um conceito C. APROVADO")
else:
    print("Você obteve um conceito A. APROVADO")