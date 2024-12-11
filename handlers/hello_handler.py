# hello_handlers.py
import os
from dotenv import load_dotenv
import time
from web3 import Web3

load_dotenv()

class HelloAgent:
    def __init__(self):
        self.ethereum_provider = os.getenv("ETHEREUM_PROVIDER")
        self.wallet_address = os.getenv("WALLET_ADDRESS")
        self.private_key = os.getenv("PRIVATE_KEY")
        self.token_contract_address = os.getenv("TOKEN_CONTRACT_ADDRESS")
      
        if not self.ethereum_provider:
            raise ValueError("Ethereum provider not found in environment variables.")
        if not self.wallet_address:
            raise ValueError("Wallet address not found in environment variables.")
        if not self.private_key:
            raise ValueError("Private key not found in environment variables.")
        if not self.token_contract_address:
            raise ValueError("Token contract address not found in environment variables.")
   
        self.web3 = Web3(Web3.HTTPProvider(self.ethereum_provider))
        if not self.web3.is_connected():
            raise ConnectionError("Failed to connect to Ethereum provider.")
    
    def get_balance(self):
        # Get balance for wallet_address
        balance = self.web3.eth.get_balance(self.wallet_address)
        return self.web3.fromWei(balance, 'ether')  # Convert Wei to Ether

def hello_handler(agent, message):
    try:
        balance = agent.get_balance()  # Make sure the correct agent is being used here
        print(f"[Hello Handler] Balance for {agent.wallet_address}: {balance} Ether")
    except Exception as e:
        print(f"[Hello Handler] Error: {e}")

