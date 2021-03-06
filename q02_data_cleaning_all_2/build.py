# Default Imports

import pandas as pd
import numpy as np

from greyatomlib.logistic_regression_project.q02_data_cleaning_all.build import data_cleaning
from greyatomlib.logistic_regression_project.q01_outlier_removal.build import outlier_removal

loan_data = pd.read_csv('data/loan_prediction_uncleaned.csv')
loan_data = loan_data.drop('Loan_ID', 1)
loan_data = outlier_removal(loan_data)
X, y, X_train, X_test, y_train, y_test = data_cleaning(loan_data)


# Write your solution here :
def convertDummies(X):
    df_new = pd.DataFrame()
    X = X.copy()
    df_categoric = X.select_dtypes(include=['object'])

    df_categoric = pd.get_dummies(df_categoric)

    return df_categoric

def data_cleaning_2(X_train, X_test, y_train, y_test):
    X_train = convertDummies(X_train)
    X_test = convertDummies(X_test)
    return X_train, X_test, y_train, y_test
