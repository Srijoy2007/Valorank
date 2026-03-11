import numpy as np
import pandas as pd

training_set = pd.read_csv("valo_all_time.csv")

training_set = training_set.dropna(subset=["kd","kpr","adr","kast","fkpr","fdpr","rating"])

X = training_set[["kd","kpr","adr","kast","fkpr","fdpr"]].values
y = training_set["rating"].values
test_set = pd.read_csv("test_set.csv")
test_set = test_set.dropna(subset=["kd","kpr","adr","kast","fkpr","fdpr"])
X_test = test_set[["kd","kpr","adr","kast","fkpr","fdpr"]].values
y_test = test_set["rating"].values
test_set.columns = test_set.columns.str.strip()
mean = X.mean(axis=0)
std = X.std(axis=0)
X_test = (X_test-mean)/std 
X = (X-mean)/std

m,n = X.shape
print("dataset size:",training_set.shape)

def cost_function(x,y,w,b):
    m = x.shape[0]
    cost_sum = 0
    for i in range(m):
        f = np.dot(w,x[i]) + b
        cost_sum += (f - y[i])**2
    return cost_sum/(2*m)

def gradient(x,y,w,b):
    m,n = x.shape
    dc_dw = np.zeros(n)
    dc_db = 0
    for i in range(m):
        f = np.dot(w,x[i]) + b
        error = f - y[i]
        for j in range(n):
            dc_dw[j] += error * x[i][j]
        dc_db += error
    dc_dw = dc_dw/m
    dc_db = dc_db/m
    return dc_dw, dc_db

def gradient_descent(x,y,alpha,iterations):
    m,n = x.shape
    w = np.zeros(n)
    b = 0
    for i in range(iterations):
        dc_dw, dc_db = gradient(x,y,w,b)
        w = w - alpha*dc_dw
        b = b - alpha*dc_db
        if i % 100 == 0:
            print("Iteration",i,"Cost",cost_function(x,y,w,b))
    return w,b

learning_rate = 0.001
iterations = 10000

final_w, final_b = gradient_descent(X,y,learning_rate,iterations)

print("w:",final_w)
print("b:",final_b)

prediction = X_test @ final_w + final_b

print("Prediction",prediction[:10])
print("actual",y_test[:10])

ss_res = np.sum((y_test-prediction)**2)
ss_tot = np.sum((y_test-np.mean(y_test))**2)
r2 = 1 - (ss_res/ss_tot)
print("Test R2:",r2)

