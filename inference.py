from tensorflow.keras.models import load_model
import pickle
import numpy as np

print("Prediction Pipeline started:")

model = load_model("coffeeModel.h5")
print("Model loaded")

with open('normalizer.pkl','rb') as f:
    norm_l = pickle.load(f)
print("Normalizer Loaded")

# Input test data
X_test = np.array(
    [
        [200, 13.9],  # good example
        [220, 13],  # perfect example
        [1000, 200],  # worst example
    ]
)

# Normalizing the the test data
X_testn = norm_l(X_test)
predictions = model.predict(X_testn)
yHat = (predictions > 0.5).astype(int)


print("Predictions:",predictions.flatten())
print("Predicted Labels:",yHat)
