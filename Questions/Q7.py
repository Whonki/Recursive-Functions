# Question 7
def question_seven(n):
    if n< 2:
        return 0
    else:
        return question_seven(n-1) + 2*n
print(question_seven(5))
print()