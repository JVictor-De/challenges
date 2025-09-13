# Crie um "jogo dos estados". Neste jogo, o jogador precisa responder
# o nome da capital de cada Estado do Brasil. O jogo deve perguntar
# ao usuário "Qual a capital do Estado X?", e checar se o usuário
# respondeu de forma correta. Após cada pergunta, o usuário pode escolher
# parar o jogo ou continuar para a próxima pergunta. Quando o usuário
# decidir parar, ou quando todas as perguntas forem respondidas,
# o código mostra o número bruto e porcentagem de acertos.


capitais = {"Acre": "Rio Branco"}


acertos = 0
erros = 0

print("Bem-vindo ao quiz de capitais do Brasil!")
def verificarResposta(acertos=0, erros=0):
    while True:
        for estado, capital in capitais.items():
            respost = input(f'Qual é a capital de {estado}?')
            if respost.strip().lower() == capital.lower():
                print("Você acertou seu miseravel!!!")
                acertos += 1
            else:
                print(f'"Eu sou o mais forte! Não há ninguém mais forte que eu!" A capital de {estado} é {capital}') # VEGETA
                erros += 1
            continuar = input("Quer continuar? (Sim ou Não) ")
            if continuar.strip().lower() == "não":
                break


        total = acertos + erros
        porcentagem = acertos / total 


        if porcentagem >= 0.7:
            print("Surpreendente. \n Parece que há um cérebro em você.")
            break

        else:
            print("'O fracasso é apenas a chance de começar de novo, com mais inteligência.- Henry Ford'.")
            continuar = input("quer continuar o treinamento? (Sim ou não) ")
            if continuar.strip().lower() == "não":
                break
            else:
                continue


verificarResposta()

