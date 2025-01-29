import unittest
from src.core.ai_service import ask_ai

class TestAIService(unittest.TestCase):

    def test_ask_ai(self):
        question = "你是谁？"
        answer = ask_ai(question)
        self.assertIsNotNone(answer)
        self.assertIn("助手", answer)

if __name__ == '__main__':
    unittest.main()
