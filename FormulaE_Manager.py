import random 

equipes = ["MAHINDRA RACING","ABT CUPRA", "ANDRETTI", "DS PENSKE", "ENVISION RACING", "ERT FORMULA", "JAGUAR TCS", "MASERATI MSG", "NEOM MCLAREN", "NISSAN", "TAG HEUER PORSCHE"] 
#Lista 'equipes' com as equipes da Formula E disponiveis para escolha.
for i in equipes:
    print(i)
print()
#Loop para printar todas equipes no terminal, e print vazio para espacar uma linha na hora da mostragem da tabela.

seuTime = str(input("Escolha uma equipe das opcoes dadas:").upper())
pontosDoTime = random.randint(1,100)
#Perguntando a equipe escolhida e simulando a pontuacao de maneira aleatoria.

def criarPontuacoes():
    '''
    Funcao para criar as pontuacoes de cada equipe, um loop que itera sobre a quantidade 
    de equipes que tem na lista das equipes e assim cria uma lista com a pontuacao de 
    cada equipe e retorna essa lista para ser usada posteriormente.
    '''
    pontuacaoEquipe = []
    for k in range(len(equipes)):
        pontuacaoEquipe.append(random.randint(1,100))
        
    return pontuacaoEquipe


def mostrarValores(seuTime):
    '''
    Funcao para mostrar a tabela simulada da pontuacao de cada equipe na corrida,
    que leva como parametro o nome do time escolhido pelo usuario,
    '''
    pontos = criarPontuacoes()
    pontos.sort()
    random.shuffle(equipes)
    i = len(equipes) - 1
    '''Variavel pontos que armazena o retorno de uma lista da funcao "criarPontuacoes"
    em seguida a funcao .sort() para ordenar a ordem de pontuacao das equipes para 
    serem mostradas corretamente na tabela, uso a funcao (da biblioteca "random") .shuffle()
    para embaralhar a lista das equipes para ter uma simulacao adequadamente aleatoria e 
    a variavel "i" que armazena a quantidade de times que tem na lista de equipes.
    '''
    
    while seuTime not in equipes:
        """
        loop while para verificar se o time escolhido existe, e se nao existir perguntar 
        ao user o nome de uma equipe que exista na nossa lista
        """
        print("O time anteriormente escolhido nao existe!")
        seuTime = str(input("Escolha uma equipe das opcoes dadas:").upper())
    
    if pontosDoTime > pontos[-1]:
        print("Parabens ganhou o campeonato")
    else:
        print("Nao foi dessa vez, vc perdeu!")
    print(f"Sua pontuacao- {seuTime} = {pontosDoTime}")
    """
    Condicao para avaliar se a pontuacao do time do usuario foi
    a maior dentre todos os times
    """
        
    print("TABELA: ")
    while i > 0: 
        """
        loop while em ordem decrescente para mostrar a tabela do
        maior para o menor.
        """
        if equipes[i] != seuTime:
            print(f"{equipes[i]} = {pontos[i]}")
        else:
            pass
        
        i-=1
            

criarPontuacoes()
mostrarValores(seuTime)

#Chamando as funcoes para rodar o codigo e usando a variavel "seuTime" como parametro
# que como ja dito leva o nome do time escolhido pelo user