L1 = []
L2 = []
L3 = []
L4 = []
L5 = []

def placemap(x,y,e):
    if y == 1:
        L5.insert(x, e)
    if y == 2:
        L4.insert(x, e)
    if y == 3:
        L3.insert(x, e)
    if y == 4:
        L2.insert(x, e)
    if y == 5:
        L1.insert(x, e)  

def printmap():
    print(' '.join(str(e) for e in L1))
    print(' '.join(str(e) for e in L2))
    print(' '.join(str(e) for e in L3))
    print(' '.join(str(e) for e in L4))
    print(' '.join(str(e) for e in L5))
