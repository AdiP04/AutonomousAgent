from utils.web3_utils import approve_tokens, transfer_tokens
from config.settings import WALLET_ADDRESS, PRIVATE_KEY

class CryptoHandler:
    def handle_message(self, message, target_address):
        if "crypto" in message.lower():
            # Approve the transfer of 1 token to the target address
            approval_tx = approve_tokens(WALLET_ADDRESS, PRIVATE_KEY, target_address, 1)
            if approval_tx:
                print(f"Approved 1 token transfer to {target_address}, approval TX: {approval_tx}")
                
                # Now proceed with the transfer
                success = transfer_tokens(WALLET_ADDRESS, PRIVATE_KEY, target_address, 1)
                if success:
                    print(f"Transferred 1 token to {target_address}, transfer TX: {success}")
                else:
                    print("Failed to transfer tokens.")
            else:
                print("Token approval failed.")
