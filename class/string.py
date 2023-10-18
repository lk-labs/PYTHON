def python(name):

    print(name[2])
    print(len(name))
    print("Hell" in name)
    print("her" not in name)
    print(name[1:])
    print(name[3:5])
    print(name[0:-1])
    print(name.lower())
    print(name.upper())
    print(name.strip())
    print(name.replace("world","python"))
    print(name.split("/"))


python(" Hello/ world")