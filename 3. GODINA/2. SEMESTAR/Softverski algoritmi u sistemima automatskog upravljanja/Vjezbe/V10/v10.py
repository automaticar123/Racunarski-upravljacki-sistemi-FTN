from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plt
import pandas as pd

global X_train
global X_test
global y_train
global y_test

def train_it(model: LogisticRegression | KNeighborsClassifier | DecisionTreeClassifier):

    if type(model) == DecisionTreeClassifier:

        tree_params = [{
            'criterion': ['gini', 'entropy'],
            'ccp_alpha': [0.0, 0.2, 0.4, 0.6, 0.8, 1]
        }]

        gs = GridSearchCV(model, tree_params, cv=5).fit(X_train, y_train)

        model.criterion = gs.best_params_['criterion']
        model.ccp_alpha = gs.best_params_['ccp_alpha']

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    if type(model) == DecisionTreeClassifier:
        _ = plot_tree(model)
        plt.show()

    print(f'Accuracy of {str(model)}: {accuracy_score(y_true=y_test, y_pred=y_pred)}')

dataset = load_iris()
X = dataset.data[:, 2:]
y = dataset.target

X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.3,
                                                    stratify=y)

lr = LogisticRegression()
knn = KNeighborsClassifier()
tr = DecisionTreeClassifier()
train_it(tr)

