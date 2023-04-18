from random import randint
import sys,time,random

typing_speed = 200 #wpm
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)

while True:
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
  print_slow("".join(L1))
  print("")
  print_slow("".join(L2))
  print("")
  print_slow("".join(L3))
  print("")
  print_slow("".join(L4))
  print("")
  print_slow("".join(L5))
  print("")
  print("")
