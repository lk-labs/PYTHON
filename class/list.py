def listers(list_1,list_2):

     list_1[4]=("Arabia")
     print(list_1)
     list_1.insert(1,"Dead")
     print(list_1)
     list_1.append("Takeoff")
     print(list_1)
     list_1.extend(list_2)
     print(list_1)
     list_1.remove(True)
     print(list_1)
     list_1.pop(3)
     print(list_1)
     del list_1[3]
     print(list_1)
     list_1.pop()
     print(list_1)
     del list_1
     print(list_1)
     list_1.clear()
     print(list_1)



listers([1,2,3,"Kenya","Nairobi",True,False],[4,6,7,"Kivitu","Juice world",False,True])