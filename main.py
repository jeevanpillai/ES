import json

with open('jsonFiles/master.json') as file:
  data = json.load(file)

words = []
query = ""

while (query != "/stop"):
  query = input("Enter your search query: ")
  words = query.lower().split(" ")

  str_object, str_attribute = "", ""
  image_link = ""

  if("what" in words and "is" in words):    #query 1: what is the <attribute> of <object>   OR   what is <object>
    
    if ("the" in words):
      for i in range(words.index("of")+1, len(words)):
        str_object += words[i]
        if(i != len(words)-1):
          str_object += "-"
    else:
      for i in range(words.index("is")+1, len(words)):
        str_object += words[i]
        if(i != len(words)-1):
          str_object += "-"

    if ("the" in words):
      for i in range(words.index("the")+1, words.index("of")):
        str_attribute += words[i]
        if(i != words.index("of")-1):
          str_attribute += "-"
    else:
      str_attribute = "definition"


  if("how" in words and "work" in words):    #query 2: how does <object> work
    for i in range(words.index("does")+1, words.index("work")):
        str_object += words[i]
        if(i != words.index("work")-1):
          str_object += "-"

  if (str_object != "" and str_attribute != ""):
    print("Object: ", str_object)
    print("Attribute: ", str_attribute)    
    print(data[str_object][str_attribute])
    if(str_attribute+"-img" in data[str_object].keys()):
      print("Image Link: ", data[str_object][str_attribute+"-img"])
  else:
    print("query not found")

##what is the definition of iterative-algorithm 
