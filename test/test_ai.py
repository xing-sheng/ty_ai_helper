import unittest
from src.core.ai_service import AIService

class TestAIService(unittest.TestCase):
    def test_ask_question(self):
        ai_service = AIService()
        response = ai_service.ask_question("你是谁?")
        self.assertIn("choices", response)
        self.assertIn("message", response["choices"][0])

if __name__ == "__main__":
    unittest.main()
