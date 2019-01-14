import numpy as np
import matplotlib.pyplot as plt

X=[]
Y=[]
for line in open('data.csv'):
    x,y=line.split(',')
    X.append(float(x))
    Y.append(float(y))

X=np.array(X)
Y=np.array(Y)


D = X.dot(X) - X.mean()*X.sum()
a = (X.dot(Y) - Y.mean() * X.sum()) / D
b = (Y.mean()*X.dot(X) - X.mean()* X.dot(Y)) / D

Yh = a*X + b

plt.scatter(X,Y)
plt.plot(X, Yh)
plt.show


n1=Y-Yh
n2 = Y - Y.mean()
r2 = 1 - n1.dot(n1) / n2.dot(n2)
print(r2)
