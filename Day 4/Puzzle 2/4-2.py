with open("input.txt", 'r') as f:
    Fdata = f.readlines()
    CardList= [1] * len(Fdata)
    
    for enum, line in enumerate(Fdata):
        Points = 1
        data = line.split(": ")[1].split("| ")  # get the Card data and the Winning Data
        data[1] = data[1][:-1]  # remove \n
        Card = data[0].split()  # make list of card
        Check = data[1].split()  # make list of winning data
        for item in Card:
            if item in Check:
                CardList[enum+Points] += CardList[enum] # add to the next card(s)
                Points += 1 # increment the Card counter

print(sum(CardList))
