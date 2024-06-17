# Python-Sprint1

<h2>Descrição do Projeto</h2>
<p>Este projeto é uma simulação de pontuação do nosso jogo Formula-E Manager. O objetivo é permitir que o usuário escolha uma equipe e veja uma simulação da pontuação dessa equipe em comparação com outras equipes do que aconteceria em partes no nosso jogo. A pontuação de cada equipe é gerada de forma aleatória para criar uma experiência imprevisível e divertida.</p>

<h2>Instruções de Uso</h2>
<h3>Instalação:</h3>
<p>Certifique-se de ter o Python instalado em seu sistema.<br>Clone este repositório ou faça o download dos arquivos.</p>
<h3>Interação:</h3>
<p>O programa exibirá uma lista de equipes da Fórmula E.<br>
Você será solicitado a escolher uma equipe. Digite o nome da equipe conforme listado (não é sensível a maiúsculas/minúsculas).<br>
O programa então simulará as pontuações para todas as equipes e exibirá uma tabela com as pontuações.<br>
Será informado se sua equipe ganhou ou perdeu o campeonato com base na pontuação gerada.</p>

<h2>Requisitos</h2>
<p>Python<br>
Biblioteca padrão random</p>

<h2>Detalhes Técnicos</h2>
<p>Lista de Equipes: Uma lista contendo os nomes das equipes da Fórmula E é definida no início do código.<br>
Escolha da Equipe: O usuário escolhe uma equipe a partir das opções fornecidas.<br>
Simulação de Pontuação: As pontuações são geradas de forma aleatória usando a função random.randint(1, 100).<br>
Funções Principais:<br>
criarPontuacoes(): Gera uma lista de pontuações aleatórias para cada equipe.<br>
mostrarValores(seuTime): Mostra a tabela de pontuação e verifica se a equipe do usuário venceu.<br>
Verificação de Entrada: O programa verifica se a equipe escolhida pelo usuário é válida e pede uma nova escolha caso contrário.<br>
Ordenação e Exibição: As pontuações são ordenadas, e as equipes são embaralhadas para criar uma exibição aleatória mas ordenada da tabela de pontuação.</p>

<h2>Integrantes</h2>
<h3>Carlos Henrique Alves - 558003</h3>
<h3>Mauricio Alves - 556214</h3>
<h3>Vinícius Santos - 558218</h3>
<h3>Rodrigo Hiroshi - 557374</h3>
