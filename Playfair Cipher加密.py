import numpy as np

one = input("輸入金鑰")
one = one.lower()
one = one.replace(" ", "")

matrix = np.empty((5, 5), dtype=str)
arr = np.zeros((26, 2), dtype=int)

j = 0
z = 0

for char in one:
    if arr[ord(char) - ord('a')][1] == 0:
        arr[ord(char) - ord('a')][1] = 1
        if char == "i":
            arr[ord('j') - ord('a')][1] = 1
            matrix[j][z] = 'i'
        elif char == "j":
            arr[ord('i') - ord('a')][1] = 1
            matrix[j][z] = 'j'
        else:
            matrix[j][z] = char
        z += 1
        if z == 5:
            z = 0
            j += 1
            
#print(matrix)
for i in range(26):
    if arr[i][1] == 0:
        if (chr(i + ord('a'))) == 'i':
            arr[ord('j') - ord('a')][1] = 1
        
        matrix[j][z] = chr(i + ord('a'))
        z += 1
        if z == 5:
            z = 0
            j += 1
    
#print(matrix)
two = input("輸入明文")
two = two.lower()
two = two.replace(" ", "")

# 找尋字符在矩陣中的位置的函數
def find_position(char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

# 使用Playfair Cipher加密
def encrypt_pair(char1, char2):
    row1, col1 = find_position(char1)
    row2, col2 = find_position(char2)

    # 同一列
    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    # 同一行
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    # 不同列和行
    else:
        return matrix[row1][col2] + matrix[row2][col1]


encrypted_text = ""

for i in range(0, len(two), 2):
    if i == len(two) - 2:
        if len(two) % 2 == 1:
            two += 'x'
    
    char1 = two[i]
    char2 = two[i + 1] 
    
    # 如果字符相同，插入x
    if char1 == char2:
        two = two[:i+1] + 'x' + two[i+1:]
        char2 = 'x'

    encrypted_pair = encrypt_pair(char1, char2)
    encrypted_text += encrypted_pair

print("加密結果:", encrypted_text)
