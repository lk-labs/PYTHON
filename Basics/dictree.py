thisdict={
    "name":"lucy",
    "faculty":"science",
    "department":"computer science",
    "unit":"cmt 210"

}
#print(thisdict["department"])
thisdict.update({"age":"15"})
print(thisdict)


if "name" in thisdict:
    print("yes")
else:
    print("no")    