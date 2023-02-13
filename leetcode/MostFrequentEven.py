def mostFrequentEven(nums) -> int:
    hm = {}
    for x in nums:
        if x % 2 == 0:
            hm[x] = {0}

    for c in nums:
        if c % 2 == 0:
            hm[c] = hm[c] + 1

    for key, value in hm.items():
        print(key, value)

    return 0


list = [3, 2, 4, 3]
mostFrequentEven(list)
