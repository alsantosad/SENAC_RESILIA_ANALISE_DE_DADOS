# Importar as bibliotecas necessárias:
import pandas as pd
import datetime as dtt
from datetime import datetime as dt
from time import sleep as sl
#Contagem para definir quantas pessoas responderam o teste
contagem = 0
#
# Dicionários de perguntas e respostas:
# Perguntas
questoes =   {
    "Questão 1": "Você tem acesso a Internet?",
    "Questão 2": " De Acordo com Ricardo Saldanha, autor do livro 'Feliz Produtivo', recomenda-se utilizar as redes sociais por até 2 horas por dia,\
    \npara evitar problemas de saúde física e mental, como a fadiga ocular, dor de cabeça, sedentarismo, problemas de sono e até mesmo a\
    \ndependência tecnológica.\n\nVocê utiliza as redes sociais por mais de 2 horas?",
    "Questão 3": "Voce já trabalhou ou trabalha atualmente nas redes sociais como parte de sua atividade profissional?",
    "Questão 4": "Um estudo divulgado pela plataforma Cupom Válido, a grande maioria dos usuários utilizam as redes sociais para se manter atualizado \
    \ncom as notícias e novos acontecimentos (36,5%), encontrar conteúdo engraçado ou de entretenimento (35,0%) e preencher o tempo livre (34,4%).\
            \n\nDito isso, você também utiliza para essa finalidade?",
    "Questão 5": "De acordo com um levantamento do Sebrae, cada vez mais, os empreendedores no Estado do Rio de Janeiro utilizam redes sociais para seus negócios.\
        \n95% dos pequenos negócios estão no Instagram, 65% estão no Facebook, 28% no LinkedIn, 9% estão no YouTube.\
            \n\nVocê tem, ou utiliza alguma dessas redes para o seu negócio?",
    "Questão 6": "Você sente que pode ter alguns desses quadros clínicos? Ansiedade, depressão, transtorno de auto-imagem entre outros problemas?",
}
# Opções de resposta
respostas = {
    "1": "Sim",
    "2": "Não",
    "3": "Não sei responder / Talvez"
}
# Gêneros
genero_alternativas = { 
    "1" : "Homem Cis",
    "2" : "Mulher Cis",
    "3" : "Homem Trans",
    "4" : "Mulher Trans",
    "5" : "Não Binário",
}
# Dados dos testers
tester = {
}

#______FUNÇÃO DE EXPORTAÇÃO PARA .CSV________
def exportacao():
    df = pd.DataFrame(tester.values(), index=tester.keys(), columns=['Pessoa', 'Idade', 'Genero', 'Data e hora', 'Resposta 1', 'Resposta 2', 'Resposta 3', 'Resposta 4', 'Resposta 5', 'Resposta 6'])
    df.to_csv(path_or_buf='./arquivo.csv', index=False, sep=';')
#
#___________________________________LOOP PRINCIPAL___________________________________________________
while True:
    dadosTester = []
# Para iniciar o questionário, será solicitado ao usuário que informe a sua idade
    idade = input("Sua idade: ")
    sl(0.5)  #Sleep para aguardar o tempo definido em segundos
    #Se a resposta for 00, encerra o loop
    if idade == "00":
        print ("\nObrigado por participar do teste!\n")
        #Parte da exportação do arquivo 
        exportacao()
        break
    #Tratamento de dados pra que as respostas não estejam fora do padrão pedido
    try:
        idade = int(idade)
        if idade < 10 or idade > 99:
            print('\nIdade inválida. A idade deve estar entre 10 e 99.\n')
            continue  # Volta ao início do loop para pedir a idade novamente
        else:
            contagem += 1 # Aumentar 1 ao contador para identificar a pessoa entrevistada sem precisar de nome
            dadosTester.append(contagem)
            dadosTester.append(idade)  # Adicionar a idade já convertida para inteiro
            # Imprimir opções de gênero
            while True:
                for gk, gv in genero_alternativas.items():
                    print(f'{gk}: {gv}')
                genero = input("\nCom qual gênero você se identifica? \n")
                if genero not in genero_alternativas:
                    print('\nResposta inválida! Digite apenas uma das opções acima.')

                else:
                    #Se estiver de acordo, anexa a resposta à lista do tester
                    dadosTester.append(genero)
                    # Anotar a hora do começo das respostas para que seja registrada
                    horaResposta = dt.now()
                    hora_formatada = horaResposta.strftime('%d/%m/%Y %H:%M:%S')
                    dadosTester.append(hora_formatada)
                    for pk, pv in questoes.items():
                    # Um segundo loop para imprimir as questões e as opções de respostas
                        while True:
                            print(f'\n{pk}: {pv}\n')
                            sl(0.5)
                            for rk, rv in respostas.items():
                                print(f"{rk}: {rv}\n")
                                sl(0.5)
                            #Solicita a resposta
                            respostaUsuario = input("Sua resposta: ")
                            #Mensagem de erro caso não esteja dentro do esperado
                            if not respostaUsuario in respostas:
                                print("\n")
                                print("*"*50)
                                print(f'\nOpção inválida. Tente novamente.\n')
                                print("*"*50)
                            #Se estiver de acordo, anexa a resposta à lista do tester
                            else:
                                dadosTester.append(respostaUsuario)
                                print("\n")
                                print("*"*50)
                                break
                    break
    #Se estier errado, devolve o pedido de resposta correta e pede para que seja reinserida a resposta
    except ValueError:
        print('\nResposta inválida! Digite apenas números inteiros.')
    # Atribuir os dados ao dicionário de dados dos testers
    tester[contagem] = dadosTester
