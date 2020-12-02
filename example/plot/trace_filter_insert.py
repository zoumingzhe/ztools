from ztools import filebase
from ztools import plot

filter_slotn = []
filter_slots = []
filter_storen = []
filter_stores = []

for i in range(16):
    filter_slotn.append(0)
    filter_storen.append(0)

with open(".\\trace.log", 'r') as trace:
    print('begin')
    eachline = trace.readline()
    while eachline:
        line = eachline.split('\t')
        for i in range(len(line)):
            line[i] = line[i].strip()
        if line[0] == 'BAK_FILTER' and line[2][:6] == "INSERT":
            filter_stores.append(line[2][-28:])
        eachline = trace.readline()
    print('end')
    trace.close()

filter_stores.sort()
with open(".\\filter_stores.log", 'w') as filter:
    for store in filter_stores:
        i = int('0x'+store[5:9], 16)
        filter_storen[i-1] = filter_storen[i-1] + 1
    print(filter_storen)
    for n in range(len(filter_storen)):
        min_slots = int(filter_storen[n] * 2)
        filter_slotn[n] = min_slots - min_slots % 128 + 128
    print(filter_slotn)
    for n in range(len(filter_slotn)):
        filter_slots.append([0] * filter_slotn[n])
        #print(filter_slotn[n], len(filter_slots[n]))
        
with open(".\\filter_stores.log", 'w') as filter:
    for store in filter_stores:
        i = int('0x'+store[5:9], 16)
        a = int('0x'+store[10:18], 16)
        b = int('0x'+store[19:23], 16)
        c = a + b
        d = c % filter_slotn[n]
        #print('INSERT', i, a, b, c, d)
        filter_slots[i-1][d] = filter_slots[i-1][d] + 1
        filter.write(store)
        filter.write(' ')
        filter.write(str(i))
        filter.write(' ')
        filter.write(str(a))
        filter.write(' ')
        filter.write(str(b))
        filter.write(' ')
        filter.write(str(c))
        filter.write(' ')
        filter.write(str(d))
        filter.write('\n')
    filter.close()

fb = filebase()
fb.ensure(".\\slots-auto")
plts = plot('slots--auto')
for i in range(len(filter_slots)):
    with open(".\\slots-auto\\slot-"+str(i)+".log", 'w') as filter:
        filter_slot = filter_slots[i]
        plt = plot('slot-'+str(i)+'-'+str(filter_slotn[i]))
        points = []
        #print(len(filter_slot))
        x = []
        y = []
        for n in range(filter_slotn[i]):
            #print(n, filter_slot[n])
            filter.write(str(n))
            filter.write(' ')
            filter.write(str(filter_slot[n]))
            ##points.append(plt.point(n, filter_slot[n], filter_slot[n] + 1))
            x.append(n)
            y.append(filter_slot[n])
            filter.write('\n')
        ##plt.scatter(points)
        ##plts.scatter(points)
        plt.xybar(x, y)
        plts.xyscatter(x, y)
        plt.save('.\\slots-auto\\slot-'+str(i)+'.png')
        #plt.show()
        filter.close()
plts.save('.\\slots-auto\\slots-auto.png')
    
input("按任意键退出")