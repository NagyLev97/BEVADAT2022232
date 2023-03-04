#Create a function that returns with a subsest of a list.
#The subset's starting and ending indexes should be set as input parameters (the list aswell).
#return type: list
#function name must be: subset
#input parameters: input_list,start_index,end_index


def subset(input_list, start_index, end_index):
    return input_list[start_index:(end_index)]
list = [0,1,2,3,4,5,6,7,8,9]

print(subset(list, 0, 4))
print(subset(list, 4, 8))


#Create a function that returns every nth element of a list.
#return type: list
#function name must be: every_nth
#input parameters: input_list,step_size


def every_nth(input_list, step_size):
    return input_list[::step_size]

list = [0,1,2,3,4,5,6,7,8,9]

print(every_nth(list, 2))
print(every_nth(list, 1))

#Create a function that can decide whether a list contains unique values or not
#return type: bool
#function name must be: unique
#input parameters: input_list


def unique(input_list):
    index = 0
    inindex = 0
    result = True
    while index < len(input_list):
        while inindex < len(input_list):
            if index == inindex:
                inindex += 1
                if inindex == len(input_list):
                    break
            if list[index] == list[inindex]:
                result = False
                return result
            inindex += 1
        inindex = 0
        index += 1
    return result

list = [0,1,2,2]
print(unique(list))
list = [0,1,2,3]
print(unique(list))


def unique(input_list):
    set_list = set(input_list)
    if len(set_list) == len(input_list):
        return True
    else:
        return False
    
list = [0,1,2,2]
print(unique(list))
list = [0,1,2,3]
print(unique(list))


#Create a function that can flatten a nested list ([[..],[..],..])
#return type: list
#fucntion name must be: flatten
#input parameters: input_list


def flatten(input_list):
    flatten_list = []
    for item in input_list:
        for element in item:
            flatten_list.append(element)
    return flatten_list

list = [[1,2,3],[4,5],[6],[7,8,9]]
print(flatten(list))


#Create a function that concatenates n lists
#return type: list
#function name must be: merge_lists
#input parameters: *args



def merge_lists(*args):
    merge_list = [element for list in args for element in list]
    return merge_list

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
merge_list = merge_lists(list1, list2, list3)
print(merge_list)


#Create a function that can reverse a list of tuples
#example [(1,2),...] => [(2,1),...]
#return type: list
#fucntion name must be: reverse_tuples
#input parameters: input_list


def reverse_tuples(input_list):
    reversed_list = []
    for item in input_list:
        new_list = item[::-1]
        reversed_element = tuple(new_list)
        reversed_list.append(reversed_element)
    return reversed_list
    
list = [(1, 2), (3, 4), (5, 6)]
reversed_list = reverse_tuples(list)
print(reversed_list)


#Create a function that removes duplicates from a list
#return type: list
#fucntion name must be: remove_tuplicates
#input parameters: input_list


def remove_duplicates(input_list):
    return list(set(input_list))

list = [1, 4, 2, 2, 5, 1]
print(remove_duplicates(list))


#Create a function that transposes a nested list (matrix)
#return type: list
#function name must be: transpose
#input parameters: input_list


def transpose(input_list):
    return [[input_list[j][i] for j in range(len(input_list))] for i in range(len(input_list[0]))]

matrix = [[1, 2], [3, 4]]
new_matrix = transpose(matrix)
print(new_matrix)

#Create a function that can split a nested list into chunks
#chunk size is given by parameter
#return type: list
#function name must be: split_into_chunks
#input parameters: input_list,chunk_size


def split_into_chunks(input_list, chunk_size):
    flatten_list = []
    for item in input_list:
        flatten_list.append(item)

    new_list = []
    for i in range(0, len(flatten_list), chunk_size):
        t = i
        new_list.append(flatten_list[t:t+chunk_size])
    return new_list

nested_list = [[1, 2, 3], [4, 5], [6, 7], [8, 9, 10, 11]]
splitted_list = split_into_chunks(nested_list, 2)
print(splitted_list)



#Create a function that can merge n dictionaries
#return type: dictionary
#function name must be: merge_dicts
#input parameters: *dict


def merge_dicts(*dict):
    merged_dict = {}
    for d in dict:
        merged_dict.update(d)

    return merged_dict

dict1 = {'one': 1, 'two' : 2}
dict2 = {'three': 3, 'four' : 4, 'six' : 6}
dict3 = {'five': 5, 'eight' : 8}
dict4 = {'nine': 9, 'eleven' : 11, 'ten' : 10}
merged_dict = merge_dicts(dict1, dict2, dict3, dict4)
print(merged_dict)


#Create a function that receives a list of integers and sort them by parity
#and returns with a dictionary like this: {"even":[...],"odd":[...]}
#return type: dict
#function name must be: by_parity
#input parameters: input_list


def by_parity(input_list):
    even_list = []
    odd_list = []
    for element in input_list:
        if element % 2 == 0:
            even_list.append(element)
        else:
            odd_list.append(element)
    new_dict = {'even' : even_list, 'odd' : odd_list}
    return new_dict

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parity_dict = by_parity(list)
print(parity_dict)


#Create a function that receives a dictionary like this: {"some_key":[1,2,3,4],"another_key":[1,2,3,4],....}
#and return a dictionary like this : {"some_key":mean_of_values,"another_key":mean_of_values,....}
#in short calculates the mean of the values key wise
#return type: dict
#function name must be: mean_key_value
#input parameters: input_dict

def mean_key_value(input_dict):
    mean_dict = {}
    for key, value in input_dict.items():
        mean_value = sum(value) / len(value)
        mean_dict[key] = mean_value
    return mean_dict

dict = {'first_key' : [1,2,3], 'second_key' : [5], 'third_key' : [2, 4, 6]}
mean_dict = mean_key_value(dict)
print(mean_dict)


#If all the functions are created convert this notebook into a .py file and push to your repo


