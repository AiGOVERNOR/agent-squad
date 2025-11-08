import json
import os

class Memory:
    """Persistent memory system using a local JSON file for storage."""

    def __init__(self, filename="memory_store.json"):
        self.filename = filename
        self.store_data = {}
        self._load()

    def _load(self):
        """Load existing data from disk if available."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    self.store_data = json.load(f)
                print(f"[Memory] Loaded {len(self.store_data)} records from {self.filename}")
            except Exception as e:
                print(f"[Memory] Failed to load existing memory: {e}")

    def _save(self):
        """Write memory to disk."""
        try:
            with open(self.filename, "w") as f:
                json.dump(self.store_data, f, indent=2)
        except Exception as e:
            print(f"[Memory] Save failed: {e}")

    def store(self, key, value):
        """Store information persistently."""
        self.store_data[key] = value
        self._save()
        print(f"[Memory] Stored key '{key}' -> saved to disk.")

    def recall(self, key, default=None):
        """Retrieve stored data."""
        value = self.store_data.get(key, default)
        print(f"[Memory] Recalled '{key}': {value}")
        return value

    def forget(self, key):
        """Forget a specific memory key."""
        if key in self.store_data:
            del self.store_data[key]
            self._save()
            print(f"[Memory] Forgot key '{key}' and updated disk.")

    def clear(self):
        """Erase everything from memory."""
        self.store_data.clear()
        self._save()
        print("[Memory] Cleared all records.")
