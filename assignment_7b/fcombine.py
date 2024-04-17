# calculate number of k-permutations of n items
# hussein suleman
# 10 april 2012

from mymath import *

def main ():
   n = get_integer("n")
   k = get_integer("k")
   nfactorial = calc_factorial(n)
   nkfactorial = calc_factorial(n, k)
   print ("Number of permutations:", nfactorial // nkfactorial)

if __name__ == "__main__":
   main()
