s = 0

with open("input.txt", "r") as f:
    for enum, line in enumerate(f.readlines()):
        
        line = line.split(": ")[1][:-1] # take the info after game x: ; [:-1] removes the \n
        line = line.replace(";", ",") # replace ; with , to make it easier to split
        line = line.split(", ")
        r = []
        g = []
        b = []
        for item in line:
            if ("red" in item):
                r.append(int(item.split(" ")[0]))
            if ("green" in item):
                g.append(int(item.split(" ")[0]))
            if ("blue" in item):
                b.append(int(item.split(" ")[0]))
        
        r = max(r)
        g = max(g)
        b = max(b)
        s += r*g*b
    
print(s)