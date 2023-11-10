import numpy as np

one = input("輸入金鑰")
one = one.lower()
one = one.replace(" ", "")

matrix = np.empty((5, 5), dtype=str)    #5*5的換算方格
arr = np.zeros((26, 2), dtype=int)      #紀錄字母是否填入過方格

j = 0                                   #代表5*5方格的y軸
z = 0                                   #代表5*5方格的x軸

#填入金鑰
for char in one:
    if arr[ord(char) - ord('a')][1] == 0:
        arr[ord(char) - ord('a')][1] = 1#標記已填入換算方格
        if char == "i":                 #若遇到i便連同j一起標記填過
            arr[ord('j') - ord('a')][1] = 1
            matrix[j][z] = 'i'
        elif char == "j":               #若遇到j便連同i一起標記填過
            arr[ord('i') - ord('a')][1] = 1
            matrix[j][z] = 'j'
        else:
            matrix[j][z] = char
        z += 1
        if z == 5:
            z = 0
            j += 1

#填充剩餘字母
for i in range(26):
    if arr[i][1] == 0:
        if (chr(i + ord('a'))) == 'i':
            arr[ord('j') - ord('a')][1] = 1

        matrix[j][z] = chr(i + ord('a'))
        z += 1
        if z == 5:
            z = 0
            j += 1

two = input("輸入密文")
two = two.lower()
two = two.replace(" ", "")

# 找尋字符在矩陣中的位置的函數
def find_position(char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

# 使用Playfair Cipher解密
def decrypt_pair(char1, char2):
    row1, col1 = find_position(char1)
    row2, col2 = find_position(char2)

    # 同一列
    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    # 同一行
    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    # 不同列和行
    else:
        return matrix[row1][col2] + matrix[row2][col1]


decrypted_text = ""

for i in range(0, len(two), 2):
    char1 = two[i]
    char2 = two[i + 1]

    decrypted_pair = decrypt_pair(char1, char2)
    decrypted_text += decrypted_pair

# 在解密删除加密的 'x'
for i in range(len(decrypted_text) - 3):
    if decrypted_text[i] == decrypted_text[i + 2] and decrypted_text[i + 1] == 'x':
        decrypted_text = decrypted_text[:i+1] + decrypted_text[i+2:]
        
print("解密結果:", decrypted_text)
