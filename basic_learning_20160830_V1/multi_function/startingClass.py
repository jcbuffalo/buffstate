from basic_learning_20160830_V1.multi_function.extraFunctions import adding

def function1():
    a =1
    return a

def main(d):
    b = function1() + d
    print ("b",b)
    return b

q = main(5)
q = q + adding(q,2)
print ("main",q)
