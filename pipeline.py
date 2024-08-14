class Pipeline:
    def __init__(self):
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def run(self):
        data = None
        for agent in self.agents:
            data = agent.run(data)
        return data
