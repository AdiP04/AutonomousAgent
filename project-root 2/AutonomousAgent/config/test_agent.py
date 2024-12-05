import unittest
from agent.base_agent import BaseAgent

class TestBaseAgent(unittest.TestCase):
    def test_message_handling(self):
        agent = BaseAgent()
        messages = []

        def test_handler(message):
            messages.append(message)

        agent.register_handler("test", test_handler)
        agent.receive_message("test message")
        agent.process_messages()
        self.assertIn("test message", messages)

if __name__ == "__main__":
    unittest.main()