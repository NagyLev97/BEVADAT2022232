import pandas as pd

from src.DecisionTreeClassifier import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

col_name = ['stop_sequence', 'from_id', 'to_id', 'status', 'line','type','day','part_of_the_day', 'delay']
data = pd.read_csv('BEVADAT2022232\\HAZI\\HAZI06\\data\\NJ.csv', skiprows=1, header=None, names=col_name)

X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values.reshape(-1,1)

X_train, X_test, Y_train, Y_test  = train_test_split(X, Y, test_size=.2, random_state=41)

classifier = DecisionTreeClassifier(min_samples_split=3, max_depth=3)
classifier.fit(X_train, Y_train)

Y_pred = classifier.predict(X_test)
print(accuracy_score(Y_test, Y_pred))