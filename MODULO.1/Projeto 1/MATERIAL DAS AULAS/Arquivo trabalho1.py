#Salário mensal
salario_mensal=1500
print("Salário Mensal: R$", salario_mensal)

#Reajuste de 50%
ajuste_50=1.5

#Novo Salário com Reajuste
reajuste=salario_mensal*ajuste_50
reajuste_valor=salario_mensal*0.5
print("Novo Salário com Reajuste: R$", reajuste)
print("Valor do aumento do Reajuste: R$", reajuste_valor)


a= int(input("Digite o primeiro Valor: "))
b= int(input("Digite o segundo valor: "))

resultado = a+b
print("resultado da soma:", resultado)

enter_user = input("Digite uma mensagem:")


while True: 
    print(f"Voce acabou de digitar:{enter_user}")
    enter_user = input("Digite uma mensagem ou digite sair:")
    if enter_user == "sair":
        break