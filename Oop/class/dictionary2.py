mydict={"Name":"lucy","StudentNo":"1045121","unit":"cmt 210","course":"computer science","Faculty":"scince"}
print(mydict["course"])
print(mydict["Name"])
print(mydict.keys())
print(mydict.values())
print(mydict.items())
print(mydict.get("course"))
mydict.update({"lec":"mr kioko","year":"2023"})
mydict["year"]=2000
print(mydict)