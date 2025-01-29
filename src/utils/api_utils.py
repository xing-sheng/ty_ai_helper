def print_response(response):
    if 'error' in response:
        print(f"Error: {response['error']}")
    else:
        print(f"AI Response: {response['choices'][0]['message']['content']}")
