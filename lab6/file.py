import os
import string


def scanPath(path: str, mode: int):
    dirs = [i for i in os.walk(path)]
    if mode == 0:
        for i in dirs:
            if len(i[1]) != 0:
                print(f"{i[0]}: {i[1]}")
    elif mode == 1:
        for i in dirs:
            print(i[0])
            print(f"{i[1]}: {i[2]}")
            print()
    elif mode == 2:
        for i in dirs:
            if len(i[2]) != 0:
                print(f"{i[0]}: {i[2]}")


def checkAccess(path: str):
    if os.path.exists(path):
        print(f"Existence: {os.access(path, os.F_OK)}")
        print(f"Readability: {os.access(path, os.R_OK)}")
        print(f"Writability: {os.access(path, os.W_OK)}")
        print(f"Executability: {os.access(path, os.X_OK)}")
    else:
        print("File does not exist")


def checkExistence(path: str):
    if os.path.exists(path):
        dir, file = os.path.split(path)
        print(dir, file)


def getNumberOfLines(path: str):
    with open(path) as file:
        print(len(file.readlines()))


def writeListToFile(path: str, data: list):
    with open(path, "a") as file:
        file.writelines(data)


def generateFiles():
    for i in string.ascii_uppercase:
        open(f"{i}.txt", "x")


def copyContent(fromFile: str, toFile: str):
    with open(fromFile) as file1:
        data = file1.read()
    with open(toFile, "w") as file2:
        file2.write(data)


def deleteByPath(path: str):
    if os.path.exists(path):
        os.remove(path)
    else:
        print("Such file does not exists")


deleteByPath("/Users/diasjakupov/Desktop/python projects/pp2/lab6/output2.txt")
