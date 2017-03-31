print "What is your name?"

name = raw_input()

# Gets everything from one past the first space to the end of the name
firstandlast = name[name.find(' ')+1:]

# get everything from the beginning to the first space
first = firstandlast[:firstandlast.find(' ')]

print first

print "What is your address?"

address = raw_input()
mylist = address.split(' ')
street = mylist[1]+" "+mylist[2]
print street

fullname = name.split(' ')
fullname.remove(fullname[1])
uppercasename = ""
listlength = len(fullname)
counter = 1
for element in fullname:
    uppercasename += element.upper()
    if (counter != listlength):
        uppercasename+ " "
    counter = counter + 1
print uppercasename

print "Dear John: My name is A. M. Aswindler, and I am running a contest for a $1000 gift certificate to The Melting Pot in Miami.  I have wonderful news, you are a finalist in this sweepstakes and may soon be the luckiest person on Main Street!  MR. DOE, DO NOT PASS UP THIS OFFER!  Please fill out your account information at the following site: http://www.swindler.net.  Good luck!"
