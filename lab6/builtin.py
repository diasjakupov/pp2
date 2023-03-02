import time
import math

def multiplyList(data: list):
    res = 1
    for i in range(len(data)):
        res *= data[i]
    print(res)


def calcLetters(data: str):
    upper = 0
    lower = 0
    for i in range(len(data)):
        if 65 <= ord(data[i]) <= 90:
            upper += 1
        elif 97 <= ord(data[i]) <= 122:
            lower += 1
    print(upper, lower)


def isPalindrome(data: str):
    print(data == "".join(list(reversed(data))))

def calcSquareIn(num: int, timeout: int):
    time.sleep(timeout / 1000)
    print(math.sqrt(num))

def validateTuple(data: tuple):
    print(all(data))

multiplyList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
calcLetters("Hello")
isPalindrome("abadaba")
calcSquareIn(25100, 2000)
validateTuple((True, True, True))
