"""
This is a letter grade converter program.
"""

score = int(input("Enter your score"))
if (score >= 90 and score <= 100):
    print("You've got A")
elif (score >= 80 and score <= 89):
    print("You've got B")
elif (score >= 70 and score <= 79):
    print("You've got C")
else:
    print("You've got F")
    print("See you next semester")


    
age = int(input("What is your age?\n"))
if (age >= 13):
    print("Your ticket is $10.")
elif (age >= 13 and age <= 59):
    print("Your ticket price is $16.")
elif (age >= 60 and age <= 100):
    print("Your ticket price is $12.")
