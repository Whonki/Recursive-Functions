# Question 2
def question_two(n):
    if n>=0:
        print(n, end = " ")
        question_two(n-2)
question_two(8)
print()