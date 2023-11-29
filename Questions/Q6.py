# Question 6
def question_six(n):
    if n> 0:
        print(n, end = " ")
        question_six(n-2)
question_six(2)
print()