
inputStr = ["eat", "tea", "tan", "ate", "nat", "bat"]

hlist = []
for _ in range(len(inputStr)):
    hlist.append({})

for i in range(len(inputStr)):
    str = inputStr[i]
    for s in str:
        if s in hlist[i]:
            hlist[i][s] += 1
        else:
            hlist[i][s] = 1

print(hlist)