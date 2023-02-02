def multipleThree(a,b,c):
    return a*b*c

def muplitpleUnknown(*args):
    res = 1;
    for i in args:
        res*=i
    return res

def factor(n):
    factorial = 1;
    for i in range(1, n+1):
        factorial*=i
    return factorial

def fib(num):
    arr = [0,1]
    for i in range(2, num):
        arr.append(arr[i-1]+arr[i-2])
    return arr[num-1]

def fib_recur(num):
    if num == 1:
        return 0
    if num == 2:
        return 1
    return fib_recur(num-2)+fib_recur(num-1)


print(multipleThree(1,2,3))
print(muplitpleUnknown(3,4,343434,1,2,3))
print(factor(3))
print(fib(100))
print(fib_recur(100))