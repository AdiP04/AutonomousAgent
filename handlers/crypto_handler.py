from utils.web3_utils import transfer_tokens

def crypto_handler(agent, message):
    target_address = "0x1234567890abcdef1234567890abcdef12345678"
    amount = 1  # Token amount
    tx_hash = transfer_tokens(agent.w3, agent.wallet_address, agent.private_key, agent.token_contract_address, target_address, amount)
    if tx_hash:
        print(f"Successfully transferred {amount} tokens to {target_address}. Transaction Hash: {tx_hash}")
    else:
        print("Token transfer failed.")
