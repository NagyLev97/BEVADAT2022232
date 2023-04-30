import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from scipy.stats import mode
from sklearn.metrics import confusion_matrix
from sklearn import datasets

class KMeansOnDigit():
    

    def __init__(self, n_clusters, random_state):
        self.n_clusters = n_clusters
        self.random_state = random_state

    def load_dataset(self):
        self.digits = datasets.load_digits()

    def predict(self):
        self.model = KMeans(self.n_clusters, self.random_state)
        self.clusters = self.model.fit_predict(self.digits.data)
    
    def get_labels(self):
        result_array = np.zeros_like(self.n_clusters)
        for cluster in range(10):
            mask = self.n_clusters == cluster
            target = self.digits.target[mask]
            mode_value = mode(target)
            result_array[mask] = mode_value.mode[0]
        return result_array
    
    def calc_accuracy(self):
        accuracy = accuracy_score(self.digits.targer, self.labels)
        return round(accuracy, 2)
    
    def confusion_matrix(self):
        self.mat = confusion_matrix(self.digits.target, self.labels)

