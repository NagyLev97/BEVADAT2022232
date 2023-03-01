
#Create a function that decides if a list contains any odd numbers.
#return type: bool
#function name must be: contains_odd
#input parameters: input_list


def contains_odd(input_list):
    index = 0
    while  index < len(input_list) and input_list[index] % 2 == 0:
        if index == len(input_list) - 1:
            if input_list[index] % 2 == 1:
                return True
        index += 1
    return index != len(input_list)

list1 = [2, 4, 2, 6, 8]
print(contains_odd(list1))

list2 = [2, 4, 2, 6, 1]
print(contains_odd(list2))  

list3 = [2, 4, 5, 2, 6]
print(contains_odd(list3))        


#Create a function that accepts a list of integers, and returns a list of bool.
#The return list should be a "mask" and indicate whether the list element is odd or not.
#(return should look like this: [True,False,False,.....])
#return type: list
#function name must be: is_odd
#input parameters: input_list


def is_odd(input_list):
    bool_list = []
    for item in input_list:
        if item % 2 == 0:
            bool_list.append(False)
        else:
            bool_list.append(True)
    return bool_list

list = [1, 3, 2, 4, 5, 8]
print(is_odd(list))



#Create a function that accpects 2 lists of integers and returns their element wise sum. <br>
#(return should be a list)
#return type: list
#function name must be: element_wise_sum
#input parameters: input_list_1, input_list_2


def element_wise_sum(input_list_1, input_list_2):
    if len(input_list_1) >= len(input_list_2):
        length = len(input_list_1)

        if len(input_list_1) > len(input_list_2):
            for i in range(0, len(input_list_1) - len(input_list_2)):
                input_list_2.append(0)
    else:
        length = len(input_list_2)

        for i in range(0, len(input_list_2) - len(input_list_1)):
                input_list_1.append(0)

   
    wise_sum_list = []
    for i in range(0, length):
        wise_sum_list.append(input_list_1[i] + input_list_2[i])
    
    return wise_sum_list

list1 = [1, 2, 3, 4]
list2 = [2, 4, 6, 5, 9]
print(element_wise_sum(list1, list2))




#Create a function that accepts a dictionary and returns its items as a list of tuples
#(return should look like this: [(key,value),(key,value),....])
#return type: list
#function name must be: dict_to_list
#input parameters: input_dict


def dict_to_list(input_dict):
    result_list = []
    for key in input_dict:
        new_tuple = (key, input_dict[key])
        result_list.append(new_tuple)
    return result_list

dict = {'alpha' : 1, 'beta' : 2, 'gamma' : 3}
print(dict_to_list(dict))



#If all the functions are created convert this notebook into a .py file and push to your repo


