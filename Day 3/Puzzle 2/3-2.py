import re

def find_numbers(string):
    matches = re.finditer(r'\d+', string)
    return [(match.group(0), 
            list(range(match.start(), match.end())))
            for match in matches] # (number, [positions the number is in])

s = 0

with open("input.txt", "r") as f:
    data = f.readlines()
    StrLen = len(data[0][:-1]) # -1 to remove \n, all strings are the same length
    DataLen = len(data)
    
    for enumL, line in enumerate(data): # enumerate over line and characters
        for enumC, char in enumerate(line):	
            if char == "*":
                Cnums = []
                for i in range(enumL-1, enumL+2): # -1, 0, 1 compared to current line
                    if i < 0 or i >= DataLen:
                        continue
                    Nums = find_numbers(data[i]) # check all instances of numbers in the line
                    for num in Nums:
                        if (enumC in num[1]) or (enumC-1 in num[1]) or (enumC+1 in num[1]): # check if the * is surrounded by a number
                            Cnums.append(int(num[0]))

                if len(Cnums) == 2:
                    s += Cnums[0] * Cnums[1]
                
print(s)

