import random
import string
import pandas as pd

num_dicts = random.randint(2,8) #random number for number of dictionaries
num_ele = random.randint(1,8) #random number for no_of_elements in a dict
list1 = []

for i in range(num_dicts):
    my_keys = 'x' #initialization
    my_values = 0
    dict1 = {} #assign empty dict
    for j in range(1,num_ele):
        my_key = random.choice(string.ascii_lowercase) #generate random chars and integers and add to the dicts
        my_value = random.choice(range(100))
        dict1[my_key] = my_value
    list1.append(dict1) #append the dict to the list


print(list1)


list3 = []

#create a list of index, key, value after traversing all the dicts present in the list
for index,dicts in enumerate(list1):
    for keys,values in dicts.items():
        list3.append([index+1,keys,values]) #create list of lists


print(list3)
#if you want to solve using dataframes
df = pd.DataFrame(list3,columns=['index','keys','values'])


dict4 = {}
added_key = []

for i in range(len(list3)): #traverse through each list element
    for j in range(i+1,len(list3)): #counter for the next lists after 'i'
        if list3[i][1] == list3[j][1] : #if the keys are same
            if list3[i][2] > list3[j][2]: #compare the values
                dict4[str(list3[i][1]) + '_' + str(list3[i][0])] = list3[i][2] #update the key value and insert in new dict4
                added_key.append(str(list3[i][1])) #add the key value to this tracker list
                #exchange the elements if the left i value is higher
                temp = list3[i]
                list3[i] = list3[j]
                list3[j] = temp

            else:
                #if j value is higher then update the key value accordingly and add to the dictionary
                dict4[str(list3[j][1]) + '_' + str(list3[j][0])] = list3[j][2]
                added_key.append(str(list3[j][1]))


for i in range(len(list3)): #those keys which are only in one dict, then add them directly without modifying the key
    if list3[i][1] not in added_key:
        dict4[list3[i][1]] = list3[i][2]

print(dict4) #print the output dict