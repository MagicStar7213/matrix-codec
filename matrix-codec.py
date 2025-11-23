from sympy import NonSquareMatrixError, init_printing, Matrix, nsimplify, pprint
from utils import list_to_matrix


def encode(encode_matrix):
    message = input("What message do you want to encode? ")
    if encode_matrix is None:
        encode_string = [m.split('/') for m in input("Enter encoding matrix numbers separating columns with / and rows with //: \n").split('//')]
        encode_matrix = list_to_matrix(encode_string)
    try:
        encode_matrix.inv()
    except NonSquareMatrixError:
        print("ERROR: Given matrix not square, thus not invertible")
        if input("Try again? [Y/n]").lower() == "y":
            encode(None)
        else:
            exit(1)
    except ValueError:
        print("ERROR: The determinant of the given matrix is 0, thus it cannot be inverted")
        if input("Try again? [Y/n]").lower() == "y":
            encode(None)
        else:
            exit(1)
    else:
        order = encode_matrix.shape[1]
        abc = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        message_list = list(message)
        char_list: list[int] = []
        if message.islower():
            abc = abc.lower()
        for letter in message_list:
            char_list.append(abc.index(letter))
        chunks = [char_list[i:i + (order * order)] for i in range(0, len(char_list), (order * order))]
        for array in chunks:
            if len(array) < order * order:
                array_length = len(array)
                for i in range(order * order - array_length):
                    array.append(0)
            matrix = Matrix(array).reshape(order, order).T
            pprint((encode_matrix*matrix).applyfunc(nsimplify))
            print(" ")
        if input("Do you want to keep the encoding matrix? yes or no: ") == "yes":
            return encode_matrix
        else:
            return None


def decode(encode_matrix):
    matrices = input(
        "Enter matrix numbers separating columns with / and rows with // and separate matrices with spaces ( ): ")
    if encode_matrix is None:
        encode_string = [m.split('/') for m in input("Enter encoding matrix numbers separating columns with / and rows with //: ").split('//')]
        encode_matrix = list_to_matrix(encode_string)
    try:
        encode_matrix.inv()
    except NonSquareMatrixError:
        print("ERROR: Given matrix not square, thus not invertible")
        if input("Try again? [Y/n]").lower() == "y":
            decode(None)
        else:
            exit(1)
    except ValueError:
        print("ERROR: The determinant of the given matrix is 0, thus it cannot be inverted")
        if input("Try again? [Y/n]").lower() == "y":
            decode(None)
        else:
            exit(1)
    else:
        result = ""
        for raw_matrix in matrices.split(' '):
            matrix = list_to_matrix([m.split('/') for m in raw_matrix.split('//')])
            mat_message = encode_matrix.inv()*matrix
            if any(i > 27.5 for line in mat_message.tolist() for i in line):
                mat_message = matrix*encode_matrix.inv()
            abc = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            temp_result = ""

            for column in mat_message.T.tolist():
                for it in column:
                    temp_result += abc[round(it)]
            result += temp_result
        print(result)
        if input("Do you want to keep the encoding matrix? yes or no: ") == "yes":
            return encode_matrix
        else:
            return None


class Main:

    def __init__(self) -> None:
        self.return_value = None

    def app(self):
        print("""
    __  __           _            _        
   |  \\/  |   __ _  | |_   _ __  (_) __  __
   | |\\/| |  / _` | | __| | '__| | | \\ \\/ /
   | |  | | | (_| | | |_  | |    | |  >  < 
   |_|  |_|  \\__,_|  \\__| |_|    |_| /_/\\_\\
     ____               _                  
    / ___|   ___     __| |   ___    ___    
   | |      / _ \\   / _` |  / _ \\  / __|   
   | |___  | (_) | | (_| | |  __/ | (__    
    \\____|  \\___/   \\__,_|  \\___|  \\___|   
                                         
    """)
        while True:
            option = input("Choose option: Encode [e], Decode [d] or Exit [q]: ")
            if option == "d":
                print("DECODE")
                while True:
                    self.return_value = decode(self.return_value)
                    if input("Do you want to keep decoding? yes or no: ") != "yes":
                        break
            elif option == "e":
                print("ENCODE")
                while True:
                    self.return_value = encode(self.return_value)
                    if input("Do you want to keep encoding? yes or no: ") != "yes":
                        break
            elif option == "q":
                print("Exiting...")
                exit(0)


if __name__ == "__main__":
    init_printing()
    Main().app()
