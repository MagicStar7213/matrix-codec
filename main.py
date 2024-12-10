import numpy as np

def decode(encodeMatrix: np.matrix=None):
  matrix=np.matrix(input("Enter matrix numbers separating columns with , and rows with ;: "), dtype=np.int64)
  if encodeMatrix == None:
    encodeMatrix=np.matrix(input("Enter encoding matrix numbers separating columns with , and rows with ;: "), dtype=np.int64)
  mat_message=np.matmul(encodeMatrix.getI(), matrix)
  
  abc=" ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  result = ""
  for column in mat_message.T.tolist():
    for it in column:
      result+=abc[round(it)]
  print(result)

if __name__ == "__main__":
  decode()