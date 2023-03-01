def subset(input_list, start_index, end_index):
    return input_list[start_index:(end_index+1)]
list = [0,1,2,3,4,5,6,7,8,9]

print(subset(list, 0, 4))
print(subset(list, 4, 8))