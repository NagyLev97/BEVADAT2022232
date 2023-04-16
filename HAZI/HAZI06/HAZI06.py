"""
1.  Értelmezd az adatokat!!!
    A feladat megoldásához használd a NJ transit + Amtrack csv-t a moodle-ból.
    A NJ-60k az a megoldott. Azt fogom használni a modellek teszteléséhez, illetve össze tudod hasonlítani az eredményedet.    

2. Írj egy osztályt a következő feladatokra:  
     2.1 Neve legyen NJCleaner és mentsd el a NJCleaner.py-ba. Ebben a fájlban csak ez az osztály legyen.
     2.2 Konsturktorban kapja meg a csv elérési útvonalát és olvassa be pandas segítségével és mentsük el a data (self.data) osztályszintű változóba 
     2.3 Írj egy függvényt ami sorbarendezi a dataframe-et 'scheduled_time' szerint növekvőbe és visszatér a sorbarendezett df-el, a függvény neve legyen 'order_by_scheduled_time' és térjen vissza a df-el  
     2.4 Dobjuk el a from és a to oszlopokat, illetve azokat a sorokat ahol van nan és adjuk vissza a df-et. A függvény neve legyen 'drop_columns_and_nan' és térjen vissza a df-el  
     2.5 A date-et alakítsd át napokra, pl.: 2018-03-01 --> Thursday, ennek az oszlopnak legyen neve a 'day'. Ezután dobd el a 'date' oszlopot és térjen vissza a df-el. A függvény neve legyen 'convert_date_to_day' és térjen vissza a df-el   
     2.6 Hozz létre egy új oszlopot 'part_of_the_day' névvel. A 'scheduled_time' oszlopból számítsd ki az alábbi értékeit. A 'scheduled_time'-ot dobd el. A függvény neve legyen 'convert_scheduled_time_to_part_of_the_day' és térjen vissza a df-el  
         4:00-7:59 -- early_morning  
         8:00-11:59 -- morning  
         12:00-15:59 -- afternoon  
         16:00-19:59 -- evening  
         20:00-23:59 -- night  
         0:00-3:59 -- late_night  
    2.7 A késéseket jelöld az alábbiak szerint. Az új osztlop neve legyen 'delay'. A függvény neve legyen pedig 'convert_delay' és térjen vissza a df-el
         0min <= x < 5min   --> 0  
         5min <= x          --> 1  
    2.8 Dobd el a felesleges oszlopokat 'train_id' 'actual_time' 'delay_minutes'. A függvény neve legyen 'drop_unnecessary_columns' és térjen vissza a df-el
    2.9 Írj egy olyan metódust, ami elmenti a dataframe első 60 000 sorát. A függvénynek egy string paramétere legyen, az pedig az, hogy hova mentse el a csv-t (pl.: 'data/NJ.csv'). A függvény neve legyen 'save_first_60k'. 
    2.10 Írj egy függvényt ami a fenti függvényeket összefogja és megvalósítja (sorbarendezés --> drop_columns_and_nan --> ... --> save_first_60k), a függvény neve legyen 'prep_df'. Egy paramnétert várjon, az pedig a csv-nek a mentési útvonala legyen. Ha default value-ja legyen 'data/NJ.csv'

3.  A feladatot a HAZI06.py-ban old meg.
    Az órán megírt DecisionTreeClassifier-t fit-eld fel az első feladatban lementett csv-re. 
    A feladat célja az, hogy határozzuk meg azt, hogy a vonatok késnek-e vagy sem. 0p <= x < 5p --> nem késik (0), ha 5p <= x --> késik (1).
    Az adatoknak a 20% legyen test és a splitelés random_state-je pedig 41 (mint órán)
    A testset-en 80% kell elérni. Ha megvan a minimum százalék, akkor azzal paraméterezd fel a decisiontree-t és azt kell leadni.

    A leadásnál csak egy fit kell, ezt azzal a paraméterre paraméterezd fel, amivel a legjobb accuracy-t elérted.

    A helyes paraméter megtalálásához használhatsz grid_search-öt.
    https://www.w3schools.com/python/python_ml_grid_search.asp 

4.  A tanításodat foglald össze 4-5 mondatban a HAZI06.py-ban a fájl legalján kommentben. Írd le a nehézségeket, mivel próbálkoztál, mi vált be és mi nem. Ezen kívül írd le 10 fitelésed eredményét is, hogy milyen paraméterekkel probáltad és milyen accuracy-t értél el. 
Ha ezt feladatot hiányzik, akkor nem fogadjuk el a házit!

HAZI-
    HAZI06-
        -NJCleaner.py
        -HAZI06.py

##################################################################
##                                                              ##
## A feladatok közül csak a NJCleaner javítom unit test-el      ##
## A decision tree-t majd manuálisan fogom lefuttatni           ##
## NJCleaner - 10p, Tanítás - acc-nál 10%-ként egy pont         ##
## Ha a 4. feladat hiányzik, akkor nem tudjuk elfogadni a házit ##
##                                                              ##
##################################################################
"""

