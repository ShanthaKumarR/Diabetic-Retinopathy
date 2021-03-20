import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

#function load_data which randomly generates data
#from utils import load_data as pandas dataframe 

#load_data as pandas dataframe
# X is the training dataset
# y is lables

X = pd.read_csv('X_data.csv',index_col=0)
Y = pd.read_csv('y_data.csv',index_col=0)

# Using the sklearn libirary the training dataset is divided into training and testing 
train_data, test_data, train_label, test_label = train_test_split(X, Y, train_size=0.75, random_state=0)

class Data_analysis:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
    def data_explore(self):
       print(self.X.head())
       print('The column attributes in the training data is ', self.X.columns) 
    def histogram_plot(self):
        for col in self.X.columns:
            self.X.loc[:, col].hist()
            plt.title(col)
            plt.show()
    def skewness_reomved_plot(self):
        for col in self.X.columns:
            np.log(self.X.loc[:, col]).hist()
            plt.title('Skewness removed'+ ' ' + col)
            plt.show()
    def standardizes_distrubution(self):
        unskewed_data = np.log(self.X)
        mean = unskewed_data.mean(axis = 0)
        stdev = unskewed_data.std(axis = 0)
        print(mean)
        standarized_data = (unskewed_data - mean) / stdev
        return standarized_data
    def model_fit(self):
        model = LogisticRegression()
        return model.fit(self.X, self.Y.values.ravel())  
    def save_model(self, model,  path):
        joblib.dump(model, path) 

train = Data_analysis(train_data, train_label)
test = Data_analysis(test_data, test_label)
train.data_explore()


# Distribution of the training dataset 
# train.histogram_plot()
# train.skewness_removed_plot()
standarized_train_data = train.standardizes_distrubution()
standarized_test_data = test.standardizes_distrubution()
model = train.model_fit()
train.save_model(model, './flask_app/lr_model.sav')

loaded_model = joblib.load('lr_model.sav')

print(loaded_model.predict(test_data))



