# Chapter 1 Challenge

### 1. Implement, as best as you can, the identity function in your favorite language (or the second favorite, if your favorite language happens to be Haskell).

```
def id(x):
    return x

def main():
    x = input('Enter x: ')
    print(id(x))

main()
```

### 2. Implement the composition function in your favorite language. It takes two functions as arguments and returns a function that is their composition.

```
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
```

### 3. Write a program that tries to test that your composition function respects identity.

```
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
```

### 4. Is the world-wide web a category in any sense? Are links morphisms?

Yes, with webpages as objects and links as the arrows that go between. I would say yes, because they will return the new webpage. I guess in that case the input to the function doesn't really matter since the link will always lead to the same place.

### 5. Is Facebook a category, with people as objects and friendships as morphisms?

I think not necessarily. There aren't identities (people can't be friends with themselves), and if A is friends with B, and B is friends with C, A is not necessarily friends with C.

### 6. When is a directed graph a category?
