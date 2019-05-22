#odd or even

num = float(input("Geez a number..   "))
check = float(input("Divide it by...?     "))

remainder = (num % check)

if remainder == 0:
    print("The number {} is a whole multiple of {}.".format(num, check))
    oddnum = False
else :
    print("The number {} is not a whole multiple of {}.".format(num, check))
    oddnum = True
