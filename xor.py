import numpy as np

# AND回路
def AND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.7
  tmp = np.sum(w*x) + b
  
  if tmp <= 0:
    return 0
  else:
    return 1

# OR回路  
def OR(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.3
  tmp = np.sum(w*x) + b
  
  if tmp <= 0:
    return 0
  else:
    return 1

# NAND回路  
def NAND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([-0.5, -0.5])
  b = 0.7
  tmp = np.sum(w*x) + b
  
  if tmp <= 0:
    return 0
  else:
    return 1

# XOR回路
def XOR(x1, x2):
  s1 = NAND(x1, x2)
  s2 = OR(x1, x2)
  y = AND(s1, s2)
  return y

#main
print("type 0 or 1")
i1 = int(input("input 1: "))
i2 = int(input("input 2: "))
print(XOR(i1, i2))