#LOOP FUNCTONS
#exp = (12, 18, 10, 19, 23, 10)
#print (exp)
#print(len(exp))

exp = []
stopped = False

while not stopped:
    e = int(input ('what is the expense (type 0 to stop)'))
    if e!=0:
        exp.append(e)
    else:
        stopped= True
print (exp)
print ('max expenses:', max(exp))
print ('total expenses:', sum(exp))

