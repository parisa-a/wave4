# getting user input for the dictionary (both keys and values)
user_input = input("Please enter the number of key/value pairs in your dictionary: ")

# making a dictionary out of the input values 
user_dict = {}
for i in range(int(user_input)):
    user_key = input("Please enter the key: ")
    user_value = input("Please enter the value: ")
    user_dict[user_key] = user_value

# defining the value user is searching for 
search_value = input("Please enter the value you would like to lookup: ")

# function to find keys and values 
def reverseLookup(user_dict, search_value):
    keys = list()
    for values in user_dict.items():
        if values[1] == search_value:
            keys.append(values[0]) 
    return(keys)

print(reverseLookup(user_dict, search_value))