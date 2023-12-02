s = 0

with open("input.txt", "r") as f:
    for enum, line in enumerate(f.readlines()):
        
        line = line.split(": ")[1][:-1] # take the info after game x: ; [:-1] removes the \n
        line = line.replace(";", ",") # replace ; with , to make it easier to split
        line = line.split(", ")
        
        for item in line:
            if ("red" in item) and (int(item.split(" ")[0]) > 12):
                break
            if ("green" in item) and (int(item.split(" ")[0]) > 13):
                break
            if ("blue" in item) and (int(item.split(" ")[0]) > 14):
                break
        else: # for else statements run if the for loop is not broken
            s += enum + 1
    
print(s)