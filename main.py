# Homework
# Write a program that solves the quadratic equation with one or more real roots.
# The coefficients can be real numbers i.e., floats.
# Your program should behave as shown below.

# PART 1
print("I can solve ax^2 + bx + c = 0 for you! ")

# PART 2
while True:
    try:  # Use 'try' command to try to input something, if it is not a number, it goes error, but do not worry, we can print that is not a real number by 'except' command.
        a = float(input("Please give me the 'a' coefficient: "))  # get the a
        b = float(input("Please give me the 'b' coefficient: "))  # get the b
        c = float(input("Please give me the 'c' coefficient: "))  # get the c
        delta = (b**2) - (4*a*c)  # calculate the delta to judge whether it has real roots.
        if a == 0:
            print("Sorry, but 'a' cannot be zero.")
        elif delta < 0:  # Check the delta and judge whether it is smaller than 0. If it is smaller than 0, the quadratic equation will does not have real roots.
            print("Sorry, but that quadratic does not have real roots.")
        else:  # Calculate the two roots
            root1 = ((-b) + (delta**0.5)) / (2*a)
            root2 = ((-b) - (delta**0.5)) / (2*a)
            print("Thank you, that is a valid input :) OKAY I'LL SOLVE IT NOW.")
            print("Root 1: ", root1)
            print("Root 2: ", root2)
            break  # break out from the loop.
    except:
        print("That is not a real number!")  # If it the a or b or c are not a number, then through it step.

quit()