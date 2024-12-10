def decode():
  order=int(input("Introduce matrix order: "))
  matrixInput=input("Enter matrix numbers separated with ,: ").split(',') 
  encodeMatrix=input("Enter encoding matrix numbers separated with ,: ").split(',')
  matrix=[]
  encode=[]
  for i in range(0,order):
    matrix[i] = []
    encode[i] = []
  for n in matrixInput:
    for row in range(0,4):
      if (len(matrix[row] >= 3)):
        continue
      else:
        matrix[row].append(n)
        break
  numbers=input("Enter numbers separated by ,: ").split(",")
  abc=" ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  result = ""
  for it in numbers:
    result+=abc[int(it)]
  print(result)
