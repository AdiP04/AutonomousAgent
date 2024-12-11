# Autonomous Agent Framework

An autonomous agent framework integrated with Ethereum blockchain functionality. This project demonstrates message handling, behaviors, and interaction with blockchain smart contracts for tasks such as token transfers and balance checks.

## Features

- **Autonomous Behavior**: Simulates real-time autonomous behavior with message generation.
- **Message Handling**: Flexible system for handling various types of messages.
- **Blockchain Integration**: Interacts with Ethereum blockchain to transfer tokens and check wallet balances.
- **Customizable Handlers**: Easily extendable to add new message types and handlers.
- **Unit Testing**: Comprehensive test suite to ensure stability and functionality.

---

## Getting Started

### Prerequisites

1. **Python (>=3.8)**
   - Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/).
2. **Ethereum Provider**
   - Use a provider such as [Infura](https://infura.io/) or [Alchemy](https://www.alchemy.com/).

---

### Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AdiP04/AutonomousAgent.git
   cd AutonomousAgent
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the root directory with the following:
   ```env
   ETHEREUM_PROVIDER=<Your Ethereum Node URL>
   WALLET_ADDRESS=<Your Wallet Address>
   PRIVATE_KEY=<Your Private Key>
   TOKEN_CONTRACT_ADDRESS=<Your Token Contract Address>
   ```

5. **Run the Application**:
   ```bash
   python main.py
   ```

6. **Run Tests**:
   ```bash
   python -m unittest discover tests
   ```

---

## Project Structure

```
AutonomousAgent/
├── agent/
│   ├── __init__.py
│   ├── base_agent.py       # Base agent class with messaging and behaviors
│   └── concrete_agent.py   # Implements Ethereum-based functionalities
├── handlers/
│   ├── __init__.py
│   ├── hello_handler.py    # Example of a simple message handler
│   └── crypto_handler.py   # Handles Ethereum-related tasks
├── utils/
│   ├── __init__.py
│   └── web3_utils.py       # Utility functions for interacting with Ethereum
├── tests/
│   └── test_agent.py       # Unit tests for the agent
├── .gitignore              # Excluded files/folders
├── requirements.txt        # Project dependencies
├── .env                    # Environment variables
├── main.py                 # Entry point for the application
└── README.md               # Project documentation
```

---

## Example Usage

### Running the Agent

- The agent generates random messages, handles Ethereum token transfers, and checks wallet balances autonomously.
- Example log output:
  ```
  Generated Message: hello blockchain
  Balance for 0xYourWalletAddress: 1.23 ETH
  Successfully transferred 10 tokens to 0xRecipientAddress. Transaction Hash: 0x123abc...
  ```

### Adding Custom Behaviors

- Define new behaviors and register them with the agent:
  ```python
  def custom_behavior():
      print("Executing custom behavior...")

  agent.add_behavior(custom_behavior)
  ```

---

## Dependencies

- Web3.py: Ethereum blockchain interaction
- Python-dotenv: Environment variable management

Install all dependencies using `pip install -r requirements.txt`.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact

- Author: Aditya Patil
- Email: adityapatilap4121@gmail.com
- GitHub: (https://github.com/AdiP04)
