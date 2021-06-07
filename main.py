import json
import enchant
import sys
#spell-checker.py

with open('jsonFiles/master.json') as file:
  data = json.load(file)

f = open("object_dict.txt", "w")
for s in data.keys():
  f.write(s+"\n")
f.close()

att_list = []
for obj in data:
  for s in data.get(obj):
    if (s not in att_list):
      att_list.append(s)

f = open("att_dict.txt", "w")
for s in att_list:
  f.write(s+"\n")
f.close()

obj_dict = enchant.PyPWL("object_dict.txt")
att_dict = enchant.PyPWL("att_dict.txt")

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
      if(not obj_dict.check(str_object[0:str_object.index("algorithm")-1])):
        suggestions = obj_dict.suggest(str_object[0:str_object.index("algorithm")-1])
      if(str_object[0:str_object.index("algorithm")-1] in data):
        str_object = str_object[0:str_object.index("algorithm")-1]
      elif(len(suggestions) > 0 ):
        if(suggestions[0] in data):
          print("Object Corrected To: ", suggestions[0])
          str_object = suggestions[0]
    else:
      if(not obj_dict.check(str_object+str("-algorithm"))):
        suggestions = obj_dict.suggest(str_object+str("-algorithm"))
      if(str_object+str("-algorithm") in data):
        str_object = str_object+str("-algorithm")
      elif(len(suggestions) > 0 ):
        if(suggestions[0] in data):
          print("Object Corrected To: ", suggestions[0])
          str_object = suggestions[0]

  if(str_object not in data):
    obj_exists = obj_dict.check(str_object)
    if(not obj_exists):
      suggestions = obj_dict.suggest(str_object)
      if(len(suggestions) >= 1):
        if(suggestions[0] in data):
          print("Object Corrected To: ", suggestions[0])
          str_object = suggestions[0]

  if(str_object in data):
    if(str_attribute not in data[str_object]):
        att_exists = att_dict.check(str_attribute)
        if(not att_exists):
          suggestions = att_dict.suggest(str_attribute)
          if(len(suggestions) > 0):
            print("Attribute Corrected To: ", suggestions[0])
            str_attribute = suggestions[0]
    
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
