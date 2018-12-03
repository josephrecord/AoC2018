from collections import Counter

count2 = 0
count3 = 0

with open("C:\\Users\\jrecord\\Documents\\GitHub\\AoC2018\\AoC2018_day2.txt") as f:
        line = f.readline()
        print(line)

        c = dict(Counter(line))
        
        if 2 in c.values():
            count2 += 1
        if 3 in c.values():
            count3 += 1

        cnt = 1


        while line:
            line = f.readline()
            c = dict(Counter(line))
            if 2 in c.values():
                count2 += 1
            if 3 in c.values():
                count3 += 1
            cnt += 1

print(count2*count3)


