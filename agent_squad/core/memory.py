import json
import os

class Memory:
    """A persistent key-value memory store for agent communication."""

    def __init__(self, filename="memory_store.json"):
        self.filename = filename
        self.data = self._load()
        print("[Memory] Loaded existing memory store." if self.data else "[Memory] No existing memory found; starting new store.")

    def _load(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

    def recall(self, key, default=None):
        """Alias for get(), to make AI agents sound more human."""
        return self.get(key, default)

    def store(self, key, value):
        """Save a value in memory and persist it."""
        self.data[key] = value
        self._save()
        print(f"[Memory] Stored key '{key}'.")

    def add(self, value):
        """Append arbitrary entries (for logs or results)."""
        if "_log" not in self.data:
            self.data["_log"] = []
        self.data["_log"].append(value)
        self._save()
        print("[Memory] Added item to log.")

    def get(self, key, default=None):
        """Retrieve a stored value."""
        return self.data.get(key, default)

    def _save(self):
        try:
            with open(self.filename, "w") as f:
                json.dump(self.data, f, indent=2)
        except Exception as e:
            print(f"[Memory] Error saving memory: {e}")
