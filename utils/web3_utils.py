from web3 import Web3
from web3.middleware import geth_poa_middleware  # For PoA networks like Rinkeby

def get_balance(w3: Web3, address: str):
    try:
        balance = w3.eth.get_balance(address)
        return w3.fromWei(balance, 'ether')
    except Exception as e:
        print(f"Error fetching balance: {e}")
        return None

def transfer_eth(w3: Web3, private_key: str, to_address: str, value: float):
    try:
        # Mock transaction parameters
        from_address = w3.eth.account.privateKeyToAccount(private_key).address
        nonce = w3.eth.get_transaction_count(from_address)

        transaction = {
            'to': to_address,
            'value': w3.toWei(value, 'ether'),
            'gas': 21000,
            'gasPrice': w3.toWei('50', 'gwei'),  # Adjust gas price if needed
            'nonce': nonce,
            'chainId': 1  # Replace with your network chain ID
        }

        # Sign the transaction
        signed_txn = w3.eth.account.sign_transaction(transaction, private_key)

        # Mock transaction: print transaction details instead of sending
        print(f"Transaction details: {transaction}")
        print(f"Signed transaction hash: {signed_txn.hash.hex()}")

        # Uncomment the next lines to send real transactions
        # tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        # print(f"Transaction hash: {tx_hash.hex()}")

        return "Mock transaction executed"
    except Exception as e:
        print(f"Error creating transaction: {e}")
        return None
