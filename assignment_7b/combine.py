# calculate number of k-permutations of n items
# hussein suleman
# 10 april 2012

n = input ("Enter n:\n")
while not n.isdigit ():
   n = input ("Enter n:\n")
n = eval (n)   

k = input ("Enter k:\n")
while not k.isdigit ():
   k = input ("Enter k:\n")
k = eval (k)

nfactorial = 1
for i in range (1, n+1):
   nfactorial *= i

nkfactorial = 1
for i in range (1, n-k+1):
   nkfactorial *= i

print ("Number of permutations:", nfactorial // nkfactorial)
