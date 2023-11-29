# Question 8
def question_eight(n):
    if n ==1 or n == 2:
        return 2* n
    else:
        return question_eight(n-1) - question_eight(n-2)
print(question_eight(5))
print()