import pandas 
import math
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

dataset = pandas.read_csv("Salary_Data.csv")
#print(dataset.head())

# salaries = dataset["Salary"]
# experience = dataset["YearsExperience"]

y = dataset["Salary"]
X = dataset["YearsExperience"].values.reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_predicted = regressor.predict(X_test)

print("Prosjecna greska: ", "%.2f" % math.sqrt(mean_squared_error(y_test, y_predicted)))
print("a =  ", regressor.coef_)
print("b = ", regressor.intercept_)

plt.scatter(X_test, y_test, color="red")
plt.plot(X_train, regressor.predict(X_train), color="blue")
plt.title("Naslov grafika"); plt.xlabel("Godine iskustva"); plt.ylabel("Plata")
plt.show()