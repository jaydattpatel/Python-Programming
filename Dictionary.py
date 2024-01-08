'''
author : Jaydatt
 dictionary
'''
dic = {
    "Name": "Rahul",
    "Gender": "Male",
    "Contacts": {"Mobile": 5646845 , "Email" : "xyz@abc"},
    "Address": {"Country":"India","State":"Mumbai"},
    1: 2}

dic["Age"] = 21 # add or modify value of key
dic['Marks'] = "85%" # add or modify value of key

del dic['Marks'] # delete Marks key and its value
del dic ['Address']['State'] # delete State key and its value

print("----------")
for key in dic :  ## or for key in list(dic.keys()) :
    print( key,": ", dic[key])
print("----------")

# The difference between .get(key) and [key] sytax in Dictionaries?
# if key found then returns value of key, otherwise return None 
print("dic.get('Name') : ", dic.get('Name'))
# if key found then returns value of key, otherwise throws error
print("dic['Name'] : ", dic['Name']) 

print("dic['Age'] : ",dic['Age']) 
print("dic['Contacts']['Email'] : ", dic['Contacts']['Email'])

print("----------list(dic.keys()) : \n", list(dic.keys())) # Prints the keys of the dictionary
print("----------list(dic.values()) : \n", list(dic.values())) # Prints the values of the dictionary 
print("----------list(dic.items()) : \n", list(dic.items())) # Prints the (key, value) for all contents of the dictionary 

print("----------dic: \n",dic)

dic_2 = {
    "Lovish": "Friend",
    "Divya": "Friend",
    "Shubham": "Friend",
    "rahul": "A Dancer"}
 # Updates the dictionary by adding key-value pairs from updateDict
dic.update(dic_2)  

print("----------dic: \n",dic)

'''
we can not take list in set and error generate for example:
s = {8,7,"Amit",[5,6]}

we can take tupel in set but can not modify tupel for example:
s = {8,7,"Amit",(5,6)}
'''
