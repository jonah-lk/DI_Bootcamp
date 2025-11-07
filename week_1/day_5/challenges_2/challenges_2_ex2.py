# Exercise 2
# Analyse this code before executing it. Write some commnts next to each line. Write the value of each variable and their changes, and add the final output. Try to understand the purpose of this program.
my_list = [2, 24, 12, 354, 233] # my_list = [2, 24, 12, 354, 233]
for i in range(len(my_list) - 1): # i from 0 to length of my_list - 1, the index of the second to last item in the list. Here i is these values: [0, 1, 2, 3]
    minimum = i # minimum is 0, then 1, 2, 3 for the other iterations
    for j in range( i + 1, len(my_list)): # j from 1 (first index i + 1) and through the rest indeces, all of them in this case. We iterate here len(list) times before we go back to the outer loop's next iteration
        if(my_list[j] < my_list[minimum]): # we check if the value starting form i + 1 to the end is less than the value of the index of the outer loop
            minimum = j # the value is indeed less so we set the min index as the inner loop index
            if(minimum != i): # if the min index has changed we do the following
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i] # we swape the new min to index i
    
print(my_list) # we sort the list