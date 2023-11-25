import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.metrics import accuracy_score, f1_score

iris = load_iris()
X = iris.data[:, 2:]
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)

# knn = KNeighborsClassifier().fit(X_train, y_train)
# y_pred_knn = knn.predict(X_test)

tr = tree.DecisionTreeClassifier()
# y_pred_tree = tr.predict(X_test)

hyperparams = [
    {
        'criterion': ['gini', 'entropy'],
        'ccp_alpha' : [0, 0.02, 0.05, 0.1, 0.3, 0.5, 1]
    }
]

grid = GridSearchCV(tr, hyperparams, cv=10).fit(X_train, y_train)
print("Najbolji hiper", grid.best_params_)

tr.ccp_alpha = grid.best_params_['ccp_alpha']
tr.criterion = grid.best_params_['criterion']
tr.fit(X_train, y_train)
y_pred_tree = tr.predict(X_test)

plt.figure(figsize=(7, 7))
_ = tree.plot_tree(tr, feature_names=iris.feature_names, 
                   class_names=iris.target_names,
                   filled=True)
plt.show()

# print("Tacnost KNN: {form}".format(form = accuracy_score(y_test, y_pred_knn)))
print("Tacnost Tree: {form}".format(form = accuracy_score(y_test, y_pred_tree)))