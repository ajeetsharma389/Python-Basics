string = '''Sam: Phoenix
Joe: Newyork
Doe: Los Angels
Dave: Phoenix
Pam: Newyork
Steve: Phoenix'''

#### Ex:1 Find number of person living in same city
split_string = string.split("\n")
item_dictionary = {}
for item in split_string:
    ## split again
    split_commas = item.split(":")
    city = split_commas[1]
    person = split_commas[0]
    if city in item_dictionary:
        item_dictionary[city] = item_dictionary[city] + 1
    else:
        item_dictionary[city] = 1
### Print the result 
#print(item_dictionary)
import re

my_string = "This is about python. Python is easy to learn and we have two major version: python2 and python3"

my_pattern = r'python'

### search how many times python appears

#print(re.findall(my_pattern, my_string))

### search how many times python appears  with case senssitive

m_patn = r'\bPython[23]?\b'
## Search operation
#print(re.search(m_patn,my_string))

### Find all operation
#print(re.findall(m_patn, my_string,flags=re.I))

### Now creating pattern object to use same pattern in advanced way

pattern_object = re.compile(m_patn)

print(pattern_object.findall(my_string))
