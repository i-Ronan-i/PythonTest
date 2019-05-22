# getting today's date
from datetime import date
today = date.today()
#changes date format
d1 = today.strftime("%d/%m/%Y")
print("Today's date:", d1)

# gets inputs of name and DoB
name = str(input("What is your name? "))
dateob = str(input("DoB, {} you biatch? (dd/mm/yyyy) ".format(name.title())))

# gets just the numerical parts of the date and DoB, for no real reason 
# - could just use int(dateob[:]) function anyway I think.
datetrans = (d1[0:2] + d1[3:5] + d1[6:10])
dobtrans = (dateob[0:2] + dateob[3:5] + dateob[6:10])


if (int(datetrans[3:5]) - int(dobtrans[3:5])) >= 0 :
    # birthday month is this month or passed.
    extrayear = True
    if (int(datetrans[0:2]) - int(dobtrans[0:2])) < 0 :
        #but the date hasn't passed.
        extrayear = False
else :
    #birthday hasn't passed otherwise
    extrayear = False

if extrayear:
    #if your birthday has already been this year your age is standard.
    age = int(datetrans[4:]) - int(dobtrans[4:]) 
    diff = 100 - age
else :
    age = int(datetrans[4:]) - int(dobtrans[4:]) -1
    # to account for the birthday still to come this year
    diff = 100 - age - 1

print ("{}, you are {} years old, you dickhole".format(name,str(age)))
bday100 = int(datetrans[4:]) + diff
print ("You will turn 100 on " + dateob[0:6] + str(bday100))

reptex = str(input("Lets get reppin... "))
for times in range(0, age):
    print(reptex)