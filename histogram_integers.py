from collections import Counter

def histogram(seq, bin_size = 5, print_hist = True):
	counts = Counter(seq)
	low, high = min(seq), max(seq)
	hist = {}
	
	for i in range(low, high, bin_size):
		bin_sum = 0
		bin = tuple([i, i + bin_size])
		for x in range(i, i + bin_size):
			if x <= high and x in counts.keys():
				bin_sum += counts[x]
		hist[bin] = hist.get(bin, bin_sum)
		
	if print_hist is True:	
		for k, v in hist.items():
			print(k, ":", "*"*v)
	return hist
	
seq = [1, 2, 3, 4, 5, 7,9, 10, 12, 12, 12]
print(histogram(seq, 5, print_hist = True))