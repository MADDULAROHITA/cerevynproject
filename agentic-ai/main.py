from agent import Agent

if __name__ == "__main__":
    agent = Agent()
    goal = "Find the top 3 recent AI research papers on agriculture, summarize them, and store the output in a structured format."
    result = agent.run(goal)
    print(result)
