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
list_a_z = list(string.ascii_lowercase)
high_values = {}
high_indexes = {}
for x in list_a_z:
    high_values[x] = 0

for i in range(len(list3)): #traverse through each list element
    for j in range(i+1,len(list3)): #counter for the next lists after 'i'
        if list3[i][1] == list3[j][1] : #if the keys are same
            if list3[i][2] > list3[j][2]: #compare the values

                added_key.append(str(list3[i][1])) #add the key value to this tracker list
                #add the value and index to the respective high dictionaries after comparing
                if list3[i][2] > high_values[list3[i][1]]:
                    high_indexes[list3[i][1]] = list3[i][0]
                    high_values[list3[i][1]] = list3[i][2]


            else:

                added_key.append(str(list3[j][1])) #add the key value to this tracker list
                # add the value and index to the respective high dictionaries after comparing
                if list3[j][2] > high_values[list3[j][1]]:
                    high_indexes[list3[j][1]] = list3[j][0]
                    high_values[list3[j][1]] = list3[j][2]



for i in range(len(list3)): #those keys which are only in one dict, then add them directly without modifying the key
    if list3[i][1] not in added_key:
        dict4[list3[i][1]] = list3[i][2]

for keys,values in high_indexes.items(): #add those keys which are present more than once
    dict4[keys +'_'+ str(values)] = high_values[keys]

print(dict4) #print the output dict