myDictionary = {
    "ema" : "apple",
    "jose" : "banana",
    "manu" : "pineapple"
}

print(myDictionary)
print(type(myDictionary))

print(myDictionary.items())

for key, value in myDictionary.items() :
  print(key + " = " + value)
