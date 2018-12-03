freqs = []
subfreq = []
current_freq = 0
i = 0

with open("C:\\Users\\jrecord\\Desktop\\AoC2018_day1.txt") as f:
    line = f.readline()
    line = line.strip("+")
    cnt = 1
    while line:
        freqs.append(int(line))
        line = f.readline()
        line = line.strip("+")
        cnt += 1

print(sum(freqs))

while True:
    res_freq = current_freq + freqs[i]

    if res_freq in subfreq:
        print(res_freq)
        break

    subfreq.append(res_freq)

    current_freq = res_freq
    
    i += 1
    if i == len(freqs):
        i = 0

    

    
    

