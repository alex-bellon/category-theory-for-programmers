def id(x):
    return x

def a(x):
    return x + 1

def b(x):
    return x + x

def comp(a, b, x):
    return b(a(x))

def main():
    x = int(input('Enter x: '))
    composition = comp(a, b, x)
    print(composition)
    print(id(composition))
    print(composition == id(composition))

main()
