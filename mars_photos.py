import requests, main_functions

# NASA's API url
url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key="

# Read your NASA API key
all_keys = main_functions.read_from_file("api_keys.json")
nasa_key = all_keys["nasa_key"]

#Build the final API url
final_url = url + nasa_key

#Make the API request
#response = requests.get(final_url).json()

#Serialize the result to a JSON document
#main_functions.save_to_file(response, "mars_photos.json")

#Deserialize the recently create JSON document
mars_photos = main_functions.read_from_file("mars_photos.json")

#What is the type of the object deserialized?
print(type(mars_photos))

#What are its keys?
print(mars_photos.keys())

#Access some of their values and their types passing their keys
print(mars_photos["photos"][0]["img_src"])
print(mars_photos["photos"][0]["camera"]["full_name"])

#Create a set containing the names of all cameras
camera_list=[]
for i in mars_photos["photos"]:
    camera_list.append(i["camera"]["full_name"])
print(set(camera_list))

#Print the image source of the photos taken by the Navigation Camera
for j in mars_photos["photos"]:
    if j["camera"]["full_name"]=="Navigation Camera":
        print(j["img_src"])

#Create a function that takes in a dictionary and a camera name
# and prints the image sources of all photos taken by the camera
# passed as argument and test this function.
def get_img_src(dataset,camera_name):
    for n in dataset["photos"]:
        if n["camera"]["full_name"]==camera_name:
            print(n["img_src"])

get_img_src(mars_photos, 'Navigation Camera')