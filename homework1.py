import random
#random module is imported

num_list = [] #create an empty list to hold the values

#for loop to generate 100 random integers
for i in range(100):
    num = random.randint(0,1000)
    num_list.append(num)

print("The generated list is", num_list)

#sort the list using bubble sort
for i in range(0,len(num_list)): #take one element of the list from the start index
    for j in range(i+1,len(num_list)):
        if num_list[i] > num_list[j]: #comapre that element with elements starting from next index to the end index
            temp = num_list[i]  #swap the elements element is bigger
            num_list[i] = num_list[j]
            num_list[j] = temp


print("Sorted list is:", num_list) #print the sorted list

#initialize variables
even_sum = 0
even_count = 0
odd_sum = 0
odd_count = 0

#calculate even and odd sums,counts and average
for num in num_list:
    if num % 2 == 0:
        even_sum += num
        even_count += 1
    else :
        odd_count += 1
        odd_sum += num
even_avg = even_sum /even_count
odd_avg = odd_sum /odd_count

#print the odd and even averages
print("Odd average is : ", odd_avg)
print("Even average is : ", even_avg)

