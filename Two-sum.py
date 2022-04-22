def two_sum(numbers, target):
    complements = {}
    for x in range(len(numbers)):
        complement = target - numbers[x]

        if numbers[x] in complements:
            return [complements[numbers[x]], x]
        else:
            complements[complement] = x
