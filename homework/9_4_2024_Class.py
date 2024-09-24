numbers = [3,4,5,6,7]
for i in numbers:
    square = i ** 2
    print("Sqaure of:", i, "is:", square)

# Example from Lecture Friday Sept 6
mystudents = ["Julian", "Walker", "Crispy", "Matt", "Shubh"]
it = iter(mystudents)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

import re

mystring = "Julian is a cool guy"
# return a match at every non white space character
x = re.findall("\S", mystring)
print(x)
if x:
    print("yes! there is a  match")
else:
    print("no, there is not a match")




