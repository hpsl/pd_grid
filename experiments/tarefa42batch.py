from mesa import *
from pd_grid.model import PdGrid
import numpy as np

# definição das variáveis dos experimentos
# que serão controladas (valor fixo) ou manipuladas:
# 1 - como modos de ativação dos agentes, foram utilizadas apenas a ativação aleatória e simultânea têm significado econômico
# respectivamente, grosso modo, racionalidade limitada vs. racionalidade ilimitada ou substantiva
# no primeiro caso, livre mercado sem instrumentos de informação, coordenação e governança públicos ou do 3o setor
# no segundo caso, perfeita informação e capacidade de processamentos instantâea e sem erros pelos agentes -
# condições que podem ser dadas de modo aproximada pelo regulador
# 2 - o número de cooperadores iniciais é variável independente, que variará de 0 a 2500 (nenhum a todos)

params = {
    "schedule_type": ("Random", "Simultaneous"),
    "cooperadores_iniciais": np.arange(start=0, stop=2501, step=250),
}

# define a quantidade de experimentos
# que serão repetidos para cada configuração de valores
# para as variáveis (de controle e independentes)
experiments_per_parameter_configuration = 10

# quantidade estimada, com base na tarefa 4.1, de passos suficientes para que a simulação
# alcance um estado de equilíbrio (steady state)
max_steps_per_simulation = 50

results = batch_run(
    PdGrid,
    parameters=params,
    iterations=experiments_per_parameter_configuration,
    max_steps=max_steps_per_simulation,
    number_processes=1,
    data_collection_period=-1,
    display_progress=True,
)

import pandas as pd

results_df = pd.DataFrame(results)

# gera uma string com data e hora
from datetime import datetime
now = str(datetime.now()).replace(":","-").replace(" ","-")

# define um prefixo para o nome do arquivo que vai guardar os dados do modelo
# contendo alguns dados dos experimentos
file_name_suffix =  ("_iter_"+str(experiments_per_parameter_configuration)+
                     "_steps_"+str(max_steps_per_simulation)+"_"+
                  now)

# define um prefixo para o nome para o arquivo de dados
model_name_preffix = "DilemaPrisioneiroCertificacao"

# define o nome do arquivo
file_name = model_name_preffix+"_model_data"+file_name_suffix+".csv"

results_df.to_csv(file_name)
