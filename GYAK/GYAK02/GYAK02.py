
import numpy as np


#FONTOS!!!

# CSAK OTT LEHET HASZNÁLNI FOR LOOP-OT AHOL A FELADAT KÜLÖN KÉRI!
# [1,2,3,4] --> ezek az értékek np.array-ek. Ahol listát kérek paraméterként ott külön ki fogom emelni!
# Ha végeztél a feladatokkal, akkor notebook-ot alakítsd át .py.
# A FÁJLBAN CSAK A FÜGGVÉNYEK LEGYENEK! (KOMMENTEK MARADHATNAK)


#Készíts egy függvényt ami létre hoz egy nullákkal teli numpy array-t.
#Paraméterei: mérete (tuple-ként), default mérete pedig legyen egy (2,2)
#Be: (2,2)
#Ki: [[0,0],[0,0]]
#create_array()

def create_array(input_tuple=(2,2)) -> np.array:
    return np.zeros(input_tuple)


# arr = create_array()
# print(arr)


#Készíts egy függvényt ami a paraméterként kapott array-t főátlóját feltölti egyesekkel
#Be: [[1,2],[3,4]]
#Ki: [[1,2],[3,1]]
#set_one()

def set_one(array: np.array) -> np.array:
    np.fill_diagonal(array, 1)
    return array

# arr = [[1,2],[3,4]]
# alma = set_one(np.array(arr))
# print(alma)

# Készíts egy függvényt ami transzponálja a paraméterül kapott mártix-ot:
# Be: [[1, 2], [3, 4]]
# Ki: [[1, 2], [3, 4]]
# do_transpose()

def do_transpose(array: np.array) -> np.array:
   return np.transpose(array)
    

# arr = [[1, 2], [3, 4]]
# alma = do_transpose(np.array(arr))
# print(alma)


# Készíts egy olyan függvényt ami az array-ben lévő értékeket N tizenedjegyik kerekíti, ha nincs megadva ez a paraméter, akkor legyen az alapértelmezett a kettő 
# Be: [0.1223, 0.1675], 2
# Ki: [0.12, 0.17]
# round_array()

def round_array(array: np.array, roundNumber = 2) -> np.array:
    return np.round(array, roundNumber)

# array = round_array([0.1223, 0.1675], 2)
# print(array)

# Készíts egy olyan függvényt, ami a bementként kapott 0 és 1 ből álló tömben a 0 - False-ra, az 1 True-ra cserélni
# Be: [[1, 0, 0], [1, 1, 1],[0, 0, 0]]
# Ki: [[ True False False], [ True  True  True], [False False False]]
# bool_array()

def bool_array(array: np.array) -> np.array:
    return array.astype(bool)
    

# array = bool_array(np.array([[1, 0, 0], [1, 1, 1],[0, 0, 0]]))
# print(array)

# Készíts egy olyan függvényt, ami a bementként kapott 0 és 1 ből álló tömben a 1 - False-ra az 0 True-ra cserélni
# Be: [[1, 0, 0], [1, 1, 1],[0, 0, 0]]
# Ki: [[ True False False], [ True  True  True], [False False False]]
# invert_bool_array()

def invert_bool_array(array: np.array) -> np.array:
    return np.invert(array.astype(bool))

# print(invert_bool_array(np.array([[1, 0, 0], [1, 1, 1],[0, 0, 0]])))

# Készíts egy olyan függvényt ami a paraméterként kapott array-t kilapítja
# Be: [[1,2], [3,4]]
# Ki: [1,2,3,4]
# flatten()

def flatten(array: np.array) -> np.array:
    return array.flatten()

# print(flatten(np.array([[1,2], [3,4]])))