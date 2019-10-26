def histogram(array, k):
    min_val, max_val = min(array), max(array)
    bin_size = (max_val - min_val) / k
    bins = []
    start, end = min_val, min_val
    while start < max_val:
        end = start + bin_size
        bins.append(tuple([start, end]))
        start = end
    counts = {}
    for t in bins:
        for i in array:
            if i == max_val:
                if i >= t[0] and i <= t[1]:
                    counts[t] = counts.get(t, 0) + 1
            else:
                if i >= t[0] and i < t[1]:
                    counts[t] = counts.get(t, 0) + 1
    return counts

print(histogram([1.23, 2.34, 1.23, 4.5], 2))
