import asyncio

class NanobotAgent:
    """A simulation agent for nanoscale experiments."""

    def __init__(self, name, memory):
        self.name = name
        self.memory = memory
        print(f"[NanobotAgent] Initialized {self.name}")

    async def run(self, task, **kwargs):
        print(f"[{self.name}] Executing nanotech task: {task} with {kwargs}")
        await asyncio.sleep(1)  # simulate computation delay
        result = {
            "task": task,
            "status": "complete",
            "details": kwargs,
        }
        if hasattr(self.memory, "add"):
            self.memory.add(result)
        else:
            print("[NanobotAgent] Warning: memory has no 'add' method.")
        print(f"[{self.name}] Stored experiment result in memory.")
        return result

    def receive(self, message):
        print(f"[{self.name}] Received message: {message}")
