import json

with open('jsonFiles/master.json') as file:
  data = json.load(file)

words = []
query = ""

while (query != "/stop"):
  query = input("Enter your search query: ")
  words = query.split(" ")

  str_object, str_attribute = "", ""

  if("what" in words and "is" in words):    #query 1: what is the <key> of <object>   OR   what is <object>
    
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

    if (str_object != "" and str_attribute != ""):
      print(data[str_object][str_attribute])
    else:
      print("query not found")


##what is the definition of iterative-algorithm 
