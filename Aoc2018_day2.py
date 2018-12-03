from collections import Counter

l = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']

print(l)



# count2 = 0
# count3 = 0

# with open("C:\\Users\\jrecord\\Documents\\GitHub\\AoC2018\\AoC2018_day2.txt") as f:
#         line = f.readline()
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


# if (c - (c & d)) == 1 and (d - (c & d)) == 1



# for i in range(len(l)):
#     for j in range(len(l)):
#         c = Counter(l[i])
#         d = Counter(l[j])

#         if len(c - d) == 1 and len(d - c) == 1:
#             print(c)
#             print(d)
#             break