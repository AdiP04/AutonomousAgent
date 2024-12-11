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

    def test_behavior_execution(self):
        agent = BaseAgent()
        behavior_executed = []

        def test_behavior():
            behavior_executed.append(True)

        agent.add_behavior(test_behavior)
        agent.run_behaviors()
        self.assertTrue(behavior_executed)

if __name__ == "__main__":
    unittest.main()
