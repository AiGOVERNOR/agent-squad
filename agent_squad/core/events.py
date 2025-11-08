import asyncio

class EventBus:
    """A simple asynchronous event system."""

    def __init__(self):
        self.listeners = {}

    def on(self, event_name, callback):
        """Register a callback for an event."""
        if event_name not in self.listeners:
            self.listeners[event_name] = []
        self.listeners[event_name].append(callback)
        print(f"[EventBus] Registered listener for '{event_name}'")

    def subscribe(self, event_name, callback):
        """Alias for on() — allows calling subscribe() instead."""
        return self.on(event_name, callback)

    async def emit(self, event_name, **kwargs):
        """Emit an event asynchronously with arbitrary keyword data."""
        print(f"[EventBus] Emitting '{event_name}' with {kwargs}")
        for cb in self.listeners.get(event_name, []):
            if asyncio.iscoroutinefunction(cb):
                await cb(**kwargs)
            else:
                cb(**kwargs)

    async def publish(self, event_name, **kwargs):
        """Alias for emit() — allows calling publish() instead."""
        await self.emit(event_name, **kwargs)
