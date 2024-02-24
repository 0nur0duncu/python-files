#decision stetements (if-elif-else)
#----------------------------------------

age = int(input("Please enter your age :"))
if age >= 18:
    print("You can get the driver licence.")
else:
    print("You cannot get the driver licence.")

#single else error
#else: #SyntaxError: invalid syntax
#    print("Life is good.")

name = input("Please enter your name :")
s_name = "george"
if name == s_name:
    print("welcome "+name +"...")
else:
    print("Access denied")

grade = int(input("please enter your quiz grade :"))
if grade>100:
    print("invalid grade")
elif grade < 50:
    print("Fail")
else:
    print("Pass")

#single elif error
#elif True: #SyntaxError: invalid syntax
#    print("Life is good.")

midtermExam = float(input("Please enter your midterm exam"))
finalExam = float(input("Please enter your final exam"))
average = (0.4 * midtermExam) + (0.6 *finalExam)

print("Average of your exams:",end=" ")
if average > 50:
    if (average >=85) and (average <=100):
        print("AA")
    elif (average >=75) and (average <85):
        print("BA")
    elif (average >=70) and (average <75):
        print("BB")
    elif (average >=65) and (average <70):
        print("CB")
    elif (average >=60) and (average <65):
        print("CC")
    elif (average >=55) and (average <60):
        print("DC")
    elif (average >=50) and (average <55):
        print("DD")
    else:
        print("Invalid average")
else:
    print("\"FF\"")