def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)
print(lesser_of_two_evens(2,5))

def animal_crackers(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]
print(animal_crackers("Levelheaded Llama"))

def makes_twenty(n1,n2):
    if n1 + n2 == 20 or n1 == 20 or n2 == 20:
        return True
    else:
        return False
print(makes_twenty(20,10))

def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return "name is too short"
print(old_macdonald("macdonald"))

def master_yoda(text):
    return " ".join(text.split()[::-1])
print(master_yoda("I am home"))

def almost_there(n):
    if ((abs(100 - n) <= 10) or (abs(200 - n) <= 10)):
        return True
    else:
        return "Number out of bounds"
print(almost_there(90))

def has_33(nums):
    for i in range(0, len(nums) - 1):
    # if nums[i] == 3 and nums[i+1] == 3:
        if nums[i:i + 2] == [3, 3]:
            return True
        else:
            return False
print(has_33([1,3,3]))

def paper_doll(text):
    result = ""
    for letter in text:
        result += letter * 3
    return result
print(paper_doll("Mississippi"))

#BLACKJACK: Given three integers between 1 and 11:
#if their sum is less than or equal to 21, return their sum.
#If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
#Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
def blackjack(a,b,c):
    if sum ((a,b,c)) <=21:
        return sum((a,b,c))
    elif 11 in ((a,b,c)) and sum(a,b,c) -10 <= 21:
        return sum((a,b,c)) - 10
    else:
        return "BUST"
print(blackjack(9,9,9))

def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total+= num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total
print(summer_69([2, 1, 6, 9, 11]))

def spy_game(nums):
    code = [0,0,7,'x']
    #as code iterates and pops off the numbers in this code list, once
    #all numbers have been popped off in code list,
    #and all that is left is the 'x' string, then it will return True
    #Since it recognizes that 007 numbers in code list has been popped
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

print(spy_game([1,2,4,0,0,7,5]))

def count_primes(num):
    #check for 0 or 1 input
    if num < 2:
        return 0

    #past this point we're dealing with numbers 2 or greater

    #List to store our prime numbers
    primes = [2]
    #counter that goes up to the input number (using number 3 because it
    #adds the bonus impact of being able to go up in steps of 2 and check
    #all odd numbers
    x = 3
    #x is going through every number up to the input number
    while x <=num:
        #check if x itself is a prime number
        #going from 3 to the end range number, in steps of 2, because every
        #even number is by default not a prime number, so we want to go
        #in steps of 2 through every odd number
        for y in range(3,x,2):
            #if statement says if x is divisible by any number in the range,
            #then it is not prime
            if x%y == 0:
                #then we go up in 2 steps to skip past the even number
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
count_primes(100)

def vol(rad):
    return 4/3 * 3.14 * rad**3
print(vol(2))

def ran_check(num,low,high):
    if num in range(low,high+1):
        print(f'{num} is in range of low and high')
    else:
        print(f'{num} is not in the range')
print(ran_check(8,2,7))

def up_low(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])
print(up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))

#OR INSTEAD OF USING DICTONARY METHOD YOU CAN USE A COUNT METHOD

def up_low_alternative(s):
    lowercase = 0
    uppercase = 0
    for letter in s:
        if letter.isupper():
            uppercase += 1
        elif letter.islower():
            lowercase += 1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", ["uppercase"])
    print("No. of Lower case Characters : ", ["lowercase"])

print(up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))


def unique_list(lst):
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

#OR YOU CAN USE A LESS EFFICIENT FOR LOOP TO ITERATE THROUGH

def unique_list_alternative(lst):
    seen_numbers = []
    for number in lst:
        if number not in seen_numbers:
            seen_numbers.append(number)
    return seen_numbers
print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))


def multiply(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total
print(multiply([1,2,3,-4]))


def palindrome(s):
    s = s.replace(' ','')
    return s == s[::-1]
print(palindrome('nurses run'))

import string
def ispangram(str1, alphabet=string.ascii_lowercase):
    #convert alphabet into a set
    alphaset = set(alphabet)
    #remove all spaces in the string to make it run properly
    str1 = str1.replace(" ",'')
    #make all lowercase so you dont get two versions of every letter
    str1 = str1.lower()
    #grab all unique letters from string and place into a set
    str1 = set(str1)
    #return if str1 is == alphaset
    return str1 == alphaset
print(ispangram("The quick brown fox jumps over the lazy dog"))

