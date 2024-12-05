import threading
from agent.concrete_agent import ConcreteAgent
from handlers.hello_handler import hello_handler
from handlers.crypto_handler import crypto_handler
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    agent = ConcreteAgent(
        ethereum_provider=os.getenv("ETHEREUM_PROVIDER"),
        wallet_address=os.getenv("WALLET_ADDRESS"),
        private_key=os.getenv("PRIVATE_KEY"),
        token_contract_address=os.getenv("TOKEN_CONTRACT_ADDRESS")
    )

    # Register handlers
    agent.register_handler("hello", hello_handler)
    agent.register_handler("crypto", lambda msg: crypto_handler(agent, msg))

    # Add behaviors
    threading.Thread(target=agent.run_behaviors, daemon=True).start()
    threading.Thread(target=agent.process_messages, daemon=True).start()

    # Keep the main thread alive
    while True:
        pass

if __name__ == "__main__":
    main()