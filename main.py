from random import randint
import sys, time, random

typing_speed = 1000  #wpm
legnth = int(input("> "))

def print_slow(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(random.random() * 10.0 / typing_speed)


while True:
  L1 = ['' for i in range(legnth)]
  L2 = ['' for i in range(legnth)]
  L3 = ['' for i in range(legnth)]
  L4 = ['' for i in range(legnth)]
  L5 = ['' for i in range(legnth)]
  Y = randint(2, 4)

  for X in range(legnth):
    if randint(1, 2) == 1:
      Y = randint(Y - 1, Y + 1)
    if Y < 1:
      Y = 1
    elif Y > 5:
      Y = 5
    if Y == 1:
      L1[X] = " "
      L2[X] = " "
      L3[X] = " "
      L4[X] = " "
      L5[X] = "_"
    elif Y == 2:
      L1[X] = " "
      L2[X] = " "
      L3[X] = " "
      L4[X] = "_"
      L5[X] = "*"
    elif Y == 3:
      L1[X] = " "
      L2[X] = " "
      L3[X] = "_"
      L4[X] = "*"
      L5[X] = "*"
    elif Y == 4:
      L1[X] = " "
      L2[X] = "_"
      L3[X] = "*"
      L4[X] = "*"
      L5[X] = "*"
    elif Y == 5:
      L1[X] = "_"
      L2[X] = "*"
      L3[X] = "*"
      L4[X] = "*"
      L5[X] = "*"

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
