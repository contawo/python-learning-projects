# nohelp.py

def welcome():
    print('Welcome to the automated technical support system.')
    print('Please describe your problem.')

def get_input():
    return input().lower()


def main():

    welcome()    
    query = get_input()
    
    while (not query=='quit'):
        print('Curious, tell me more.')

        query = get_input()    
    
    
main()