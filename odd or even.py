#odd or even

#gets inputs for numerator and denominator.
num = float(input("Geez a number..   "))
check = float(input("Divide it by...?     "))

#gets the remainded of the division.
remainder = (num % check)

if remainder == 0:
    print("The number {} is a whole multiple of {}.".format(num, check))
    oddnum = False
else :
    print("The number {} is not a whole multiple of {}.".format(num, check))
    oddnum = True
