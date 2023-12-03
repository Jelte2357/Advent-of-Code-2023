import re

def find_numbers(string):
    matches = re.finditer(r'\d+', string)
    return [(match.group(0), match.start(), match.end()) for match in matches]

s = 0

with open("input.txt", "r") as f:
    data = f.readlines()
    StrLen = len(data[0][:-1]) # -1 to remove \n, all strings are the same length
    DataLen = len(data)
    
    for enumL, line in enumerate(data):
        Nums = find_numbers(line) # return [(number, start, end), ...]
        for Num in Nums:
            for i in range(enumL - 1, enumL + 2): # -1, 0, 1 compared to current line
                if i < 0 or i >= DataLen: # if out of bounds
                    continue
                for j in range(Num[1]-1, Num[2]+1): # -1, 0, 1 compared to current number position in string)
                    if j < 0 or j >= StrLen: # if out of bounds
                        continue
                    if data[i][j] not in "1234567890.": # if a special character
                        s += int(Num[0])
                        
print(s)

