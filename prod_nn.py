import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.models import Sequential
from keras.layers import Dense
from keras.activations import linear, relu, sigmoid
import matplotlib.pyplot as plt

def loaddata():
    file=open("data.txt","r")
    matrice=[]
    vector=[]
    culori=[]
    size=[]
    while True:
        line=file.readline()
        if not line:
            break;
        linie=list(map(float,line.split()))
        size.append(linie.pop())
        culori.append(linie.pop())
        vector.append(linie.pop())
        matrice.append(linie)
    file.close() 
    vector=np.asarray(vector)
    culori=np.asarray(culori)
    size=np.asarray(size)
    mat=np.asarray(matrice)
    matrice=np.asmatrix(mat)
    return matrice,vector,culori,size

X, y, c, s = loaddata()
print ('The first element of X is: ', X[0])
print ('The first element of y is: ', y[0])
print ('The last element of y is: ', y[-1])
print ('The shape of X is: ' + str(X.shape))
print ('The shape of y is: ' + str(y.shape))
tf.random.set_seed(1234) # for consistent results
model = Sequential(
    [               
        tf.keras.Input(shape=(5,)),
        layers.Dense(25, activation="relu", name="layer1"),
        layers.Dense(15, activation="relu", name="layer2"),
        layers.Dense(40, activation="relu", name="layer3"),
        layers.Dense(7, name="layer4"), 
    ], name = "model" 
)
model.summary()
[layer1, layer2, layer3, layer4] = model.layers
#### Examine Weights shapes
W1,b1 = layer1.get_weights()
W2,b2 = layer2.get_weights()
W3,b3 = layer3.get_weights()
W4,b4 = layer4.get_weights()
#print(f"W1 shape = {W1.shape}, b1 shape = {b1.shape}")
#print(f"W2 shape = {W2.shape}, b2 shape = {b2.shape}")
#print(f"W3 shape = {W3.shape}, b3 shape = {b3.shape}")
#print(f"W4 shape = {W4.shape}, b4 shape = {b4.shape}")

model.compile(
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
)

history = model.fit(
    X,y,
    epochs=100
)
#print(layer1.get_weights())
#print(layer2.get_weights())
#print(layer3.get_weights())
#print(layer4.get_weights())
print ('The shape of first element is: ' + str(X[0].shape))
model.save('first.model')
arr = np.array([[0, 7, 4, 8, 4398.90]])
print ('The shape of arr is: ' + str(arr.shape))
prediction = model.predict(arr)
print("aici1")
print(np.argmax(prediction))
print("aici2")