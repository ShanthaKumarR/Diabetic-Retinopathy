import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

#function load_data which randomly generates data
#from utils import load_data as pandas dataframe 

#load_data as pandas dataframe
# X is the training dataset
# y is lables





#To see the first 10 records in the training dataset pass 10 as the argument to the head()

#print(y.head(10))



class Data_analysis:
    def __init__(self, dataset, label, index_col = 0):
        self.dataset = dataset
        self.label = label
        self.index_col = index_col
    def data(self):
        X = pd.read_csv(self.dataset, self.index_col)
        Y = pd.read_csv(self.label,self.index_col)
        print(x.head())
        return X

obj1 = Data_analysis('X_data.csv', 'y_data.csv', 0)
X = obj1.data()
#print(X)




# Distribution of the training dataset 

# Using the sklearn libirary the training dataset is divided into training and testing 

#X_train_raw, X_test_raw, y_train, y_test = train_test_split(X, y, train_size=0.75, random_state=0)
