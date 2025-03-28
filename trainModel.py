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
import pickle


print("Traning pipeline started:")
start = time()

# Load Data
X, y = loadCoffeeData()

# normalising the data set
set_seed(1234)  # to get consistent result

norm_l = Normalization(axis=-1)
norm_l.adapt(X)  # setting up accoring to coffee data set.
Xn = norm_l(X)  # Also, the mean and varience of the data set is now 0,1 resp

X_train = np.tile(Xn, (1000, 1))
y_train = np.tile(y, (1000, 1))

# setting up neural network
inputLayer = Input(shape=(2,))
layer1 = Dense(units=3, activation="sigmoid", name="layer1")
layer2 = Dense(units=1, activation="sigmoid", name="layer2")
model = Sequential([inputLayer, layer1, layer2])

# Compiling
model.compile(
    loss=binary_crossentropy,
    optimizer=Adam(learning_rate=0.01),
)

# training the model
model.fit(X_train, y_train, epochs=10)

# saving the model
model.save("coffeeModel.h5")
with open('normalizer.pkl','wb') as f:
    pickle.dump(norm_l,f)

end = time()

print(f"Traning completed in:{end-start}")
print("Model and Normalizer saved sucessfully")