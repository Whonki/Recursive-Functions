# Question 1
def question_one(n):
    if n>=0:
        print(n, end = " ")
        question_one(n-2)
question_one(8)
print()