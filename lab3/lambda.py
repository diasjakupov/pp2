x = lambda a : a + 10
print(x(5))

x1 = lambda a, b : a * b
print(x1(5, 6))

x2 = lambda a, b, c : a + b + c
print(x2(5, 6, 2))

#Usage
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

mytripler = myfunc(3)

print(mytripler(11))


