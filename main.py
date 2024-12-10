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
    matrix=np.matrix(array, dtype=np.int64).reshape(order, order).T
    print(np.matmul(encodeMatrix, matrix))
  if input("Do you want to keep the encoding matrix? yes or no: ") == "yes":
    return encodeMatrix
  else:
    return None

def decode(encodeMatrix: np.matrix=None) -> np.matrix:
  matrices=input("Enter matrix numbers separating columns with , and rows with ; and separate matrices with spaces ( ): ")
  if encodeMatrix is None:
    encodeMatrix=np.matrix(input("Enter encoding matrix numbers separating columns with , and rows with ;: "), dtype=np.int64)
  result=""
  for matrix in matrices.split(' '):
    mat_message=np.matmul(encodeMatrix.getI(), np.matrix(matrix, dtype=np.int64))
    abc=" ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    temp_result = ""

    for column in mat_message.T.tolist():
      for it in column:
        temp_result+=abc[round(it)]
    result+=temp_result
  print(result)
  if input("Do you want to keep the encoding matrix? yes or no: ") == "yes":
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
  return_value: np.matrix = None
  while (True):
    option=input("Choose option: Encode [e] or Decode [d]: ")
    if option == "d":
      return_value = decode()
      while input("Do you want to keep the decoding? yes or no: ") == "yes":
        return_value=decode(return_value)
    elif option == "e":
      return_value = encode()
      while input("Do you want to keep the encoding? yes or no: ") == "yes":
        return_value=encode(return_value)