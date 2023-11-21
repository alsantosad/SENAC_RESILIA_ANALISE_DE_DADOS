# importa a função sleep
from time import sleep as sl
# início da execução do código
if __name__ == "__main__":
    # imprime uma apresentação para o usuário
    print("\nOlá!\
          \nSomos da empresa FGV e estamos realizando uma pesquisa nos bairros do Rio de Janeiro sobre as redes sociais:\nO tempo de uso, objetividade da utilização, e o impacto excessivo das redes sociais.\n")
    sl(2)
    print("\nGostaria de participar de uma pesquisa sobre o uso das redes sociais?\n")
    sl(1)
    # Exibe uma explicação sobre o funcionamento da pesquisa
    print("\nPara que possamos começar, vou te explicar as regras.\nI) Responda as perguntas apenas com o teclado numérico.\
              \nII) Caso não queira mais fazer o questionário, responda com '00' quando a idade for perguntada!\n")
    sl(1)
# Chama o módulo quiz, onde está a pesquisa em si
import quiz as qz
