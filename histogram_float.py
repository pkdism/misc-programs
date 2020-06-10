l = [10.2, 11.3, 11.4, 14.5, 17.8]

mn = int(min(l))
mx = int(max(l) + 1)

bin_width = 2

buckets = list(range(mn, mx+1, 2))

hist = {}

for i in range(len(buckets)-1):
	t = tuple([buckets[i], buckets[i+1]])
	hist[t] = hist.get(i, 0)

for x in l:
	index = int((x-mn)//2)
	t = tuple([buckets[index], buckets[index+1]])
	hist[t] += 1

print(hist)
