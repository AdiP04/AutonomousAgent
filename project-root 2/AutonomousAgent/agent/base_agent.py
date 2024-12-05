import time
import threading
from typing import Callable, Dict, List

class BaseAgent:
    def __init__(self):
        self.inbox = []
        self.outbox = []
        self.handlers: Dict[str, Callable] = {}
        self.behaviors: List[Callable] = []

    def register_handler(self, message_type: str, handler: Callable):
        self.handlers[message_type] = handler

    def add_behavior(self, behavior: Callable):
        self.behaviors.append(behavior)

    def receive_message(self, message: str):
        self.inbox.append(message)

    def process_messages(self):
        while True:
            if self.inbox:
                message = self.inbox.pop(0)
                message_type = message.split()[0]
                if message_type in self.handlers:
                    self.handlers[message_type](message)
            time.sleep(1)

    def run_behaviors(self):
        for behavior in self.behaviors:
            threading.Thread(target=behavior, daemon=True).start()