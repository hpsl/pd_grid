# 1) histogramas que comparam - para cada número inicial de cooperadores e para cada um dos dois possíveis modos de ativação no passo da simulação (Random ou Simultaneous) - as frequências de ocorrência de diferenças de score entre o agente mais e menos bem sucedido no passo final da simulação:

> hist(dataset$Diferenca_Score_Agentes[dataset$cooperadores_iniciais==0 & dataset$schedule_type=="Random"])

> hist(dataset$Diferenca_Score_Agentes[dataset$cooperadores_iniciais==250 & dataset$schedule_type=="Random"])

> hist(dataset$Diferenca_Score_Agentes[dataset$cooperadores_iniciais==500 & dataset$schedule_type=="Random"])

> hist(dataset$Diferenca_Score_Agentes[dataset$cooperadores_iniciais==750 & dataset$schedule_type=="Random"])

> hist(dataset$Diferenca_Score_Agentes[dataset$cooperadores_iniciais==1000 & dataset$schedule_type=="Random"])

> hist(dataset$Diferenca_Score_Agentes[dataset$cooperadores_iniciais==1250 & dataset$schedule_type=="Random"])

> hist(dataset$Diferenca_Score_Agentes[dataset$cooperadores_iniciais==1500 & dataset$schedule_type=="Random"])

> hist(dataset$Diferenca_Score_Agentes[dataset$cooperadores_iniciais==1750 & dataset$schedule_type=="Random"])

> hist(dataset$Diferenca_Score_Agentes[dataset$cooperadores_iniciais==2000 & dataset$schedule_type=="Random"])

> hist(dataset$Diferenca_Score_Agentes[dataset$cooperadores_iniciais==2250 & dataset$schedule_type=="Random"])

> hist(dataset$Diferenca_Score_Agentes[dataset$cooperadores_iniciais==2500 & dataset$schedule_type=="Random"])

> hist(dataset$Diferenca_Score_Agentes[dataset$cooperadores_iniciais==0 & dataset$schedule_type=="Simultaneous"]) 

> hist(dataset$Diferenca_Score_Agentes[dataset$cooperadores_iniciais==250 & dataset$schedule_type=="Simultaneous"])

> hist(dataset$Diferenca_Score_Agentes[dataset$cooperadores_iniciais==500 & dataset$schedule_type=="Simultaneous"])

> hist(dataset$Diferenca_Score_Agentes[dataset$cooperadores_iniciais==750 & dataset$schedule_type=="Simultaneous"])

> hist(dataset$Diferenca_Score_Agentes[dataset$cooperadores_iniciais==1000 & dataset$schedule_type=="Random"])

> hist(dataset$Diferenca_Score_Agentes[dataset$cooperadores_iniciais==1250 & dataset$schedule_type=="Random"])

> hist(dataset$Diferenca_Score_Agentes[dataset$cooperadores_iniciais==1500 & dataset$schedule_type=="Random"])

> hist(dataset$Diferenca_Score_Agentes[dataset$cooperadores_iniciais==1750 & dataset$schedule_type=="Random"])

> hist(dataset$Diferenca_Score_Agentes[dataset$cooperadores_iniciais==2000 & dataset$schedule_type=="Random"])

> hist(dataset$Diferenca_Score_Agentes[dataset$cooperadores_iniciais==2250 & dataset$schedule_type=="Random"])

> hist(dataset$Diferenca_Score_Agentes[dataset$cooperadores_iniciais==2500 & dataset$schedule_type=="Random"])



# 2) gráficos de barras que medem, nos resultados do batch, a prevalência de cooperação no passo final da simulação para diferentes números mínimos de cooperadores no passo inicial, comparando os modos de ativação "Random" (em economia evolucionária, semelhante a racionalidade limitada e ausência de coordenação) com Simultaneous (economicamente, aproxima-se da "racionalidade substantiva" neoclássica, com informação perfeita, possivelmente provida pelo regulador)


> dataset <- read.csv("DilemaPrisioneiroCertificacao_model_data_iter_100_steps_100_2022-09-13-23-21-16.471495.csv")

> View(dataset)

> random <- subset(dataset, dataset$schedule_type=="Random")

> CoopFinal.CoopInicial.Random <- aggregate(random$Cooperating_Agents,by=list(random$cooperadores_iniciais),FUN=sum)

> simultaneous <- subset(dataset, dataset$schedule_type=="Simultaneous")

> CoopFinal.CoopInicial.Simultaneous <- aggregate(simultaneous$Cooperating_Agents,by=list(simultaneous$cooperadores_iniciais),FUN=sum)

> barplot(CoopFinal.CoopInicial.Random$x, names=CoopFinal.CoopInicial.Random$Group.1)

> barplot(CoopFinal.CoopInicial.Simultaneous$x, names=CoopFinal.CoopInicial.Simultaneous$Group.1)


# 3) gráficos de barras que medem, nos resultados do batch, o score acumulado no passo final de todas as simulações para diferentes números mínimos de cooperadores no passo inicial, comparando os modos de ativação "Random" (em economia evolucionária, semelhante a racionalidade limitada e ausência de coordenação) com Simultaneous (economicamente, aproxima-se da "racionalidade substantiva" neoclássica, com informação perfeita, possivelmente provida pelo regulador)


> DiferencaScoreFinal.CoopInicial.Random <- aggregate(random$Diferenca_Score_Agentes,by=list(random$cooperadores_iniciais),FUN=sum)

> DiferencaScoreFinal.CoopInicial.Simultaneous <- aggregate(simultaneous$Diferenca_Score_Agentes,by=list(simultaneous$cooperadores_iniciais),FUN=sum)

> barplot(DiferencaScoreFinal.CoopInicial.Simultaneous$x, names=DiferencaScoreFinal.CoopInicial.Simultaneous$Group.1)

> barplot(DiferencaScoreFinal.CoopInicial.Random$x, names=DiferencaScoreFinal.CoopInicial.Random$Group.1)

