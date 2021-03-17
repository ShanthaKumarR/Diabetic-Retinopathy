import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

#function load_data which randomly generates data
#from utils import load_data as pandas dataframe 

#load_data as pandas dataframe
# X is the training dataset
# y is lables

X = pd.read_csv('X_data.csv',index_col=0)
Y = pd.read_csv('y_data.csv',index_col=0)

# Using the sklearn libirary the training dataset is divided into training and testing 
X_train, X_test, train_label, test_label = train_test_split(X, Y, train_size=0.75, random_state=0)




class Data_analysis:
    def __init__(self, X, Y, X_train):
        self.X = X
        self.Y = Y
        self.X_train = X_train
    def data_explore(self):
       print(self.X.head())
       print('The column attributes in the training data is ', self.X.columns) 
    def histogram_plot(self):
        for col in self.X.columns:
            self.X.loc[:, col].hist()
            plt.title(col)
            plt.show()
   
obj1 = Data_analysis(X, Y, X_train)
obj1.data_explore()
obj1.histogram_plot()

# Distribution of the training dataset 

