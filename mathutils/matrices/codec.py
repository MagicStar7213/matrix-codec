from sympy import NonSquareMatrixError, nsimplify, pprint
from .utils import Matrix, parse_matrix


def encode(encode_matrix: Matrix | None):
    message = input("What message do you want to encode? ")
    if encode_matrix is None:
        encode_matrix = parse_matrix(input("Enter encoding matrix: "))
        if encode_matrix is None:
            if input("There was an error in the encoding matrix. Start over? [Y/n] ").lower() == "y":
                return encode(encode_matrix)
            else:
                return None
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
        if input("Do you want to keep the encoding matrix? [Y/n]: ").lower() == "y":
            return encode_matrix
        else:
            return None


def decode(encode_matrix: Matrix | None):
    matrices = input(
        "Enter matrices separating each one with one space ( ): ")
    if encode_matrix is None:
        encode_matrix = parse_matrix(input("Enter encoding matrix: "))
        if encode_matrix is None:
            if input("There was an error in the encoding matrix. Start over? [Y/n] ").lower() == "y":
                return decode(encode_matrix)
            else:
                return None
    try:
        encode_matrix.inv()
    except NonSquareMatrixError:
        print("ERROR: Given matrix not square, thus not invertible")
        if input("Try again? [Y/n]").lower() == "y":
            return decode(None)
        else:
            exit(1)
    except ValueError:
        print("ERROR: The determinant of the given matrix is 0, thus it cannot be inverted")
        if input("Try again? [Y/n]").lower() == "y":
            return decode(None)
        else:
            exit(1)
    else:
        result = ""
        for raw_matrix in matrices.split(' '):
            matrix = parse_matrix(raw_matrix)
            if matrix is None:
                if input("There was an error in a message matrix. Start over? [Y/n] ").lower() == "y":
                    return decode(encode_matrix)
                else:
                    return None
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
        if input("Do you want to keep the encoding matrix? [Y/n]: ").lower() == "y":
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
                return
            else:
                print("ERROR: Option not found. Please try again.")
                continue