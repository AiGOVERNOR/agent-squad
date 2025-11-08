from mcp.server.fastmcp import FastMCP
from agent_squad.agent_squad.core.memory import Memory

class AgentManager:
    def __init__(self):
        # Initialize FastMCP as the command core
        self.mcp = FastMCP()
        self.agents = {}
        self.memory = Memory()
        print("[Governor] Agent Manager initialized with persistent memory.")

    def register(self, name, agent):
        """Register an agent with the manager."""
        self.agents[name] = agent
        print(f"[Governor] Registered agent: {name}")

    def run(self, name, *args, **kwargs):
        """Run a registered agent by name."""
        if name in self.agents:
            print(f"[Governor] Running agent {name}")
            result =
