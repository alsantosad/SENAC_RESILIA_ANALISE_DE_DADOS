def vogal():
    resultado = input("Escreva qualquer caractere para sabermos se é ou não uma vogal: ")
    vogais = "AEIOUaeiou"  # Lista de vogais
    
    if resultado in vogais:
        print(f"{resultado} é uma vogal.")
    else:
        print(f"{resultado} não é uma vogal.")

vogal()