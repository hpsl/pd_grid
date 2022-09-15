# Dilema do prisioneiro demográfico aplicado à certificação ambiental

## Resumo

O modelo demográfico do dilema do prisioneiro disponibilizado no framework Python Mesa é uma variante do [Prisoner's Dilemma] descrito na Teoria dos Jogos, com a diferença principal de que cada jogador interage com todos os seus oito vizinhos imediatos em um grid geográfico. Cada agente pode Cooperar ou Desistir. A cada passo, o score de cada agente cresce para cada vizinho seu que "C"oopera, em maior ou menor grau segundo a matriz de payoff abaixo. Cada agente decide a cada passo reproduzindo a decisão do vizinho com maior score. 

Esta é uma adaptação do modelo, em que cada agente coopera ao "C"ertificar sua produção, incorrendo em um custo, que reduz o seu ganho de score (lucratividade relativa) no passo.

Quando os vizinhos certificam, a credibilidade da regularidade ambiental da produção na área circunvizinha  aumenta e a receita sobe proporcionalmente.

Quando os vizinhos certificam e o agente não, ele maximiza o seu ganho de score (lucratividade) naquele passo, por aumentar a sua receita sem custo.

Isso se reflete na matriz de payoff do modelo adaptado - semelhante ao do modelo do framework, mas *com a diferença crucial de um valor "D" dinâmico*:

|               | Certifica | Desiste |
|:-------------:|:---------:|:-------:|
| **Certifica** |   1, 1    |  0, D   |
|  **Desiste**  |   D, 0    |  0, 0   |

O valor *D* é o bônus de defecção, isto é, a vantagem econômica relativa do comportamento oportunista (de "trair" um vizinho cooperador, beneficiando-se sem cooperar). 

No framework, "D" era fixo em 1,6. Nesta adaptação, *D* é uma função lambda que traduz a relação Receita total / (Receita total - custo de certificação): métrica da atratividade econômica da "traição". Nos experimentos, variou entre 3,2 e menos de 1,5.

Como o custo de certificação cai com o aumento no número de agentes que certificam, a decisão de certificar é especialmente desvantajosa com poucos cooperadores e fica mais atrativa com o eventual alastramento da cooperação, diminuindo ainda mais a linearidade do comportamento da simulação e aumentando o seu realismo. 

A adaptação no código tambem incorporou a possibilidade de manipular o número inicial de cooperadores, como nova variável independente (no modelo original, eram fixos em ~50%).

Foram também acrescentadas visualizações, como novas possíveis variáveis dependentes, do número de cooperadores a cada passo e da comparação do maior e do menor scores dos agentes a cada passo.

Essa diferença de score traduz a heterogeneidade de desempenho dos agentes em decorrência do histórico da inter-relação das suas decisões com os vizinhos. Não poderia, portanto, ser descrita em uma função matemática agregada e abstrata, só se revelando graças à simulação multi-agente. 

Esses atributos são coletados para fins de experimentaçao em laboratório, demonstrada no arquivo batch neste diretório.

Merece destaque o fato de que o regime de ativação empregado revelou-se capaz de interagir de modos imprevisíveis com o número de cooperadores iniciais, de forma não-linear e altamente contra-intuitiva. 

Esta não era uma correlação detectável no modelo original do Mesa (com cooperadores iniciais e bônus "D" fixos), nem tampouco foi descrita na respectiva documentação ou em publicações correlatas. 

Aparentemente, trata-se, portanto, de um achado de pesquisa original, que merece um aprofundamento na simulação e nos experimentos para eventual publicação.

## Como executar 

##### Simulação do Modelo na Web

Para executar o modelo interativo, execute ``mesa runserver`` neste diretório.


## Arquivos

* ``run.py`` ponto de entrada da simulação interativa.
* ``pd_grid/``: contém as classes do modelo (model) e dos agentes (agent) classes; o modelo recebe como argumentos: 
* a string ``schedule_type``, que determina o modo de ativação dos agentes a cada passo: aleatório (Random) ou simultâneo (Simultaneous).
* o inteiro ``cooperadores_iniciais``: um número entre 0 e 2500, que determina o número inicial de agentes econômicos que optam por certificar a sua produção (comportamento cooperativo, ou "C").
* ``tarefa42batch.py``: o arquivo usado para disparar os experimentos na simulação, com diferentes combinações entre números iniciais de cooperadores e modos de ativação.

## Leituras suplementares



This model is adapted from:

Wilensky, U. (2002). NetLogo PD Basic Evolutionary model. http://ccl.northwestern.edu/netlogo/models/PDBasicEvolutionary. Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.

The Demographic Prisoner's Dilemma originates from:

[Epstein, J. Zones of Cooperation in Demographic Prisoner's Dilemma. 1998.](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.8.8629&rep=rep1&type=pdf)
