tuple1 = ("apple","banana","cherry")
print(tuple1[0])
for x in tuple1:
    print(x)

### Dictionary

testDict = {"b":1, "a":2, "c":3}

for key in testDict:
    print(key,testDict[key])
## change item in dict
allKey = testDict.values()

print(allKey)
testDict["e"]=200

for key, values in testDict.items():
  print("key=",key,"value=",values )