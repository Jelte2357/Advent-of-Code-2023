s = 0

with open("input.txt", 'r') as f:
  for line in f.readlines():
    Points = 0
    data = line.split(": ")[1].split("| ")  # get the Card data and the Winning Data
    data[1] = data[1][:-1]  # remove \n
    Card = data[0].split()  # make list of card
    Check = data[1].split()  # make list of winning data
    for item in Card:
      if item in Check:
        if Points == 0:
          Points += 1
        else:
          Points *= 2
    s += Points

print(s)

# I also wanted to prove I could do this in one line. Though not very readable, here it is:
#print(sum([(item if item<2 else 2**(item-1)) for item in ([len([item for item in (line.split(": ")[1].split("| ")[0]).split() if item in (line.split(": ")[1].split("| ")[1]).split()]) for line in open("input.txt", "r").readlines()])]))