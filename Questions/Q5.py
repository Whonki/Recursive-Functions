# Question 5
def question_five(x,y):
    if y == 1:
        return x
    else: 
        return x*question_five(x,y-1)
print(question_five(4,3))
print()