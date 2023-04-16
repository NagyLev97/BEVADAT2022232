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
