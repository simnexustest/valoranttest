import random

agents = [
    "Brimstone", "Viper", "Omen", "Killjoy", "Cypher", "Sage", "Sova", "Phoenix",
    "Jett", "Reyna", "Raze", "Breach", "Skye", "Yoru", "Astra", "KAY/O",
    "Chamber", "Neon", "Fade", "Harbor", "Gekko", "Deadlock"
]

banned_agents = []

def select_random_agent():
    available_agents = [agent for agent in agents if agent not in banned_agents]
    if not available_agents:
        print("All agents are banned. Resetting bans.")
        banned_agents.clear()
        available_agents = agents
    
    random_agent = random.choice(available_agents)
    return random_agent

while True:
    banned_agents_str = ', '.join(banned_agents) if banned_agents else "None"
    print(f"Banned agents: {banned_agents_str}")

    prompt = input("Type the name of an agent to ban, or type 'Y' to select a random agent, or 'n' to quit: ").strip()
    prompt_lower = prompt.lower()

    if prompt_lower == 'n':
        break
    elif prompt_lower == 'y':
        random_agent = select_random_agent()
        print(f"Randomly selected agent: {random_agent}")
    elif prompt_lower in [agent.lower() for agent in agents]:
        agent_to_ban = next(agent for agent in agents if agent.lower() == prompt_lower)
        if agent_to_ban not in banned_agents:
            banned_agents.append(agent_to_ban)
            print(f"{agent_to_ban} has been banned.")
        else:
            print(f"{agent_to_ban} is already banned.")
    else:
        print("Invalid input. Please try again.")
