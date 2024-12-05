from agent.base_agent import BaseAgent
from web3 import Web3
import time
import random

class ConcreteAgent(BaseAgent):
    def __init__(self, ethereum_provider, wallet_address, private_key, token_contract_address):
        super().__init__()
        self.w3 = Web3(Web3.HTTPProvider(ethereum_provider))
        self.wallet_address = wallet_address
        self.private_key = private_key
        self.token_contract_address = token_contract_address

        self.add_behavior(self.generate_random_messages)
        self.add_behavior(self.check_balance)

    def generate_random_messages(self):
        words = ["hello", "crypto", "world", "space", "blockchain"]
        while True:
            message = f"{random.choice(words)} {random.choice(words)}"
            print(f"Generated Message: {message}")
            self.receive_message(message)
            time.sleep(2)

    def check_balance(self):
        while True:
            balance = self.w3.eth.get_balance(self.wallet_address)
            print(f"Balance for {self.wallet_address}: {self.w3.fromWei(balance, 'ether')} ETH")
            time.sleep(10)

    def transfer_token(self, target_address: str, amount: int):
        print(f"Transferring {amount} tokens to {target_address}")
        # Mock transaction - Add real transaction logic here.