# S08 Review of Conditionals (if, elif, else)

# if score >= 90:
#     print("You got an A! Excellent Work")
# elif score >= 60:
#     print("You passed the exam")
# else:
#     print("You did not pass. Better luck next time!")


def evaluate_score(score):
    if score >= 90:
        return "You got an A! Excellent Work"
    elif score >= 60:
        return "You passed the exam"
    else:
        return "You did not pass. Better luck next time!"
    
# score = int(input("Enter your score: "))
# result = evaluate_score(score)
# print(result)

def mystery(x):
    if x > 0:
        return "positive"
    else:
        return "non-positive"
    print("done")

# result = mystery(0)
# print(result)

#x = 15
#y = x > 10 and x < 20
#print(type(y))
#print(y)

def check(n):
    if n % 2 == 0 and n % 3 == 0:
        print(f"{n} is divisible by both 2 and 3")
    elif n % 2 == 0:
        print(f"{n} is divisible by 2 but not by 3")
    else:
        print(f"{n} is not divisible by 2")

check(8)
check(6)