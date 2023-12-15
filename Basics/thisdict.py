thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": "red"
}
#print(thisdict.keys())
#print(thisdict.values())
#print(thisdict.items())
#print(thisdict["brand"])
#print(thisdict.get("year"))
#thisdict["lecturer"]="kamau"
thisdict.update({"colors":"white"})
thisdict.pop("year")
del thisdict["brand"]
print(thisdict)
for x in thisdict:
    print(thisdict)