import pandas as pd

from src.DecisionTreeClassifier import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

col_name = ['stop_sequence', 'from_id', 'to_id', 'status', 'line','type','day','part_of_the_day', 'delay']
data = pd.read_csv('HAZI\\HAZI06\\data\\NJ.csv', skiprows=1, header=None, names=col_name)

X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values.reshape(-1,1)

X_train, X_test, Y_train, Y_test  = train_test_split(X, Y, test_size=.2, random_state=41)

classifier = DecisionTreeClassifier(min_samples_split=100, max_depth=11)
classifier.fit(X_train, Y_train)

Y_pred = classifier.predict(X_test)
print(accuracy_score(Y_test, Y_pred))

# S = [5, 10, 50, 100, 150]
# D = [8, 9, 10, 11, 12]

# S = [2, 8, 15, 30, 45, 60, 100]
# D = [3, 8, 10, 12, 15, 20, 30]

# results = []
# i = 0
# for choice in D:
#     j = 0
#     for choise_two in S:
#         try:
#             classifier = DecisionTreeClassifier(min_samples_split=S[j], max_depth=D[i])
#             classifier.fit(X_train, Y_train)
#             Y_pred = classifier.predict(X_test)
#             accuracy = accuracy_score(Y_test, Y_pred)
#             results.append(accuracy)
#             print(f'Min split: {S[j]}, Max depth: {D[i]}. The accuracy: {accuracy}')
#             j=j+1
#         except Exception:
#             print(f'ERROR: Min split: {S[j]}, Max depth: {D[i]}.')
#             j=j+1
#     i=i+1
    
# A min_samples_split paraméter befolyásolja a fa modell komplexitását, illetve overfitting is jelentkezhet, ha például 
# túl alacsony az érték, hiszen ekkor a fa sok ágat hoz létre, mellyel túl specifikus lesz a modell. 
# Ugyanez vonatkozik a max_depth-re is, csak fordítva. Ha túl magas az érték, akkor juthatunk el gyorsan az overfittingig.
# Ha viszont túl alacsony, akkor underfitting jelentkezhet. 
# Ezekből kiindulva olyan stratégiát követtem az optimális fitting megválasztásához, hogy a min_split értékeket
# nagyobb lépésközökkel, míg a max_depth-et kisebb lépésközökkel futtattam grid search segítségével. Ha a max_depth értéke 
# kicsi (2,3,4), akkor a teszteseteken keresztül is látszik, hogy az accuracy ugyanakkora. Vagyis a jó stratégia, ha a 
# max_depth értékét növelem. 
# Ilyen módon jutottam el a 80,36%-os accuracy-ig, amit 100-as min_split-tel és 11-es max_depth-tel értem el.
# Kíváncsi voltam arra is, hogy kisebb min_splittel is el lehet-e jutni hasonlóan jó eredményhez. 80,15% accuracy-t
# lehetett elérni 15 min_split és 20 max_depth megválasztásával. 
# A tesztesetek futtatásánál kiderült, hogy több esetben hibára fut az algoritmus, ezért egy try-catch blokkot tettem
# a kódba. 

