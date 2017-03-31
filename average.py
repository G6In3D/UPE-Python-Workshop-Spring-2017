print "Python 101"

# Gets a student's name
print "Enter a student's name:"
name = raw_input()

# Get a number of grades
print "Enter number of grades:"
numgrades = int(raw_input())

# Does something 5 times
sum = 0.0
for i in range(1, numgrades+1):
    print "Enter a grade ", i, ":"
    grade = int(raw_input())
    sum = sum + grade

average = sum / numgrades

print name, "'s average:", average

if (average >= 90):
    print "Letter grade is A"

elif (average >= 80):
    print "Letter grade is B"

elif (average >= 70):
    print "Letter grade is C"

elif (average >= 60):
    print "Letter grade is D"

else:
    print "Letter grade is F"
