age=int(input("Enter your age: "))
if age>=18:
    print("You are an adult")   #no brackets are used in python, indentation does the work.
else:
    print("You are not an adult")

print("end of program")

day = input("enter the day: ")
if day=="Sunday":
    print("woohoo")
elif day=="Monday":
    print("Go to work")
elif day=="Tuesday":
    print("Hanuman chalisa")
else:
    print("Party")
print("End")

#use hashtag to input a single line comment
'''Use these triple inverted commas to insert
comments in two or more then two lines.
At the end of you multiple line comment again put
these 3 commas to mark the end. it is not needed 
in case of a single line comment'''

a=3
b=5
c=7
if a > b:
    if a > c:
        print(a, 'is largest')
    else:
        print(c, 'is largest')
else:
    if b > c:
        print(b, 'is largest')
    else:
        print(c, 'is largest')