# ------------------------------------------------------------------

#Tesztesetek:

# Min split: 5, Max depth: 2. The accuracy: 0.7823333333333333
# Min split: 10, Max depth: 2. The accuracy: 0.7823333333333333
# Min split: 50, Max depth: 2. The accuracy: 0.7823333333333333
# Min split: 100, Max depth: 2. The accuracy: 0.7823333333333333
# Min split: 150, Max depth: 2. The accuracy: 0.7823333333333333

# Min split: 5, Max depth: 3. The accuracy: 0.7839166666666667
# Min split: 10, Max depth: 3. The accuracy: 0.7839166666666667
# Min split: 50, Max depth: 3. The accuracy: 0.7839166666666667
# Min split: 100, Max depth: 3. The accuracy: 0.7839166666666667
# Min split: 150, Max depth: 3. The accuracy: 0.7839166666666667

# Min split: 5, Max depth: 4. The accuracy: 0.7849166666666667
# Min split: 10, Max depth: 4. The accuracy: 0.7849166666666667
# Min split: 50, Max depth: 4. The accuracy: 0.7849166666666667
# Min split: 100, Max depth: 4. The accuracy: 0.7849166666666667
# Min split: 150, Max depth: 4. The accuracy: 0.7846666666666666

# Min split: 5, Max depth: 5. The accuracy: 0.7885833333333333
# Min split: 10, Max depth: 5. The accuracy: 0.7885833333333333
# Min split: 50, Max depth: 5. The accuracy: 0.7885833333333333
# Min split: 100, Max depth: 5. The accuracy: 0.7885833333333333
# Min split: 150, Max depth: 5. The accuracy: 0.78825

# Min split: 5, Max depth: 6. The accuracy: 0.7885
# Min split: 10, Max depth: 6. The accuracy: 0.7885
# Min split: 50, Max depth: 6. The accuracy: 0.7885
# Min split: 100, Max depth: 6. The accuracy: 0.7888333333333334
# Min split: 150, Max depth: 6. The accuracy: 0.7884166666666667

# Min split: 5, Max depth: 7. The accuracy: 0.7934166666666667
# Min split: 10, Max depth: 7. The accuracy: 0.7935
# Min split: 50, Max depth: 7. The accuracy: 0.7935833333333333
# Min split: 100, Max depth: 7. The accuracy: 0.7940833333333334
# Min split: 150, Max depth: 7. The accuracy: 0.793

# ERROR: Min split: 5, Max depth: 8.
# Min split: 10, Max depth: 8. The accuracy: 0.7955833333333333
# Min split: 50, Max depth: 8. The accuracy: 0.7954166666666667
# Min split: 100, Max depth: 8. The accuracy: 0.7969166666666667
# Min split: 150, Max depth: 8. The accuracy: 0.7955833333333333

# ERROR: Min split: 5, Max depth: 9.
# ERROR: Min split: 10, Max depth: 9.
# Min split: 50, Max depth: 9. The accuracy: 0.7981666666666667
# Min split: 100, Max depth: 9. The accuracy: 0.7986666666666666
# Min split: 150, Max depth: 9. The accuracy: 0.7973333333333333

# ERROR: Min split: 5, Max depth: 10.
# ERROR: Min split: 10, Max depth: 10.
# Min split: 50, Max depth: 10. The accuracy: 0.8010833333333334
# Min split: 100, Max depth: 10. The accuracy: 0.80225
# Min split: 150, Max depth: 10. The accuracy: 0.7991666666666667

