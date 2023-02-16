# 1) Squares
def getSquaresUpUntil(until: int):
    num = 1
    while num <= until:
        yield num ** 2
        num += 1


# for i in getSquaresUpUntil(5):
#     print(i)


# 2) Even

def getEvenUpUntil(until: int):
    num = 0
    while num <= until:
        yield num
        num += 2


# userInput = int(input())
#
# print(*[i for i in getEvenUpUntil(userInput)], sep=",")


def getDivNumbersUntil(until: int):
    num = 1
    while num <= until:
        if num % 3 == 0 and num % 4 == 0:
            yield num
        num += 1


# userInput = int(input())
#
# print(*[i for i in getDivNumbersUntil(userInput)], sep=",")


# 4) Get Squares from a to b
def getSquaresInRange(a: int, b: int):
    while a <= b:
        yield a ** 2
        a += 1






