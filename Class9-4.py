#streamlit run _______.py
import math

print(math.pi)
print(math.factorial(5))
print(math.sqrt(36))
print(math.floor(3.14))
print(math.ceil(3.14))

#list are used to store elements in a specific order
professors = ["greg", "richard", "kianoosh", "debra", "patriacia", "agoritsa"]
#length of the list
print(len(professors))
print(professors[0]) #first element
#calling the 1 element in the list
print(professors[1])
#will print out agoritsa since it is the last one of the list
print(professors[-1])
print(professors[1:4]) #accessing indices 1,2 and 3
print(professors[:3]) # accessing elements in position 0,1, and 2
print(professors[3:]) #accessing elements from position 3 onwards
print(professors[:]) #list all of them
print(professors)

#methods that can make all letters either capitilized, lower case or first letter upper and rest lower case
for j in professors:
    print(j.upper())
    print(j.lower())
    print(j.title())

"""This
is
a
block
comment"""

# append will insert an element to the end of the list
professors.append("micheal")
print(professors)
professors.insert(2,"Jason") #insert will add an element to the specified index
print(professors)
professors[1]="leo" #replacing the value in index 1 with a new value
print(professors)
professors.remove("agoritsa")
print(professors)
x=professors.pop(3)
print(x)
print(professors)
print(professors.index("patricia"))
print(professors.count("greg"))
professors.reserve()
print(professors)
professors.sort()
print(professors)