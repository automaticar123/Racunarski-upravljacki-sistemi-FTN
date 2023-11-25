import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score

global X_train
global X_test
global y_train
global y_test

def train_me(model: LogisticRegression | KNeighborsClassifier | DecisionTreeClassifier):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print(f'Accuracy of {model} is {accuracy_score(y_true=y_test, y_pred=y_pred)}')

    if type(model) == KNeighborsClassifier:
        print(f'Confussion matrix of {model} is \r\n{confusion_matrix(y_true=y_test, y_pred=y_pred)}')

    elif type(model) == LogisticRegression:
        params = [{
            'C':[10, 40, 300, 434]
        }]
        gs = GridSearchCV(model, params, cv=2, verbose=10).fit(X_train, y_train)
        model.C = gs.best_params_['C']
        print(f'F1 score of {model} is {f1_score(y_true=y_test, y_pred=y_pred)}')


dataset = pd.read_csv('Churn.csv')

X = dataset.drop('Exited', axis='columns')
y = dataset['Exited'].values.reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    stratify=y)

model_lr = LogisticRegression()
model_knn = KNeighborsClassifier()
model_dt = DecisionTreeClassifier()

train_me(model_lr); train_me(model_knn); train_me(model_dt)