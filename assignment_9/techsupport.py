# Tech support based on support

import numpy as np

responses= np.array([
    ['bluetooth','Have you tried mouthwash?'],
    ['windows','Ah, I think I see your problem. What version?'],
    ['apple', 'You do mean the computer kind?'],
    ['blue', 'Ah, the blue screen of death. And then what happened?'],
    ['spam', 'You should see if your mail client can filter messages.'],
    ['connection', 'Contact Telkom.'],
    ['crashed', 'Are the drivers up to date?'],
    ['hacked', 'You should consider installing anti-virus software.']])

def get_response(input_text):
    input_text_list = separate_input_text(input_text)
    
    for word in input_text_list:
        for word_response in responses:
            if word_response[0] == word:
                return word_response[1]
    return None
    

def print_welcome():
    print('Welcome to the automated technical support system.')
    print('Please describe your problem:')


def get_input():
    return input().lower()

# Separates an input text by spaces
def separate_input_text(text):
    return text.split(" ")

def main():
    print_welcome()
    query=get_input()
    while not query=='quit':
        response=get_response(query)
        if response==None:
            print('Curious, tell me more.')
        else:
            print(response)
        query=get_input()
        
if __name__ == "__main__":
    main()