# ERROR: Min split: 5, Max depth: 11.
# ERROR: Min split: 10, Max depth: 11.
# Min split: 50, Max depth: 11. The accuracy: 0.8026666666666666
# Min split: 100, Max depth: 11. The accuracy: 0.8035833333333333 <--
# Min split: 150, Max depth: 11. The accuracy: 0.80075

# ERROR: Min split: 5, Max depth: 12.
# ERROR: Min split: 10, Max depth: 12.
# Min split: 50, Max depth: 12. The accuracy: 0.8
# Min split: 100, Max depth: 12. The accuracy: 0.8025
# Min split: 150, Max depth: 12. The accuracy: 0.80025

# ------------------------------------------------------------------

# ERROR: Min split: 8, Max depth: 3.
# ERROR: Min split: 15, Max depth: 3.
# ERROR: Min split: 30, Max depth: 3.
# ERROR: Min split: 45, Max depth: 3.
# ERROR: Min split: 60, Max depth: 3.
# ERROR: Min split: 100, Max depth: 3.

# Min split: 2, Max depth: 8. The accuracy: 0.7839166666666667
# Min split: 8, Max depth: 8. The accuracy: 0.7955
# ERROR: Min split: 15, Max depth: 8.
# ERROR: Min split: 30, Max depth: 8.
# ERROR: Min split: 45, Max depth: 8.
# ERROR: Min split: 60, Max depth: 8.
# ERROR: Min split: 100, Max depth: 8.

# Min split: 2, Max depth: 10. The accuracy: 0.7839166666666667
# Min split: 8, Max depth: 10. The accuracy: 0.7956666666666666
# ERROR: Min split: 15, Max depth: 10.
# ERROR: Min split: 30, Max depth: 10.
# ERROR: Min split: 45, Max depth: 10.
# ERROR: Min split: 60, Max depth: 10.
# ERROR: Min split: 100, Max depth: 10.

# Min split: 2, Max depth: 12. The accuracy: 0.7839166666666667
# Min split: 8, Max depth: 12. The accuracy: 0.7955
# Min split: 15, Max depth: 12. The accuracy: 0.80075
# Min split: 30, Max depth: 12. The accuracy: 0.7995
# Min split: 45, Max depth: 12. The accuracy: 0.7929166666666667
# Min split: 60, Max depth: 12. The accuracy: 0.78425
# Min split: 100, Max depth: 12. The accuracy: 0.7818333333333334

# Min split: 2, Max depth: 15. The accuracy: 0.7839166666666667
# Min split: 8, Max depth: 15. The accuracy: 0.7953333333333333
# Min split: 15, Max depth: 15. The accuracy: 0.8015
# Min split: 30, Max depth: 15. The accuracy: 0.79975
# Min split: 45, Max depth: 15. The accuracy: 0.7931666666666667
# Min split: 60, Max depth: 15. The accuracy: 0.7865833333333333
# Min split: 100, Max depth: 15. The accuracy: 0.7843333333333333

# Min split: 2, Max depth: 20. The accuracy: 0.7839166666666667
# Min split: 8, Max depth: 20. The accuracy: 0.7955
# Min split: 15, Max depth: 20. The accuracy: 0.8015                <--
# Min split: 30, Max depth: 20. The accuracy: 0.8016666666666666
# Min split: 45, Max depth: 20. The accuracy: 0.7949166666666667
# Min split: 60, Max depth: 20. The accuracy: 0.7896666666666666
# Min split: 100, Max depth: 20. The accuracy: 0.7880833333333334

# Min split: 2, Max depth: 30. The accuracy: 0.7839166666666667
# Min split: 8, Max depth: 30. The accuracy: 0.7969166666666667
# Min split: 15, Max depth: 30. The accuracy: 0.80225
# Min split: 30, Max depth: 30. The accuracy: 0.8025
# Min split: 45, Max depth: 30. The accuracy: 0.7985
# Min split: 60, Max depth: 30. The accuracy: 0.7974166666666667
# Min split: 100, Max depth: 30. The accuracy: 0.7973333333333333
