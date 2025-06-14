import datetime

class Memory:
    def __init__(self):
        self.session_memory = []
        self.log_path = "logs/sample_logs.txt"

    def store(self, entry: str):
        timestamped = f"[{datetime.datetime.now()}] {entry}"
        self.session_memory.append(timestamped)
        with open(self.log_path, "a") as f:
            f.write(timestamped + "\n")

    def recall(self):
        return self.session_memory
