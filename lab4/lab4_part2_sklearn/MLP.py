from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
import numpy as np

sclaer = MinMaxScaler()
data = np.load('./data/DatawithrawL.npy')
a = data[:,:-1]
b = data[:,-1]
stl_b = sclaer.fit_transform(b.reshape(-1,1))
x_train,x_test,y_train,y_test = train_test_split(a,stl_b,test_size=0.2)
clf = MLPRegressor(hidden_layer_sizes=(128,8),activation='relu',solver='adam',batch_size=1024,learning_rate_init=0.1,max_iter=10000000)
rf = clf.fit (x_train, y_train.ravel())
stl_y_pred = rf.predict(x_test)
y_pred = sclaer.inverse_transform(stl_y_pred.reshape(-1,1))
y_test_rst = sclaer.inverse_transform(y_test.reshape(-1,1))
print("MLP结果如下：")
print("MSE：",mean_squared_error(y_test_rst,y_pred))
