import time
import random

def random_message_generator(agent):
    words = ["hello", "crypto", "world", "space", "blockchain"]
    while True:
        message = f"{random.choice(words)} {random.choice(words)}"
        agent.receive_message(message)
        time.sleep(2)