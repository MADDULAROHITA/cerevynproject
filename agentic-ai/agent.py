from planner import Planner
from tools import web_search, summarize
from memory import Memory
import json

class Agent:
    def __init__(self):
        self.planner = Planner()
        self.memory = Memory()

    def run(self, goal):
        plan = self.planner.create_plan(goal)

        for step in plan:
            self.memory.add_step(step)

            if "Search" in step:
                papers = web_search()
                self.memory.add_result(papers)

            if "Summarize" in step:
                summarized = []
                papers = self.memory.results[0]
                for p in papers:
                    summarized.append({
                        "title": p["title"],
                        "year": p["year"],
                        "summary": summarize(p)
                    })
                self.memory.add_result(summarized)

        final_output = self.memory.results[-1]
        with open("output.json", "w") as f:
            json.dump(final_output, f, indent=2)
        return final_output
