import numpy as np
#FONTOS!!!

# CSAK OTT LEHET HASZNÁLNI FOR LOOP-OT AHOL A FELADAT KÜLÖN KÉRI!
# [1,2,3,4] --> ezek az értékek np.array-ek. Ahol listát kérek paraméterként ott külön ki fogom emelni!
# Ha végeztél a feladatokkal, akkor notebook-ot alakítsd át .py.
# A FÁJLBAN CSAK A FÜGGVÉNYEK LEGYENEK! (KOMMENTEK MARADHATNAK)

# Írj egy olyan fügvényt, ami megfordítja egy 2d array oszlopait. Bemenetként egy array-t vár.
# Be: [[1,2],[3,4]]
# Ki: [[2,1],[4,3]]
# column_swap()

def column_swap(input_array: np.array) -> np.array:
    input_array[:, [1, 0]]  = input_array[:, [0, 1]]
    return input_array
    
#print(column_swap(np.array([[1,2],[3,4]])))

# Készíts egy olyan függvényt ami összehasonlít két array-t és adjon vissza egy array-ben, hogy hol egyenlőek 
# Pl Be: [7,8,9], [9,8,7] 
# Ki: [1]
# compare_two_array()
# egyenlő elemszámúakra kell csak hogy működjön

def compare_two_array(input_array1: np.array, input_array2: np.array) -> np.array:
    return np.where(input_array1 == input_array2)[0]

#print(compare_two_array(np.array([7,8,9]), np.array([9,8,7])))

#Készíts egy olyan függvényt, ami vissza adja a megadott array dimenzióit:
# Be: [[1,2,3], [4,5,6]]
# Ki: "sor: 2, oszlop: 3, melyseg: 1"
# get_array_shape()
# 3D-vel még műküdnie kell!

def get_array_shape(input_array: np.array) -> str:
    dim = input_array.shape
    row = dim[0]
    column = dim[1] if len(dim) > 1 else 1
    deep = dim[2] if len(dim) > 2 else 1
    return 'sor: {}, oszlop: {}, melyseg: {}'.format(row, column, deep)

#print(get_array_shape(np.array([[1,2,3], [4,5,6]])))

# Készíts egy olyan függvényt, aminek segítségével elő tudod állítani egy neurális hálózat tanításához szükséges pred-et egy 
# numpy array-ből. 
# Bementként add meg az array-t, illetve hogy mennyi class-od van. Kimenetként pedig adjon vissza egy 2d array-t, ahol a 
# sorok az egyes elemek. Minden nullákkal teli legyen és csak ott álljon egyes, ahol a bementi tömb megjelöli. 
# Pl. ha 1 van a bemeneten és 4 classod van, akkor az adott sorban az array-ban a [1] helyen álljon egy 1-es, a többi helyen pedig 0.
# Be: [1, 2, 0, 3], 4
# Ki: [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# encode_Y()

def encode_Y(input_array: np.array, classNum) -> np.array:
    array_output = np.zeros((len(input_array), classNum))
    array_output[np.arange(len(input_array)), input_array] = 1
    return array_output

#print(encode_Y(np.array([1, 2, 0, 3]), 4))

# A fenti feladatnak valósítsd meg a kiértékelését. Adj meg a 2d array-t és adj vissza a decodolt változatát
# Be:  [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# Ki:  [1, 2, 0, 3]
# decode_Y()

def decode_Y(input_array: np.array) -> np.array:
    return np.argmax(input_array, axis = 1)


#print(decode_Y(np.array([[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]])))

# Készíts egy olyan függvényt, ami képes kiértékelni egy neurális háló eredményét! Bemenetként egy listát és egy array-t 
# és adja vissza azt az elemet, aminek a legnagyobb a valószínüsége(értéke) a listából.
# Be: ['alma', 'körte', 'szilva'], [0.2, 0.2, 0.6]. # Az ['alma', 'körte', 'szilva'] egy lista!
# Ki: 'szilva'
# eval_classification()

def eval_classification(input_list, input_array: np.array) -> str:
    return input_list[np.argmax(input_array)]

#print(eval_classification(['alma', 'körte', 'szilva'], [0.2, 0.2, 0.6]))

# Készíts egy olyan függvényt, ahol az 1D array-ben a páratlan számokat -1-re cseréli
# Be: [1,2,3,4,5,6]
# Ki: [-1,2,-1,4,-1,6]
# replace_odd_numbers()

def replace_odd_numbers(input_array: np.array):
    return np.where(input_array % 2 == 1, -1, input_array)
    
#print(replace_odd_numbers(np.array([1,2,3,4,5,6])))

