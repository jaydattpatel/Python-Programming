''' 
author : Jaydatt

The following techniques will be covered in this section:

json.loads(json string) : convert data from JSON format string to dictionary
json.dumps(list or set) : convert data from dictionary to JSON format string

Sr. 	Python Objects	|         JSON
1.  	Dict	        |         Object
2.  	list tuple	    |         Array
3.  	Str	            |         String
4.  	int, float	    |         Number
5.  	True	        |         true
6.  	False	        |         false
7.  	None	        |         null

JSON stands for JavaScript Object Notation. It looks a lot like the representation of nested dictionaries and lists in python when we write them out as literals in a program, but with a few small differences (e.g., the word null instead of None). When your program receives a JSON-formatted string, generally you will want to convert it into a python object, a list or a dictionary.

Again, python provides a module for doing this. The module is called json. We will be using two functions in this module, loads and dumps.

json.loads() takes a string as input and produces a python object (a dictionary or a list) as output.

json.dumps() function we will use is dumps. It does the inverse of loads. It takes a python object, typically a dictionary or a list, and returns a string, in JSON format. It has a few other parameters. Two useful parameters are sort_keys and indent. When the value True is passed for the sort_keys parameter, the keys of dictionaries are output in alphabetic order with their values. The indent parameter expects an integer. When it is provided, dumps generates a string suitable for displaying to people, with newlines and indentation for nested lists or dictionaries. 

The indent parameter specifies the spaces that are used at the beginning of a line. We can use the indent parameter of json.dump() to specify the indentation value. By default, when you write JSON data into a file, Python doesn't use indentations and writes all data on a single line, which is not readable.
'''


import json

# convert data from JSON string to dictionary
print("----------convert data from JSON to dictionary-------------")
file_string = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
print("JSON: ",file_string)
# get List of data from string to dictionary
d = json.loads(file_string)
print("------")
print(type(d))
print(d.keys())
print(d['resultCount'])
# print(file_string['resultCount'])


# convert data from dictionary to JSON format
print("----------convert data from dictionary to JSON format-------------")

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

d = {'key1': {'c': True, 'a': 90, '5': 50}, 'key2':{'b': 3, 'c': "yes"}}

print("Dictionary: ", d)
print('--------')
print("JSON: ", pretty(d))