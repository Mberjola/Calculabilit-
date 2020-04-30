import time
import matplotlib.pyplot as plt


def algo2(n:int)-> str:
    ch:str = ""
    nb:int = n
    while (nb != 0):
        ch = str(nb % 2) + ch
        nb = nb // 2
    return ch
# Tests
#for i in range(0,20):
#    print(algo2(i))
# Tracé du temps dʼexécution
T = []
X = range(0,60)
Y = 0
for N in X:
    debut = time.clock()
    algo2(2**N)
    fin = time.clock()
    #print(debut,fin)
    T.append(1000000*(fin-debut))




plt.plot(X, T)
plt.title("Temps dʼexécution algo2(2^N)")
plt.xlabel("N")
plt.ylabel("Temps (sec) *100000")
plt.show()