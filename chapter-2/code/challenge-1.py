def memoize(func):
    mem = {}

    def checkMem(num):
        if num not in mem:
            mem[num] = func(num)
        return mem[num]

    return checkMem

@memoize
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)
