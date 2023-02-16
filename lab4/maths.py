import math


def convertDegreeToRad(degree: int) -> float:
    return (degree * math.pi) / 180.0


def calcAreaOfTrap(height: int, firstBase: int, secondBase: int) -> float:
    return ((firstBase + secondBase) / 2) * height


def calcAreaOfThePolygon(sides: int, length: int) -> float:
    apothem = length / (2 * math.tan(math.pi / sides))
    perimeter = sides * length
    area = 0.5 * apothem * perimeter
    return area


def calcAreaOfTheParallelogram(height: int, length: int):
    return length * height
