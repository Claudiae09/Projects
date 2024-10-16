import requests, main_functions

#API url
url = "http://api.open-notify.org/astros.json"

#Make the API request

#Serialize the result to a JSON document

#Deserialize the recently create JSON document

#What is the type of the object deserialized?

#What are its keys?

#Access some of their values passing their keys

#What are the names of the astronauts?

#Print their names using a for loop

#Sort their names
for j in sorted(astronautsDict['people'],key = lambda x : x["name"]):
    print(j["name"])