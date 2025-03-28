
# ☕ Coffee Roast Classifier

A simple neural network model to classify coffee roast data using TensorFlow and Keras. This project demonstrates:
- Data normalization
- Neural network training
- Basic prediction
- CI/CD workflow using GitHub Actions

---

## 📂 Project Structure
```
.
├── trainModel.py          
├── inference.py        
├── coffeeRoastUtils.py     
├── requirements.txt        
└── .github/workflows/
    └── coffee_roast.yml    
```
---

## 🚀 Setup Instructions

1. Clone the repository:
 ```
   git clone https://github.com/YourUsername/Coffee_Roast.git
   cd Coffee_Roast
```

3. (Optional) Create a virtual environment:
```
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   .\venv\Scripts\activate    # For Windows
```
5. Install the dependencies:
```
   pip install -r requirements.txt
```
---

## 🟣 Training the Model
```
  python trainModel.py
```
---

## 🟡 Running Predictions
```
  python inference.py
```
---

## ✅ GitHub Actions Workflow

This repository contains a CI workflow:
- Automatically runs on every push to main
- Installs dependencies
- Trains the model
- Makes predictions

---

## 💡 Notes

- The dataset is loaded using coffeeRoastUtils.py.
- The model is a simple feedforward neural network.
- Predictions are binary classifications.

---

## 👨‍💻 Author

Prince Khatri  
[GitHub Profile](https://github.com/Prince-Khatri)


