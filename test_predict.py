import tensorflow as tf
from tensorflow import keras
import numpy as np
model = keras.models.load_model("size.model")
arr = np.array([[0, 7, 4, 8, 4398.90]])
print ('The shape of arr is: ' + str(arr.shape))
prediction = model.predict(arr)
print("size prediction:")
print(np.argmax(prediction))
print("aici2")

model = keras.models.load_model("colour.model")
arr = np.array([[0, 5, 0, 8, 4398.90]])
print ('The shape of arr is: ' + str(arr.shape))
prediction = model.predict(arr)
print("colour prediction:")
print(np.argmax(prediction))
print("aici2")

model = keras.models.load_model("price.model")
arr = np.array([[0, 5, 0, 8, 1050.90]])
print ('The shape of arr is: ' + str(arr.shape))
prediction = model.predict(arr)
print("price prediction:")
print(np.argmax(prediction))
print("aici2")