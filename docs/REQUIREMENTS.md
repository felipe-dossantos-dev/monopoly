# Banco Imobiliário

## Refatorando o texto
O objetivo dessa seção é separar o texto por conceito para ficar mais fácil de organizar os pensamentos para fazer o código

### Partidas
Numa partida desse jogo, os jogadores se alteram em rodadas, numa ordem definida aleatoriamente no começo da partida.
Os jogadores sempre começam uma partida com saldo de 300 para cada um. 
Um jogador que fica com saldo negativo perde o jogo, e não joga mais
Caso o jogo demore muito, como é de costume em jogos dessa natureza, o jogo termina na milésima rodada com a vitória do jogador com mais saldo. O critério de desempate é a ordem de turno dos jogadores nesta partida. 

### Jogadores
Os jogadores sempre começam uma partida com saldo de 300 para cada um. 
No começo da sua vez, o jogador joga um dado equiprovável de 6 faces que determina quantas espaços no tabuleiro o jogador vai andar. 

Cada um dos jogadores tem uma implementação de comportamento diferente, que dita as ações que eles vão tomar ao longo do jogo. Mais detalhes sobre o comportamento serão explicados mais à frente. 

Um jogador que fica com saldo negativo perde o jogo, e não joga mais

#### Tipos de jogadores
O jogador um é impulsivo; 
O jogador impulsivo compra qualquer propriedade sobre a qual ele parar. 

O jogador dois é exigente; 
O jogador exigente compra qualquer propriedade, desde que o valor do aluguel dela seja maior do que 50. 

O jogador três é cauteloso; 
O jogador cauteloso compra qualquer propriedade desde que ele tenha uma reserva de 80 saldo sobrando depois de realizada a compra. 

O jogador quatro é aleatório;
O jogador aleatório compra a propriedade que ele parar em cima com probabilidade de 50%. 


### Compra de propriedades
Jogadores só podem comprar propriedades caso ela não tenha dono e o jogador tenha o dinheiro da venda
Ao cair em uma propriedade sem proprietário, o jogador pode escolher entre comprar ou não a propriedade. Esse é a única forma pela qual uma propriedade pode ser comprada. Ao comprar uma propriedade, o jogador perde o dinheiro e ganha a posse da propriedade.
Quando o jogador sai do jogo ele perde suas propriedades e portanto podem ser compradas por qualquer outro jogador. 


### Rodada
No começo da sua vez, o jogador joga um dado equiprovável de 6 faces que determina quantas espaços no tabuleiro o jogador vai andar. 
Ao completar uma volta no tabuleiro, o jogador ganha 100 de saldo. 


### Propriedades
Cada propriedade tem um custo de venda e um valor de aluguel.
Pode ter de um proprietário.
Tem uma posição fixa no tabuleiro.
Tem um valor de aluguel,caso um proprietário caso já estejam compradas
Ao cair em uma propriedade sem proprietário, o jogador pode escolher entre comprar ou não a propriedade. Esse é a única forma pela qual uma propriedade pode ser comprada. 
Ao cair em uma propriedade que tem proprietário, ele deve pagar ao proprietário o valor do aluguel da propriedade. 
Quando o jogador sai do jogo ele perde suas propriedades e portanto podem ser compradas por qualquer outro jogador. 


### Tabuleiro
O tabuleiro tem uma ordem de propriedades.
Não é possível construir hotéis e nenhuma outra melhoria sobre as propriedades do tabuleiro, por simplicidade do problema.
Ao completar uma volta no tabuleiro, o jogador ganha 100 de saldo. 
tabuleiro é composto por 20 propriedades em sequência


## Saída 
Uma execução do programa proposto deve rodar 300 simulações, imprimindo no console os dados referentes às execuções. Esperamos encontrar nos dados as seguintes informações: 
Quantas partidas terminam portime out (1000 rodadas); 
Quantos turnos em média demora uma partida; 
Qual a porcentagem de vitórias por comportamento dos jogadores; 
Qual o comportamento que mais vence.