s = 0

with open("input.txt", 'r') as f:
    for line in f.readlines():
        Flocs = [{1:line.find('one')},
                {2:line.find('two')},
                {3:line.find('three')},
                {4:line.find('four')},
                {5:line.find('five')},
                {6:line.find('six')},
                {7:line.find('seven')},
                {8:line.find('eight')},
                {9:line.find('nine')},
                {1:line.find('1')},
                {2:line.find('2')},
                {3:line.find('3')},
                {4:line.find('4')},
                {5:line.find('5')},
                {6:line.find('6')},
                {7:line.find('7')},
                {8:line.find('8')},
                {9:line.find('9')}]
        Llocs = [{1:line.rfind('one')},
                {2:line.rfind('two')},
                {3:line.rfind('three')},
                {4:line.rfind('four')},
                {5:line.rfind('five')},
                {6:line.rfind('six')},
                {7:line.rfind('seven')},
                {8:line.rfind('eight')},
                {9:line.rfind('nine')},
                {1:line.rfind('1')},
                {2:line.rfind('2')},
                {3:line.rfind('3')},
                {4:line.rfind('4')},
                {5:line.rfind('5')},
                {6:line.rfind('6')},
                {7:line.rfind('7')},
                {8:line.rfind('8')},
                {9:line.rfind('9')}]
        
        f_locs = [item for item in Flocs if int(next(iter(item.values()))) != -1]
        l_locs = [item for item in Llocs if int(next(iter(item.values()))) != -1]
        Min=min(f_locs, key=lambda x: next(iter(x.values())))
        Max=max(l_locs, key=lambda x: next(iter(x.values())))
        s += next(iter(Min.keys())) * 10 + next(iter(Max.keys()))
        
print(s)
