from tensorflow.random import set_seed
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Normalization
from tensorflow.keras.losses import binary_crossentropy
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import Input
from coffeeRoastUtils import loadCoffeeData
import numpy as np
from time import time

print("Import Sucessful")
start = time()
# import data set
print("Importing dataset")
X, y = loadCoffeeData()
print("Imported dataset sucessfully")


print("Normalising the data set")
set_seed(1234)  # to get consistent result

# normalising the data set
norm_l = Normalization(axis=-1)
norm_l.adapt(X)  # setting up accoring to coffee data set.
Xn = norm_l(X)  # Also, the mean and varience of the data set is now 0,1 resp

X_train = np.tile(Xn, (1000, 1))
y_train = np.tile(y, (1000, 1))

print("Normalised the data set sucessfully")


# setting up neural network
print("Setting up neiral network")
inputLayer = Input(shape=(2,))
layer1 = Dense(units=3, activation="sigmoid", name="layer1")
layer2 = Dense(units=1, activation="sigmoid", name="layer2")
model = Sequential([inputLayer, layer1, layer2])
print("Setting up Completed for neiral network")


# training the model
print("Model training")
model.compile(
    loss=binary_crossentropy,
    optimizer=Adam(learning_rate=0.01),
)
print("Model Compile completed")


model.fit(X_train, y_train, epochs=10)
end = time()
print("Model Compile Trained")

print(f"tt:{end-start}")
# model training completed

X_test = np.array(
    [
        [200, 13.9],  # good example
        [220, 13],  # perfect example
        [1000, 200],  # worst example
    ]
)

X_testn = norm_l(X_test)

predictions = model.predict(X_testn)

# Function to make output human understandable
print(predictions)


yHat = (predictions > 0.5).astype(int)
# Printing the output to the console

print(yHat)
