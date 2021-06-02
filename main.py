import json

with open('jsonFiles/intro to algo.json') as file:
  data = json.load(file)

#print(data["iterative-algorithm"]["definition"])

query = input("Enter your search query: ")
words = query.split(" ")

foundObject = ""
foundKey = ""
att = []

if "of" in words:
  str = ""
  for i in range(words.index("of")+1, len(words)):
    str += words[i]
    if(i != len(words)-1):
      str += "-"
  words.append(str);

for var in data.keys():
  for key in data[var].keys():
    if key not in att:
      att.append(key)

print(att)

for word in words:
  for key in data.keys():
    if key == word:
      foundObject = key

print("")

for word in words:
  for key in att:
    if key == word:
      foundKey = key

print("\n")

print("Found Object: ", foundObject)
print("Found Key: ", foundKey)
print(data[foundObject][foundKey])


##what is the definition of iterative-algorithm 
