#Defining Functions
def printName(name):
    print("Your name is", name)   #No need to give space after is when using comma
    print"Your name is", name
    print "Your name is " + name

printName('Roopam')

def power3(number):
    print(number**3)

power3(5)

#Return values
def girlsAgeAllowed(age):
     return age//2 + 7

for age in range(15,61):
    print "The person with age", age, "can date a girl who is at least", girlsAgeAllowed(age), "years old."

#Default arguments
def printwt(wt=70):
    print "Your weight is", wt, "fatty!"

printwt(75)
printwt()

#Keyword arguments
def printThis(name='Roopam', prep='is', adj='awesome'):
    print name, prep, adj

printThis()
printThis(adj='decisive', prep='will always be')
printThis(name='Shubham')

#Flexible number of arguments
def addNumbers(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)

addNumbers(5,98,97,25,36)

#Unpacking arguments
def printBirthday(month, day, year):
    print month, day, year

mydata = ['May', 25, 1991]

printBirthday(*mydata)

 