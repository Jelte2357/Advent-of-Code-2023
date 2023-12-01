s = 0

with open("input.txt", 'r') as f:
    for line in f.readlines():
        Fp = False
        Lp = -1
        for char in line:
            if char in '123456789':
                if Fp == False:
                    Fp = True
                    s += (10*int(char))
                Lp = int(char)
        s += Lp
print(s)
