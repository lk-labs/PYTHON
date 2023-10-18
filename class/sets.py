def sets(set_1):

    print(len(set_1))
    print("Brc0d3s" in set_1)
    set_1.add("Vivian")
    print(set_1)
    set_1.discard("Brc0d3s")
    print(set_1)
    set_1.remove("Stacy")  # remove() returns error if item is missing while discard() doesn't
    print(set_1)
    set_1.pop()
    print(set_1)  # removes the first value
    set_1.clear()
    print(set_1)
    #del set_1
    #print(set_1)


sets({"Jude","Debby","Ivy","Aby","Stacy","Josh","Brc0d3s",254,354,True,False})