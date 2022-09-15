import mesa

from .portrayal import portrayPDAgent
from .model import PdGrid

# Make a world that is 50x50, on a 500x500 display.
canvas_element = mesa.visualization.CanvasGrid(portrayPDAgent, 50, 50, 500, 500)

model_params = {
    "height": 50,
    "width": 50,
    "schedule_type": mesa.visualization.Choice(
        "Scheduler type",
        value="Random",
        choices=list(PdGrid.schedule_types.keys()),
    ),
    "cooperadores_iniciais": mesa.visualization.Slider("Número inicial aprox. de certificadores", 0.0, 0.0, 2500.0, 10.0)
    # novo parâmetro acrescentado equivale à variável independente
}


chart_diferenca_agentes = mesa.visualization.ChartModule(
    [{
        "Label": "Maior_Score_Agentes",
        "Color": "#6C6CFF"
    },
    {
        "Label": "Menor_Score_Agentes",
        "Color": "#FF6C6C"
    },
    ],
    data_collector_name="datacollector"
)

chart_coooperating_agents = mesa.visualization.ChartModule(
    [{
        "Label": "Cooperating_Agents",
        "Color": "#6C6CFF"
    }
    ],
    data_collector_name="datacollector"
)

# novas visualizações visam a explorar a hipótese causal número de cooperadores iniciais -> diferença de desempenho entre os agentes
server = mesa.visualization.ModularServer(
    PdGrid, [canvas_element, chart_diferenca_agentes, chart_coooperating_agents], "Dilema do Prisioneiro em Certificação Socioambiental", model_params
)
