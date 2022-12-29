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

print(item_dictionary)