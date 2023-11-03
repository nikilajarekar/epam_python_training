import re
import random
import string
import pandas as pd

#Function to normalize the cases
def normalize(str11):
    normal_cased = str11.capitalize()
    return normal_cased

#Function : pattern to match the last word of each sentence by finding the letters and dot at the end
def find_lastword(str1,pattern):
    last_words = re.findall(pattern,normal_case)
    return last_words

#Function to create Sentence
def create_sentence(last_words):
    sentence = ' '.join(last_words)
    # remove the dots
    new_sentence = sentence.replace(".", "", 6)
    return new_sentence

#Function : # find the pos to insert
def find_insert_pos(normal_case):
    insert_pos = normal_case.index('paragraph') + len('paragraph') + 1
    return insert_pos

#function : # insert the sentence at the specified position
def insert_sentence(normal_case,new_sentence,insert_pos):
    added_string = normal_case[:insert_pos] + new_sentence + normal_case[insert_pos:]
    return added_string

#function : # pattern to find the "Iz" only as a full word and replace it with is
def replace_iz(iz_pattern,added_string):
    correct_str = re.sub(iz_pattern, 'is', added_string)
    return correct_str

#function : count whitespaces
def count_whitespaces(pattern, correct_str):
    res = re.findall(pattern, correct_str)
    return len(res)

str1 = '''homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

normal_case = normalize(str1)


pattern = '[a-z]+\.'
last_words = find_lastword(normal_case,pattern)

new_sentence = create_sentence(last_words)

insert_pos = find_insert_pos(normal_case)

inserted_sentence = insert_sentence(normal_case,new_sentence,insert_pos)

iz_pattern = r'\biz\b'
correct_sentence = replace_iz(iz_pattern,inserted_sentence)
print(correct_sentence)

#pattern to find \n \t spaces \r \f
whitespaces_pattern = '\s'

whitespaces_count = count_whitespaces(whitespaces_pattern,correct_sentence)
print(whitespaces_count)

#Collections_Homework

#Functio to create dictionary as specified
def create_dict(num_dicts,num_ele,list1):
    for i in range(num_dicts):
        my_keys = 'x' #initialization
        my_values = 0
        dict1 = {} #assign empty dict
        for j in range(1,num_ele):
            my_key = random.choice(string.ascii_lowercase) #generate random chars and integers and add to the dicts
            my_value = random.choice(range(100))
            dict1[my_key] = my_value
            list1.append(dict1) #append the dict to the list
    return list1

#Function : create a list of index, key, value after traversing all the dicts present in the list
def list_of_index_key_value(list1):
    list3 = []
    for index,dicts in enumerate(list1):
        for keys,values in dicts.items():
            list3.append([index+1,keys,values]) #create list of lists
    return list3

def create_final_dict(list3):
    dict4 = {}
    added_key = []
    list_a_z = list(string.ascii_lowercase)
    high_values = {}
    high_indexes = {}
    for x in list_a_z:
        high_values[x] = 0

    for i in range(len(list3)):  # traverse through each list element
        for j in range(i + 1, len(list3)):  # counter for the next lists after 'i'
            if list3[i][1] == list3[j][1]:  # if the keys are same
                if list3[i][2] >= list3[j][2]:  # compare the values

                    added_key.append(str(list3[i][1]))  # add the key value to this tracker list
                    # add the value and index to the respective high dictionaries after comparing
                    if list3[i][2] > high_values[list3[i][1]]:
                        high_indexes[list3[i][1]] = list3[i][0]
                        high_values[list3[i][1]] = list3[i][2]


                else:

                    added_key.append(str(list3[j][1]))  # add the key value to this tracker list
                    # add the value and index to the respective high dictionaries after comparing
                    if list3[j][2] > high_values[list3[j][1]]:
                        high_indexes[list3[j][1]] = list3[j][0]
                        high_values[list3[j][1]] = list3[j][2]

    for i in range(
            len(list3)):  # those keys which are only in one dict, then add them directly without modifying the key
        if list3[i][1] not in added_key:
            dict4[list3[i][1]] = list3[i][2]

    for keys, values in high_indexes.items():  # add those keys which are present more than once
        dict4[keys + '_' + str(values)] = high_values[keys]

    return dict4  # print the output dict

num_dicts = random.randint(2,8) #random number for number of dictionaries
num_ele = random.randint(1,8) #random number for no_of_elements in a dict
list1 = []
list1 = create_dict(num_dicts,num_ele,list1)
print(list1)

list3 = list_of_index_key_value(list1)
print(list3)

final_dict = create_final_dict(list3)

print(final_dict)






