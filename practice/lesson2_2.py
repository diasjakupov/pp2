rawDate = input()

def getFormattedDateTime(rawDate):
    format_time = lambda x: x.split(" ")
    date = lambda x: x[0].split("-")
    time = lambda x: x[1];
    
    for i in date(format_time(rawDate)):
        print(i)

    print(time(format_time(rawDate)))

def splitArrayByDiv():
    arr = [1,2,3,4,5,6,7,8]
    even = lambda x: [i for i in x if i % 2 == 0]
    odd = lambda x: [i for i in x if i % 2 == 1]

    print(f"Number of even: {len(even(arr))}")
    print(f"Number of odd: {len(odd(arr))}")


class Animal:
    def breath(self):
        print("Breath")

class Mammal(Animal):
    def walk(self):
        print("Walk")


class Dog(Mammal):
    def bark(self):
        print("Bark")
 


haski = Dog()
haski.walk()
haski.breath()
haski.bark()


getFormattedDateTime(rawDate)
splitArrayByDiv()