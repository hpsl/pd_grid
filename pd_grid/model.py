import mesa

from .agent import PDAgent

class PdGrid(mesa.Model):
    """Model class for iterated, spatial prisoner's dilemma model."""

    schedule_types = {
        "Sequential": mesa.time.BaseScheduler,
        "Random": mesa.time.RandomActivation,
        "Simultaneous": mesa.time.SimultaneousActivation,
    }

    # This dictionary holds the payoff for this agent,
    # keyed on: (my_move, other_move)

    payoff = {("C", "C"): 1, ("C", "D"): 0, ("D", "C"): 3, ("D", "D"): 0}
    # os números iniciais foram definidos pelos criterios de
    # a) razoabilidade econômica e
    # b) compatibilidade com valores razoáveis para a matriz de payoff no caso de defecção ("D","C)
    receita_adicional_certificados = 200000
    custo_fixo_certificadora = 6250000
    custo_variavel_unitario_certificacao = 75000


    def __init__(
            self, width=50, height=50, schedule_type="Random", cooperadores_iniciais=100.0, payoffs=None, seed=None,
    ):
        """
        Create a new Spatial Prisoners' Dilemma Model.

        Args:
            width, height: Grid size. There will be one agent per grid cell.
            schedule_type: Can be "Sequential", "Random", or "Simultaneous".
                           Determines the agent activation regime.
            payoffs: (optional) Dictionary of (move, neighbor_move) payoffs.
        """
        self.cooperadores_iniciais = cooperadores_iniciais
        self.grid = mesa.space.SingleGrid(width, height, torus=True)
        self.schedule_type = schedule_type
        self.schedule = self.schedule_types[self.schedule_type](self)

        # Create agents
        for x in range(width):
            for y in range(height):
                predisposicao_cooperar=self.cooperadores_iniciais/(width*height)
                agent = PDAgent((x, y), self, None, predisposicao_cooperar)
                self.grid.place_agent(agent, (x, y))
                self.schedule.add(agent)


        self.datacollector = mesa.DataCollector(
            {
                "Cooperating_Agents": lambda m: len(
                    [a for a in m.schedule.agents if a.move == "C"]
                ),
                "Maior_Score_Agentes": lambda m: max(
                    a.score for a in m.schedule.agents
                ),
                "Menor_Score_Agentes": lambda m: min(
                    a.score for a in m.schedule.agents
                ),
                "Diferenca_Score_Agentes": lambda m: max(
                    a.score for a in m.schedule.agents
                ) - min(
                    a.score for a in m.schedule.agents
                )
            }
            # visa a avaliar a hipótese causal: número de cooperadores iniciais -> diferença de desempenho entre os agentes
        )

        self.running = True
        self.datacollector.collect(self)

    def step(self):
        # atualiza a cada passo a predisposição ao comportamento oportunista - i.e, nao certificar a própria producao quando os vizinhos certificam, ou ("D", "C")
        # essa predisposicao equivale à vantagem relativa de não certificar e lucrar a receita total vs.certificar e lucrar apenas a receita MENOS o custo de certificacao
        # onde o custo de certificação equivale ao custo variável unitário (para cada projeto, portanto, não muda: consultores, imagem aérea, etc)
        # MAIS o custo fixo unitário (custo fixo total da certificadora dividido pelo total de projetos certificados pelos agentes)
        # ou, matematicamente, predisposicao ao oportunismo = Receita/(Receita-(CustoFixo/num. de Certificados)-CustoVar)
        # como o custo de certificacao cai com o aumento de agentes certificados, a tentação de desistir é maior para os primeiros que certificam (pois incorrem em custo + alto)
        cooperating_agents = lambda m: len([a for a in m.schedule.agents if a.move == "C"])
        self.payoff[("D", "C")] = self.receita_adicional_certificados/(self.receita_adicional_certificados-(self.custo_fixo_certificadora/(cooperating_agents(self)+100))-self.custo_variavel_unitario_certificacao)
        self.schedule.step()
        # collect data
        self.datacollector.collect(self)


    def run(self, n):
        """Run the model for n steps."""
        for _ in range(n):
            self.step()
