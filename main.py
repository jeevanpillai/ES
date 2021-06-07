import json

with open('jsonFiles/master.json') as file:
  data = json.load(file)

words = []
query = ""

while(True):
  query = input("Enter your search query: ")
  if(query == "/stop"): 
    break
  if("?" in query):
    query = query[0:len(query)-1]     ##removes "?" char
  words = query.lower().split(" ")

  str_object, str_attribute = "", ""
  image_link = ""

  if("what" in words and "is" in words):    #query 1: what is the <attribute> of <object>   OR   what is <object>   OR  what is the <attribute> of the <object> 
    
    if ("of" in words):    ## object collector, 
      for i in range(words.index("of")+1, len(words)):
        if(words[i] != "the"):
          str_object += words[i]
        if(i != len(words)-1 and words[i] != "the"):
          str_object += "-"
    else:
      for i in range(words.index("is")+1, len(words)):
        if(words[i] != "the"):
          str_object += words[i]
        if(i != len(words)-1 and words[i] != "the"):
          str_object += "-"

    if ("of" in words):  ## attribute collector, attribute always leads with "the"
      for i in range(words.index("the")+1, words.index("of")):
        str_attribute += words[i]
        if(i != words.index("of")-1):
          str_attribute += "-"
    else:
      str_attribute = "definition"

  if("how" in words and "work" in words):    #query 2: how does <object> work OR how does a <object> work OR how does the <object> work
    str_attribute = "how-work"
    str_search = "does"
    if ("a" in words): str_search = "a"
    if ("the" in words): str_search = "the"
    for i in range(words.index(str_search)+1, words.index("work")):
        str_object += words[i]
        if(i != words.index("work")-1):
          str_object += "-"

  if(str_object not in data):
    if("algorithm" in str_object):
      if(str_object[0:str_object.index("algorithm")-1] in data):
        str_object = str_object[0:str_object.index("algorithm")-1]
    else:
      if(str_object+str("-algorithm") in data):
        str_object = str_object+str("-algorithm")


  if(str_object in data and str_attribute not in data[str_object]):  ## defaults attributes to "definition" if attribute not found in data set
    str_attribute = "definition"

  ##print("Object: ", str_object)
  ##print("Attribute: ", str_attribute)   

  if (str_object in data and str_attribute in data[str_object]): 
    print(data[str_object][str_attribute])
    if(str_attribute+"-img" in data[str_object].keys()):
      print("Image Link: ", data[str_object][str_attribute+"-img"])
  else:
    print("query not found")

  print("")

##what is the definition of iterative-algorithm 
