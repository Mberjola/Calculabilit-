from time import *
import matplotlib.pyplot as plt
def MultiRusse(x: int, y: int):
    a = x
    b = y
    r = 0
    while (a > 0):
        if (a % 2 == 0):
            b = 2 * b
            a = a // 2
        else:
            r = r + b
            a = a - 1
    return r
# print("MultiRusse(2,4)")
# print(MultiRusse(2,4))
# print("MultiRusse(3,5)")
# print(MultiRusse(3,5))
# print("MultiRusse(2,2)")
# print(MultiRusse(2,2))
T = []
E = []
X = range(0, 250)
for N in X:
    debut = time()
    MultiRusse(2**N,5)
    T.append(time()-debut)
s = 0
for i in T:
    s += i
    moy = s / 250
print(moy)
plt.plot(X, T)
plt.title("Temps d'exécution Multiplication russe (2^N,3)")
plt.xlabel("N")
plt.ylabel("Temps (ns)")
plt.show()