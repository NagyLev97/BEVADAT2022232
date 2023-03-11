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

def replace_odd_numbers(input_array: np.array) -> np.array:
    return np.where(input_array % 2 == 1, -1, input_array)
    
#print(replace_odd_numbers(np.array([1,2,3,4,5,6])))

# Készíts egy olyan függvényt, ami egy array értékeit -1 és 1-re változtatja, attól függően, hogy az adott elem nagyobb vagy
# kisebb a paraméterként megadott számnál.
# Ha a szám kisebb mint a megadott érték, akkor -1, ha nagyobb vagy egyenlő, akkor pedig 1.
# Be: [1, 2, 5, 0], 2
# Ki: [-1, 1, 1, -1]
# replace_by_value()

def replace_by_value(input_array: np.array, num) -> np.array:
    return np.where(input_array < num, -1, 1)

#print(replace_by_value(np.array([1, 2, 5, 0]), 2))

# Készíts egy olyan függvényt, ami egy array értékeit összeszorozza és az eredményt visszaadja
# Be: [1,2,3,4]
# Ki: 24
# array_multi()
# Ha több dimenziós a tömb, akkor az egész tömb elemeinek szorzatával térjen vissza

def array_multi(input_array: np.array) -> int:
    return np.prod(input_array)

#print(array_multi(np.array([1,2,3,4])))

# Készíts egy olyan függvényt, ami egy 2D array értékeit összeszorozza és egy olyan array-el tér vissza, aminek az elemei a soroknak a szorzata
# Be: [[1, 2], [3, 4]]
# Ki: [2, 12]
# array_multi_2d()

def array_multi_2d(input_array: np.array) -> np.array:
    return np.prod(input_array, axis=1)

#print(array_multi_2d(np.array([[1, 2], [3, 4]])))

# Készíts egy olyan függvényt, amit egy meglévő numpy array-hez készít egy bordert nullásokkal. 
# Bementként egy array-t várjon és kimenetként egy array jelenjen meg aminek van border-je
# Be: [[1,2],[3,4]]
# Ki: [[0,0,0,0],[0,1,2,0],[0,3,4,0],[0,0,0,0]]
# add_border()

def add_border(input_array: np.array) -> np.array:
    shape = np.array(input_array.shape) + 2
    output_array = np.zeros(shape)
    output_array[1:-1, 1:-1] = input_array
    return output_array

#print(add_border(np.array([[1,2],[3,4]])))

# Készíts egy olyan függvényt ami két dátum között felsorolja az összes napot és ezt adja vissza egy numpy array-ben. 
# A fgv ként str vár paraméterként 'YYYY-MM' formában.
# Be: '2023-03', '2023-04'  # mind a kettő paraméter str.
# Ki: ['2023-03-01', '2023-03-02', .. , '2023-03-31',]
# list_days()

def list_days(start, end) -> np.array:
    return np.arange(start, end, dtype='datetime64[D]')

#print(list_days('2023-03', '2023-04'))

# Írj egy fügvényt ami vissza adja az aktuális dátumot az alábbi formában: YYYY-MM-DD. Térjen vissza egy 'numpy.datetime64' típussal.
# Be:
# Ki: 2017-03-24
# get_act_date()

def get_act_date() -> str:
    return np.datetime64('today', 'D')

print(get_act_date())

# Írj egy olyan függvényt ami visszadja, hogy mennyi másodperc telt el 1970 január 01. 00:02:00 óta. Int-el térjen vissza
# Be: 
# Ki: másodpercben az idó, int-é kasztolva
# sec_from_1970()

def sec_from_1970() -> int:
    now = np.datetime64('today', 'D')
    past = np.datetime64('1970-01-01')
    return int((now - past) / np.timedelta64(1, 's'))


#print(sec_from_1970())
