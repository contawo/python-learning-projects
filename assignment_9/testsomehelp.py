# Harness for somehelp

import random
import somehelp
import sys

def main():
    seed = int(sys.argv[1])
    random.seed(seed)
    somehelp.main()
    
main()
