import numpy as np

def encode(encodeMatrix: np.matrix=None) -> np.matrix:
  message=input("What message do you want to encode? ")
  if encodeMatrix is None:
    encodeMatrix=np.matrix(input("Enter encoding matrix numbers separating columns with , and rows with ;: "), dtype=np.int64)
  order=encodeMatrix.shape[1]
  abc=" ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  message_list=list(message)
  for letter in message_list:
    message_list[message_list.index(letter)] = abc.index(letter)
  chunks = [message_list[i:i+(order*order)] for i in range(0, len(message_list), (order*order))]
  for array in chunks:
    if len(array) < order*order:
      array_length=len(array)
      for i in range(order*order-array_length):
        array.append(0)
    matrix=np.matrix(array).reshape(order, order).T
    print(np.matmul(encodeMatrix, matrix))
  if int(input("Do you want to keep the encoding matrix? Yes [1] or No [0] ")) == 1:
    return encodeMatrix
  else:
    return None

def decode(encodeMatrix: np.matrix=None) -> np.matrix:
  matrix=np.matrix(input("Enter matrix numbers separating columns with , and rows with ;: "), dtype=np.int64)
  if encodeMatrix is None:
    encodeMatrix=np.matrix(input("Enter encoding matrix numbers separating columns with , and rows with ;: "), dtype=np.int64)
  mat_message=np.matmul(encodeMatrix.getI(), matrix)
  
  abc=" ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  result = ""
  for column in mat_message.T.tolist():
    for it in column:
      result+=abc[round(it)]
  print(result)
  if int(input("Do you want to keep the encoding matrix? Yes [1] or No [0] ")) == 1:
    return encodeMatrix
  else:
    return None

if __name__ == "__main__":
  print("""
  __  __           _            _        
 |  \/  |   __ _  | |_   _ __  (_) __  __
 | |\/| |  / _` | | __| | '__| | | \ \/ /
 | |  | | | (_| | | |_  | |    | |  >  < 
 |_|  |_|  \__,_|  \__| |_|    |_| /_/\_\\
   ____               _                  
  / ___|   ___     __| |   ___    ___    
 | |      / _ \   / _` |  / _ \  / __|   
 | |___  | (_) | | (_| | |  __/ | (__    
  \____|  \___/   \__,_|  \___|  \___|   
                                         
""")
  while (True):
    option=input("Choose option: Encode [e] or Decode [d] ")
    if option == "d":
      return_value: np.matrix = decode()
      while (not(return_value is None)):
        return_value=decode(return_value)
    elif option == "e":
      return_value: np.matrix = encode()
      while not((return_value is None)):
        return_value=encode(return_value)