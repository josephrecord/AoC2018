from collections import Counter

ids = []
test = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']

count2 = 0
count3 = 0

with open("C:\\Users\\jrecord\\Documents\\GitHub\\AoC2018\\AoC2018_day2.txt") as f:
        for line in f:
            ids.append(line.strip())
        print(ids)
        
        
#          PART ONE
#          line = f.readline()
#         print(line)

#         c = dict(Counter(line))
        
#         if 2 in c.values():
#             count2 += 1
#         if 3 in c.values():
#             count3 += 1

#         cnt = 1


#         while line:
#             line = f.readline()
#             c = dict(Counter(line))
#             if 2 in c.values():
#                 count2 += 1
#             if 3 in c.values():
#                 count3 += 1
#             cnt += 1

# print(count2*count3)

for i in range(len(ids)):
    for j in range(len(ids)):
        c = Counter(ids[i])
        d = Counter(ids[j])
        if len(c - d) == 1 and len(d - c) == 1:
            print(ids[i])
            print(ids[j])
            print(c-d)
            print(d-c)
            break