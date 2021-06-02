#String concatenation (aka how to put strings together)

name1 = "Naz"
age1 = 28

#Multiple ways to print the variable name1 and age1
print("my name is " + name1 + " and I am " + str(age1))
print("my name is {}".format(name1))
print(f"My name is {name1} and I am {age1}") #preferred way to do this

name = input("What is your name?: ")
age = input("What is your age?: ")
activity1 = input("What is your favourite activity?: ")
emotion = input("How does this make you feel? ")
activity2 = input("What is your 2nd favourite activity?: ")


madlib = f"Hi there, my name is {name} and I'm {age} years old! " \
         f"My favourite activity is {activity1}, it makes me very {emotion}. " \
         f"I also enjoy {activity2}."

print(madlib)