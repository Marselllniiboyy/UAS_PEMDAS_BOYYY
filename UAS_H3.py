L = 1000
BL = 900
C = 500
BC = 400
B =100
WB = 90 
K = 50
WK = 40
W = 10
HW = 9
U = 5
HU = 4
H = 1

i = int(input())

if i < 1 or i > 3999:
  print("No Proceed")
else:
  while i > 0:
    if  i-L >= 0:
      i = i-L
      print("L", end="")
    elif i-BL >= 0:
      i = i-BL
      print("BL", end="")
    elif i - C >=0:
      i = i-C
      print("C",end="")
    elif i  - BC >= 0:
      i = i-BC
      print("BC", end="")
    elif i - B >= 0:
      i = i-B
      print("B", end="")
    elif  i - WB >= 0:
      i = i-WB  
      print("WB", end="")
    elif  i - K >= 0:
      i = i-K
      print("K", end="")
    elif  i - WK >= 0:
      i = i-WK
      print("WK", end="")
    elif   i - W >= 0:
      i = i-W
      print("W", end="")
    elif   i - HW >= 0:
      i = i-HW
      print("HW", end="")
    elif i - U >= 0:
      i = i -  U
      print("U", end="")
    elif i - HU >= 0:
      i = i - HU
      print("HU", end="")
    elif i - H >= 0:
      i = i - H
      print("H", end="")