from src.core.ai_service import AIService
from src.utils.api_utils import print_response

def main():
    ai_service = AIService()
    
    while True:
        question = input("请输入问题 (退出请输入'exit'): ")
        
        if question.lower() == 'exit':
            break
        
        response = ai_service.ask_question(question)
        print_response(response)

if __name__ == "__main__":
    main()
