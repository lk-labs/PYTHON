def myfunction(n):
    return lambda a:a*n
mydoubler=myfunction(2)
mytripler=myfunction(5)
print(mydoubler(12))
print(mytripler(10))