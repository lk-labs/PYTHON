def myfunction(n):
    return lambda a:a*n
result=myfunction(3)
print("the product is ",result(11))