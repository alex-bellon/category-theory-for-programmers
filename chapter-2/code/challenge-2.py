import random

def memoize(func):
    mem = {}

    def checkMem(num):
        if num not in mem:
            mem[num] = func(num)
        return mem[num]

    return checkMem

@memoize
def rand(num):
    return random.randint(0, num)
