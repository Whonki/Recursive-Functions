# Question 4
def question_four(n):
    if n>= 2:
        return 3+ question_four(n//2)
    else:
        return 5
question_four(30)
print()