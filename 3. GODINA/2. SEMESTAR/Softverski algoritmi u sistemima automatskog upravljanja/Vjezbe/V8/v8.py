# import pandas
import warnings
from sklearn import datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
# import math

warnings.filterwarnings('ignore')

# Load datasets
X, y = datasets.load_breast_cancer(return_X_y=True)

# Split the dataset into training and testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.3, stratify=y)

# Make and fit the model
clf = LogisticRegression().fit(X_train, y_train)

# Calculate the prediction
y_pred = clf.predict(X_test)

print("Accuracy score: ", accuracy_score(y_true=y_test, y_pred=y_pred))
print("Confusion matrix: \n", confusion_matrix(y_true=y_test, y_pred=y_pred))
print("Precision metrics: ", precision_score(y_true=y_test, y_pred=y_pred))
print("Recall score metrics: ", recall_score(y_true=y_test, y_pred=y_pred))
print("F1 score metrics: ", f1_score(y_true=y_test, y_pred=y_pred))


# # Multinomial logistical regression
# X, y = datasets.load_digits(return_X_y=True)

# X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.3, stratify=y)

# clf = LogisticRegression(multi_class='multinomial').fit(X_train, y_train)
# y_pred = clf.predict(X_test)

# print("The achieved accuracy: ", "%.2f" % (accuracy_score(y_test, y_pred)*100))