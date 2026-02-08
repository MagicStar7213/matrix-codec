# Matrices

Matrix utils allow you to calculate the product of two matrices, the adjugate/conjugate matrix, the determinant and encode a message using matrices.

## Usage
The encoding function only allows uppercase letters and spaces for now.
Matrices should be introduced in a special way. Columns must be separated with single slashes `/` and rows with double slashes `//`. Also, multiple matrices are separated from each other with spaces  `" "`

### Product (Multiplication)
You enter the first matrix, hit `Enter ⏎` and then the second matrix.

For example, if I wanted to enter the matrix $`\begin{pmatrix} 1 & -2 & 1\\0 & -3 & 4\\2 & 1 & -1 \end{pmatrix}`$ I would have to type it like this: `1/-2/1//0/-3/4//2/1/-1` 
and then enter the second matrix $`\begin{bmpmatrixatrix} 2 & -1 & 1\\3 & 0 & -2\\-1 & 4 & 3 \end{pmatrix}`$ which would turn into `2/-1/1//3/0/-2//-1/4/3`.

The result would then be: $`\begin{pmatrix} -5 & 3 & 8\\-13 & 16 & 18\\8 & -6 & -3 \end{pmatrix}`$

### Determinant
You enter the matrix you want to calculate the determinant of, for example $`\begin{vmatrix} 1 & -2 & 1\\0 & -3 & 4\\2 & 1 & -1 \end{vmatrix}`$,
which you would type as `1/-2/1//0/-3/4//2/1/-1`.

The output is the result: `-11`

### Rank
To calculate the rank of any matrix, just enter it, for example: $`\begin{pmatrix} 1 & -2 & 1 & 3\\0 & -3 & 4 & 1\\2 & 1 & -1 & 0 \end{pmatrix}`$ in the program like so: `1/-2/1/3//0/-3/4/1//2/1/-1/0`.

The program will then print the rank of the given matrix: `3`

### Adjugate (conjugate)
To calculate de adjugate you type the matrix you want, for example this one: $`\begin{pmatrix} 1 & -2 & 1\\0 & -3 & 4\\2 & 1 & -1 \end{pmatrix}`$
in the form: `1/-2/1//0/-3/4//2/1/-1`.

Result: 
$`\begin{pmatrix} -1 & 8 & 6\\-1 & -3 & -5\\-5 & -4 & -3 \end{pmatrix}`$

### Encoding
You must provide 2 inputs: the **message** and the **encoding matrix**. The message must be in all CAPS and cannot contain any special characters (`,.;:?'"-_+=!@#$%^&*()~|\\[]{}<>/` or accents) nor numbers. For example: `I LOVE PYTHON`

After, choose an encoding matrix. **IT MUST BE SQUARE**, or it won't work. For example

$`\begin{pmatrix}
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9
\end{pmatrix}`$

When we plug it into the program, it looks like this `1/2/3//4/5/6//7/8/9`. Then the program gives the matrix or matrices containing the encoded message:
$`\begin{pmatrix}
45 & 74 & 107\\
108 & 200 & 230\\
171 & 326 & 353
\end{pmatrix}
\begin{pmatrix}
81 & 14 & 0\\
210 & 56 & 0\\
339 & 98 & 0
\end{pmatrix}`$

### Decoding
To decode a message we need 2 inputs again: the matrix/matrices of the **encoded message** and the **encoding matrix**.

First you must input the matrices that form the encoded message, just like when encoding. However, to separate between matrices you must separate them with a space `' '`.

Therefore, the matrices 

$`\begin{pmatrix}
45 & 74 & 107\\
108 & 200 & 230\\
171 & 326 & 353
\end{pmatrix}
\begin{pmatrix}
81 & 14 & 0\\
210 & 56 & 0\\
339 & 98 & 0
\end{pmatrix}`$

would be introduced into the program like this: `45/74/107//108/200/230//171/326/353 81/14/0//210/56/0//339/98/0`. After, you input the encoding matrix `1/2/3//4/5/6//7/8/9` and it gives us the original message `I LOVE PYTHON`

### Using variables
When entering matrices for any operation you can also include variables or expressions, just not divisions (as / is used for element separation, but it will be changed in the future). For example, a matrix can look like `5/m-7//k-4/6` and it will be computed symbolically
