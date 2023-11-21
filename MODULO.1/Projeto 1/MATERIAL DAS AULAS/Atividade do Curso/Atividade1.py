# Atividade 1 
# Na próxima black friday quero comprar uma televisão, mas tenho algumas limitações e restrições. São elas:
# A TV deve ter no mínimo 32 polegadas;
# A TV deve custar no máximo R$1900,00.

#Compra na Black Friday
print("-"*20 + "Black Friday" + "-"*20)
print("HOJE TEMOS O LANÇAMENTO DAS NOSSAS SAMSUNG QLED")

# Variavel com o Valor maximo da tv
valor_tv = str(input("Qual o valor da TV Samsung QLED? R$"))

# Variavel com as polegadas minimas
polegada_tv = int(input("Quantas polegadas tem a TV Samsung QLED? "))
if valor_tv <= str("1900") and polegada_tv >= 32:
    print("Gloria ao Papai do Céu, Posso Comprar essa TV!")
else:
    print("Black friday sem Graça... Não vou comprar!")