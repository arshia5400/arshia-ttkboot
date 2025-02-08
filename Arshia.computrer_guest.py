import random

random_number=random.randint(1,100)
print('welcome to this game')
print("please guess the computer guess")

while True:
    try:
        user_guess=int(input('Enter your guess:'))
        if user_guess==random_number:
            print("congratulation!,your guess like computer guess:")
        elif user_guess>random_number:
            print("it,s higher than computer guess!" )
        else:
            print("it,s lower than computer guess!")
    except ValueError:
        print("Invalid input! Please enter a valid number.") 
