# Imports

import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk
from scipy import stats
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from wrangle import new_data, clean_data, missing_zero_values_table, train_validate_test_split


# Model for Individual Project 

def run_model():
   
    df = new_data()
    
    #clean the data
    
    df = clean_data(df)

    # train, validate, split the data
    
    train, validate, test = train_validate_test_split(df, seed=123)
          
# Select features to be used in the model
    
    cols = ['annual_salary_2020','base_pay_2020', 'leave_payout_2020', 'other_2020', 'arbitration_and_settlements', 'overtime_2020', 'additional_compensation', 'total_compensation',
           'years_employed', 'ethnicity_ASIAN', 'ethnicity_BLACK', 'ethnicity_HISPANIC', 'ethnicity_NATIVE AMERICAN', 'ethnicity_NATIVE HAWAIIAN',
           'ethnicity_OTHER', 'ethnicity_WHITE']

    X = test[cols]
    y = test.gender
    
# Create and fit the model
    
    forest = RandomForestClassifier(bootstrap=True, 
                            class_weight=None, 
                            criterion='gini',
                            min_samples_leaf=1,
                            n_estimators=100,
                            max_depth=10, 
                            random_state=123).fit(X, y)

# Create a DataFrame to hold predictions
    
    results = pd.DataFrame(
        {'Actual_Gender': test.gender,
         'Model_Predictions': forest.predict(X),
         'Model_Probabilities': forest.predict_proba(X)[:,1]
        })

# Generate csv
    
    results.to_csv('modeling_results.csv')

    return results