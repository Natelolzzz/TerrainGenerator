from random import randint

L1 = ['','','','','','','','','','','','','','','','','','','','']
L2 = ['','','','','','','','','','','','','','','','','','','','']
L3 = ['','','','','','','','','','','','','','','','','','','','']
L4 = ['','','','','','','','','','','','','','','','','','','','']
L5 = ['','','','','','','','','','','','','','','','','','','','']
Y = 3
Loops = 0

for X in range(20):
  Y = randint(Y-1,Y+1)
  if Y < 1:
    Y = 1
  elif Y > 5:
    Y = 5
  if Y == 1:
    L1[Loops] = " "
    L2[Loops] = " "
    L3[Loops] = " "
    L4[Loops] = " "
    L5[Loops] = "_"
  elif Y == 2:
    L1[Loops] = " "
    L2[Loops] = " "
    L3[Loops] = " "
    L4[Loops] = "_"
    L5[Loops] = "*"
  elif Y == 3:
    L1[Loops] = " "
    L2[Loops] = " "
    L3[Loops] = "_"
    L4[Loops] = "*"
    L5[Loops] = "*"
  elif Y == 4:
    L1[Loops] = " "
    L2[Loops] = "_"
    L3[Loops] = "*"
    L4[Loops] = "*"
    L5[Loops] = "*"
  elif Y == 5:
    L1[Loops] = "_"
    L2[Loops] = "*"
    L3[Loops] = "*"
    L4[Loops] = "*"
    L5[Loops] = "*"

  Loops += 1
print("".join(L1))
print("".join(L2))
print("".join(L3))
print("".join(L4))
print("".join(L5))
