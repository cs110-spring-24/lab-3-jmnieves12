print("Options: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
run = input("Enter the problem you want to run: ")
run = int(run)





# 1. Write a program that prints out the numbers 1 to 1000. (+5 points)

if run == 1:
    # Your code for problem 1 goes here
    print("Running problem 1.")
    for number in range(1000): # Edward put for count in range(1, 1001):
        print(number)
    print("Successfully ran problem 1.")






# 2. Write a program that prints out the odd numbers between 1 and 1000. (+5 points)

if run == 2:
    # Problem 2
    print("Running problem 2")
    for number in range(1000): # Edward put for count in range(1, 1001, 2): TO DO THE EVENS ONLY, USING THE STEP PART OF THE FOR FUNCTION
        if number % 2 == 0:
            continue
        print(number)
    print("Successfully ran problem 2.")





# 3. Write a program that prints out the numbers between 0 and 1000 that are divisible by 3. (+10 points)

if run == 3:
    # Problem 3
    print("Running problem 3")
    for number in range(1000):
        if number % 3 == 0:
            print(number)
        else:
            continue
    print("Successfully ran problem 3.")





# 4. Write a program that prints out the numbers between 1 and 1000 that are divisible by 3 or 5. (+10 points)

if run == 4:
    print("Running problem 4")
    for number in range(0, 1001, 1):
        if number % 3 == 0:
            print(number)
        elif number % 5 == 0:
            print(number)
    print("Successfully ran problem 4.")




# 5. Write a program that asks the user to enter a number and prints out all the numbers between 1 and that number that are divisible by 11 or 13.
#The number entered should be greater than 200. (+10 points) Extra credit if the programs asks again if the number is less than 200. (+5 points)

if run == 5:
    print("Running problem 5")
    number = int(input("Enter any number above 200: "))
    if number >= 200:
            
        for number in range(1, number):
            if number % 11 == 0:
                print(number)
            elif number % 13 == 0:
                print(number)
            else:
                continue
        
    elif number <= 200:
        print("You did not enter a number over 200.")
    print("Successfully ran problem 5.")




# 6. Write a program that prints out each letter of a string line by line (+5 points)

if run == 6:
    # Problem 6 code
    print("Running problem 6")
    string = input("Enter a word: ")
    for l in range(len(string)):
        print(string[l])
    print("Successfully ran problem 6.")




# 7. Write a program that asks the user to enter a string and outputs every second letter. The string must be more than 10 letters long. (+10 points)

if run == 7:
    # Problem 7 code
    print("Running problem 7")
    string = input("Enter a word that's MORE than 10 letters long: ")
    if len(string) >= 10:
        for l in range(0, len(string), 2):
            print(string[l])
    elif len(string) <= 10:
        print("You did not enter a word with more than 10 letters.")
    print("Successfully ran problem 7.")




# 8. Write a program that rolls 1000 dice and prints out the number of times each number was rolled. (+15 points)


if run == 8:
    #Problem 8 code
    print("Running problem 8")
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    import random
    timesrolled = 0
    dice = 0
    while timesrolled <= 1000:
        dice = random.randint(1, 6)
        if dice == 1:
            one = one + 1
            timesrolled = timesrolled + 1
        if dice == 2:
            two = two + 1
            timesrolled = timesrolled + 1
        if dice == 3:
            three = three + 1
            timesrolled = timesrolled + 1
        if dice == 4:
            four = four + 1
            timesrolled = timesrolled + 1
        if dice == 5:
            five = five + 1
            timesrolled = timesrolled + 1
        if dice == 6:
            six = six + 1
            timesrolled = timesrolled + 1
        print(dice)

    print(f"You rolled one {one} times, two {two} times, three {three} times, four {four} times, five {five} times, and six {six} times.")




# 9. Write a program that checks if a given number is a prime number.
# A prime number is a number that is only divisible by 1 and itself. The user enters a number and the programs prints out whether the number is a prime number or not. (+15 points)


if run == 9:
    #Problem 9 code
    add = 1
    print("Running problem 9")
    number = int(input("Enter a number to check if it's a prime number: "))
    isprime = True #assuming it's true
    for add in range(2, number): #range needs to NOT be 0, 1 or itself #starting at 2 is correct bc 13/1 is 13
        # if number % add != 0:
        #     continue
        if number % add == 0:
            isprime = False
            break
        # The numbers that make this work come entirely from the for loop. NOT some variable + 1.

    if isprime == True:
        print("Your number IS a prime number.")
    else:
        print("Your number IS NOT a prime number.")





# 10. Write a program that prints out the prime numbers less than 1000. (+20 points)



if run == 10:
    print("Running problem 10")
    for number in range(2, 1001):
        isprime = True
        for add in range(2, number):
            if number % add == 0:
                isprime = False
                break

        if isprime == True:
            print(number)
        #goes back to the outer loop. Inner one just broke.