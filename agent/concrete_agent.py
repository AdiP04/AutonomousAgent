from web3 import Web3
import time
import os
import random
from utils.web3_utils import transfer_tokens
from agent.base_agent import BaseAgent



class ConcreteAgent(BaseAgent):
   def __init__(self, ethereum_provider, wallet_address, private_key, token_contract_address):
       super().__init__()
       self.w3 = Web3(Web3.HTTPProvider(ethereum_provider))
       self.wallet_address = wallet_address
       self.private_key = private_key
       self.token_contract_address = token_contract_address

       if not self.w3.is_connected():
           raise ConnectionError("Failed to connect to Ethereum provider.")

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
           try:
               balance = self.w3.eth.get_balance(os.getenv("WALLET_ADDRESS"))
               print(f"Balance for {self.wallet_address}: {balance} Wei")
           except Exception as e:
               print(f"Error checking balance: {e}")
           time.sleep(10)

   def transfer_tokens(w3: Web3, wallet_address: str, private_key: str, contract_address: str, to_address: str, amount_in_wei: int):
    try:
        to_address = w3.toChecksumAddress(to_address)

        contract = w3.eth.contract(address=contract_address, abi=[
            {"constant": False, "inputs": [{"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}],
             "name": "transfer", "outputs": [{"name": "", "type": "bool"}], "type": "function"}
        ])

        nonce = w3.eth.get_transaction_count(wallet_address)
        
        gas_price_wei = 20000000000  # 20 Gwei in Wei

        transaction = contract.functions.transfer(to_address, amount_in_wei).build_transaction({
            'nonce': nonce,
            'gas': 200000,
            'gasPrice': gas_price_wei,
        })

        signed_tx = w3.eth.account.sign_transaction(transaction, private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

        return tx_hash.hex()

    except Exception as e:
        print(f"Token transfer failed: {e}")
        return None

