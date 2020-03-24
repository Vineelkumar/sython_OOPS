from  itertools import product
x = int(input())
ap = []
ac = []
for i in range(x):
    n,m = input().split(" ")
    ap.append(int(n))
    ac.append(int(m))
y = int(input())
bp = []
bc = []
for i in range(y):
    n,m = input().split(" ")
    bp.append(int(n))
    bc.append(int(m))
pl = list(product(ap,bp))
cl = list(product(ac,bc))
#print(pl,cl)
d = {}
for i in range(len(pl)):
    g = pl[i][0] + pl[i][1]
    h = cl[i][0] * cl[i][1]
    if g not in d:
        d[g] = h
    else:
        d[g]+=h
d =  dict(sorted(d.items(),key = lambda x: -x[0]))
#print(d)
p = 0 
x = list(d.keys())
for i in range(len(x)):
    if d[x[i]] != 0 and i > 0:
        if d[x[i]] > 0:
            print(" + ",end="")
        else:
            print(" - ",end="")
    if d[x[i]] != 0:
        print(abs(d[x[i]]),end="")
    if d[x[i]] !=0 and x[i] !=0:
        print("x^{}".format(x[i]),end="")
