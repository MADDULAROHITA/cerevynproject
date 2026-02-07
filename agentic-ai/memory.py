class Memory:
    def __init__(self):
        self.steps = []
        self.results = []

    def add_step(self, step):
        self.steps.append(step)

    def add_result(self, result):
        self.results.append(result)

    def get_memory(self):
        return {
            "steps": self.steps,
            "results": self.results
        }
