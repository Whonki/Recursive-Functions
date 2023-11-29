# Question 3
def question_three(n):
    if n>=0:
        print(n, end = " ")
        question_three(n-2)
        print(n, end = " ")
question_three(8)
print()