def missing_number(array):
    n = len(array) + 1
    total_sum = n * (n + 1) // 2
    array_sum = sum(array)
    missing_value = total_sum - array_sum
    return missing_value

print(missing_number([1, 2, 4]))
print(missing_number([1, 2, 3, 4, 6]))
