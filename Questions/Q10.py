# Question 10
def question_ten(x,y):
    if x == y:
        return 0
    else: 
        return question_ten(x-1,y)+1
print(question_ten(8,3))
print()