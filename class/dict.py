def dicts(student):
    print(len(student))
    print(student.get("Name"))
    print(student.keys())
    student["Units taken"] = ("7")
    print(student)
    print(student.values())
    student["Name"]=("Cypher")
    print(student)
    print(student.items())
    print("Name" in student)
    student.update({"Age": 40})
    print(student)
    student.pop("Units taken")
    print(student)
    student.popitem() # removes the last inserted item
    print(student)
    del student["Age"]
    print(student)
    #del student
    #print(student)
    #student.clear()
    #print(student)

dicts({
    "Name" : "Brc0d3s",
    "Stdnt_no" : 1045858,
    "Faculty" : "Science",
    "Department" : "Computer science",
    "Age" : 20,
    "Weight" : "75 kg"
})