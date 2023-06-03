arr = [0, 1, 2, 2, 1, 0]

freq = {}

for a in arr:
    if a in freq:
        freq[a] += 1
    else:
        freq[a] = 1

print(freq)

ans = []

freq_keys = list(freq.keys())
freq_keys.sort()

print(freq_keys)

for k in freq_keys:

    val = freq[k]

    for i in range(val):
        ans.append(k)

print(ans)