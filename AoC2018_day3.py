width = 4
length = 4
upperleft = (3,1)
upperright = (upperleft[0] + (width - 1), upperleft[1])
lowerright = (upperleft[0] + (width - 1), upperleft[1] + (length - 1))
lowerleft = (upperleft[0], upperleft[1] + (length - 1))
square = (upperleft, upperright, lowerright, lowerleft)

# print(square)

rec1 = ((1,3), (4,3), (4,6), (1,6))
rec2 = ((3,1), (6,1), (6,4), (3,4))
print(rec1)
print(rec2)

xspan1 = (rec1[0][0], rec1[1][0])
print(xspan1)
yspan1 = (rec1[0][1], rec1[2][1])
print(yspan1)

xspan2 = (rec2[0][0], rec2[1][0])
print(xspan2)
yspan2 = (rec2[0][1], rec2[2][1])
print(yspan2)

if xspan1[0] < xspan2[0] < xspan1[1]:
    xoverlap = xspan1[1] - xspan2[0] + 1
    print(xoverlap)

if yspan1[0] < yspan2[0] < yspan1[1]:
    yoverlap = yspan1[1] - yspan2[0] + 1
    print(yoverlap)

elif yspan1[0] < yspan2[1] < yspan1[1]:
    yoverlap = yspan1[1] - yspan2[1] + 1
    print(yoverlap)