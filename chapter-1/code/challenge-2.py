def a(x):
    return x + 1

def b(x):
    return x + x

def comp(a, b, x):
    return b(a(x))

def main():
    x = int(input('Enter x: '))
    print(comp(a, b, x))

main()
