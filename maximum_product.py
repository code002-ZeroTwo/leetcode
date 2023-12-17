def maxProduct(nums):
    firstmax = float('-inf')
    secondmax = float('-inf')

    for i in nums:
        if firstmax < i:
            secondmax = firstmax
            firstmax = i


        elif firstmax >= i and secondmax < i:
            secondmax = i

    print(firstmax)
    print(secondmax)
    return (firstmax - 1) * (secondmax - 1)


print(maxProduct([1,5,4,5]))