#W3School
# def my_function():
#   print("Hello from a function")

# my_function()

# #arguments
# def my_function2(fname):
#   print(fname + " Refsnes")

# my_function2("Emil")
# my_function2("Tobias")
# my_function2("Linus")

# def my_function3(fname, lname):
#   print(fname + " " + lname)

# my_function3("Emil", "Refsnes")

# #arbitrary args
# def my_function4(*kids):
#   print("The youngest child is " + kids[2])

# my_function4("Emil", "Tobias", "Linus")

# def my_function5(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_function5(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# #Arbitrary Keyword Arguments
# def my_function6(**kid):
#   print("His last name is " + kid["lname"])

# my_function6(fname = "Tobias", lname = "Refsnes")

# #Default Value
# def my_function7(country = "Norway"):
#   print("I am from " + country)

# my_function7("Sweden")
# my_function7("India")
# my_function7()
# my_function7("Brazil")


# #Passing list
# def my_function8(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function8(fruits)



# #Return
# def my_function9(x):
#   return 5 * x

# print(my_function9(3))
# print(my_function9(5))
# print(my_function9(9))


# #Pass
# def myfunction10():
#   pass


# #Recursion
# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)

#**********************
#Functions1
import math
from itertools import permutations 
import random



def fromGramsToOunces(grams: float):
  return 28.3495231 * grams

def fromFarToCel(temp: float):
  return ((5 / 9) * (temp - 32))

def puzzleSolver(numheads: int, numlegs: int):
  chicken = ((numlegs-4*numheads)//(-2))
  rabbits = numheads - chicken
  return f"There are rabbits: {rabbits} and chicken: {chicken}"


def isPrime(num: int):
  for i in range(2, int(math.sqrt(num))+1):
    if num % i == 0:
      return False
  return True


def filter_prime(nums: list):
  return [i for i in nums if isPrime(i)]


def permutation():
  userInput = input()
  perm = permutations(userInput)

  for i in perm:
    print("".join(i))


def inverseSentence():
  userInput = input().split()
  for i in userInput[::-1]:
    print(i, end=" ")

def findThreesTogether(nums: list):
  first = 0
  second = 0

  while first <= len(nums)-1 and second <= len(nums)-2:
    if nums[first] == nums[second+1] and nums[first] == 3:
      return True
    first+=1
    second+=1

  return False


def findCombination(nums: list):
  res = ""
  for i in nums:
    if i == 0 or i == 7:
      res+=str(i)

  return True if res.find("007") >=0 else False


def findVolumeOfSphere(radious: float):
  return (4/3)*math.pi*(radious**3)



def uniqueElWithoutSet(nums: list):
  counter = {}
  for i in nums:
    if counter.get(i) is None:
      counter[i] = nums.count(i)
  return list(counter.keys())


def isPalindrome(word: str):
  start = 0
  end = len(word)-1
  while start < end:
    if(word.lower()[start] == word.lower()[end]):
      start+=1
      end-=1
    else: return False
  return True


def printHistogram(heights: list):
  for i in heights:
    print("*"*i)


def guessNumber():
  num = random.randint(0, 20)
  name = input("Hello! What is your name?\n")

  guess = -1
  count = 1

  print("Well, KBTU, I am thinking of a number between 1 and 20.")
  
  while guess != num:
    print("Take a guess.")
    guess = int(input())
    if guess == num:
      print(f"Good job, KBTU! You guessed my number in {count} guesses!")
    elif guess < num:
      print("Your guess is too low.")
    elif guess > num:
      print("Your guess is too high")
    count+=1

guessNumber()




