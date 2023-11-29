# Question 9
def question_nine(n):
    if n == 1 or n == 2:
        return 2*n
    else:
        return question_nine(n-1) - question_nine(n-2)
print(question_nine(-4))
print()