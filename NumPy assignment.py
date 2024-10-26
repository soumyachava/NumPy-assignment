#1
print("1","output")
import numpy as np
print("my numpy version is",np.__version__)

#2
print("2","output")
array_1d = np.arange(10)
print("array",array_1d)

#3
print("3","output")
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
iris_data = np.genfromtxt(url, delimiter=',', dtype=None, encoding=None)
print("Iris dataset:\n", iris_data)

#4
print ("4","0utput")
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
iris_data = np.genfromtxt(url, delimiter=',', dtype=None, encoding=None)

petal_width = np.array([float(row[3]) for row in iris_data if row[3] != ''])

position = np.where(petal_width > 1.0)[0][0]
print("Position of first occurrence where petal width > 1.0:", position)

#5
print("5","output")
np.random.seed(100)
a = np.random.uniform(1, 50, 20)
print("Original array:\n", a)
a_clipped = np.clip(a, 10, 30)
print("Modified array:\n", a_clipped)



