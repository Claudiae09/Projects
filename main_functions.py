
#json can be imported does not need to be installed
import json

#goal of save to file: to save the data.
#a file name was created
def save_to_file(data,file_name):
    with open(file_name,'w') as write_file: #with created a block in python for a certain action to take place. the with word is to open a file. The W command is to have write permission.
        json.dump(data,write_file,indent=4)
        print('The file {0} was successfully created.'.format(file_name))

#goal of the function is to read the json file that ws created
def read_from_file(file_name):
    with open(file_name,'r') as read_file: #R is used to read the file
        data=json.load(read_file) #method from load. It requires a method to be assigned to.
        print('You successfully read from {0}.'.format(file_name))
        return data