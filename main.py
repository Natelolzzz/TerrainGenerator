import random

L1 = []
L2 = []
L3 = []
L4 = []
L5 = []

Loop1 = 1
Loop2 = 1
Loop3 = 1

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

while Loop1 != 5:
    A = random.randint(0, 3) 
    while Loop2 != A:
        placemap(Loop1,Loop2,2)
        loop2 = Loop2+1
    B = random.randint(1, 2)
    while Loop3 != B:
        placemap(Loop1,A+Loop3,1)
        Loop3 = Loop3+1
    Loop1 = Loop1+1
printmap()
