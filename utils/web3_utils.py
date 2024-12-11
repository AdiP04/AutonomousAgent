import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

ethereum_provider = os.getenv('ETHEREUM_PROVIDER')
wallet_address = os.getenv('WALLET_ADDRESS')
private_key = os.getenv('PRIVATE_KEY')
token_contract_address = os.getenv('TOKEN_CONTRACT_ADDRESS')

w3 = Web3(Web3.HTTPProvider(ethereum_provider))
print(w3,"w3")

def transfer_tokens(w3: Web3, wallet_address: str, private_key: str, contract_address: str, to_address: str, amount_in_wei: int):
    try:
        # Convert addresses to checksum format
        wallet_address = w3.toChecksumAddress(wallet_address)
        to_address = w3.toChecksumAddress(to_address)
        contract_address = w3.toChecksumAddress(contract_address)

        contract = w3.eth.contract(address=contract_address, abi=[
            {"constant": False, "inputs": [{"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}],
             "name": "transfer", "outputs": [{"name": "", "type": "bool"}], "type": "function"}
        ])
        
        nonce = w3.eth.get_transaction_count(wallet_address)
        
        # Set the gas price as a static value in Wei (for example, 20 Gwei)
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
