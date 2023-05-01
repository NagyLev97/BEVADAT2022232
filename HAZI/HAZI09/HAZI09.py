import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from scipy.stats import mode
from sklearn.metrics import confusion_matrix
from sklearn import datasets

class KMeansOnDigits():
    

    def __init__(self, n_clusters, random_state):
        self.n_clusters = n_clusters
        self.random_state = random_state

    def load_dataset(self):
        self.digits = datasets.load_digits()

    def predict(self):
        self.model = KMeans(n_clusters=self.n_clusters, random_state=self.random_state)
        self.clusters = self.model.fit_predict(self.digits.data)
    
    def get_labels(self):
        result_array = np.zeros_like(self.clusters)
        for cluster in range(self.n_clusters):
            mask = (self.n_clusters == cluster)
            target = self.digits.target[mask]
            mode_value = mode(target)
            result_array[mask] = mode_value.mode[0]
        self.labels = result_array
    
    def calc_accuracy(self):
        accuracy = accuracy_score(self.digits.target, self.labels)
        return round(accuracy, 2)
    
    def confusion_matrix(self):
        self.mat = confusion_matrix(self.digits.target, self.labels)

