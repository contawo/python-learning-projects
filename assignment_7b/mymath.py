def get_integer(s):
    if s == "n":
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        return eval (n) 
    else:
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        return eval (k)

def calc_factorial(n, k = 0):
    nkfactorial = 1
    for i in range (1, n-k+1):
        nkfactorial *= i
    return nkfactorial