import threading
from agent.concrete_agent import ConcreteAgent
from handlers.hello_handler import hello_handler
from handlers.crypto_handler import crypto_handler
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def main():
    # Initialize agent with environment variables
    agent = ConcreteAgent(
        ethereum_provider=os.getenv("ETHEREUM_PROVIDER"),
        wallet_address=os.getenv("WALLET_ADDRESS"),
        private_key=os.getenv("PRIVATE_KEY"),
        token_contract_address=os.getenv("TOKEN_CONTRACT_ADDRESS")
    )

    # Register handlers
    agent.register_handler("hello", lambda msg: hello_handler(agent, msg))
    agent.register_handler("crypto", lambda msg: crypto_handler(agent, msg))

    # Start agent behaviors in separate threads
    threading.Thread(target=agent.run_behaviors, daemon=True).start()
    threading.Thread(target=agent.process_messages, daemon=True).start()

    # Keep the main thread alive
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()
