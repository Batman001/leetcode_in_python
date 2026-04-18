
def function(nums, k):
    stack = []
    for num in nums:
        while k > 0 and stack != [] and stack[-1] > num:
            stack.pop()
            k -= 1
        stack.append(num)

    return ''.join(stack)


if __name__ == '__main__':
    nums = "1432219"
    k = 3
    print(function(nums, k))
