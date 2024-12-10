# Matrix Codec
![Python](https://img.shields.io/badge/-Python-yellow?style=flat-square&labelColor=blue&logo=python&logoColor=white)
![Matrix](https://img.shields.io/badge/-Matrix-black?style=flat-square&logo=matrix)

Matrix Codec is a simple Python script that allows you to encode a message using an encoding matrix you must provide.

## Usage
The encoding function only allows uppercase letters and spaces for now.
Matrices should be introduced in a special way. Columns must be separated with commas `,` and rows with semicolons `;`. Also multiple matrices are separated from each other with spaces  `" "`

### Encoding
You must provide 2 inputs: the message and the encoding matrix. The message must be in all CAPS and cannot contain any special characters (`,.;:?'"-_+=!@#$%^&*()~|\\[]{}<>/` or accents) nor numbers. For example: `I LOVE PYTHON`

After, choose an encoding matrix. **IT MUST BE SQUARE**, or it won't work. For example
$$ \begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6\\
7 & 8 & 9
\end{bmatrix}$$

When we plug it into the program, it looks like this `1,2,3;4,5,6;7,8,9`. Then the program gives the matrix or matrices containing the encoded message: ```html
[[ 45  74 107]<br/>
 [108 200 230]<br/>
 [171 326 353]]<br/>
[[ 81  14   0]<br/>
 [210  56   0]<br/>
 [339  98   0]]
```