import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle
import os # Need this for checking file existence

# (The data loading and cleaning code remains the same as before)
# --- 1. DATA LOADING AND CLEANING ---
try:
    dataset = pd.read_csv('btim.csv', na_values='NA')
except FileNotFoundError:
    print("Creating dummy heart_data.csv file.")
    csv_data = """male,age,education,currentSmoker,cigsPerDay,BPMeds,prevalentStroke,prevalentHyp,diabetes,totChol,sysBP,diaBP,BMI,heartRate,glucose,TenYearCHD
1,39,4,0,0,0,0,0,0,195,106,70,26.97,80,77,0
0,46,2,0,0,0,0,0,0,250,121,81,28.73,95,76,0
1,48,1,1,20,0,0,0,0,245,127.5,80,25.34,75,70,0
0,61,3,1,30,0,0,1,0,225,150,95,28.58,65,103,1
0,46,3,1,23,0,0,0,0,285,130,84,23.1,85,85,0
0,43,2,0,0,0,0,1,0,228,180,110,30.3,77,99,0
0,63,1,0,0,0,0,0,0,205,138,71,33.11,60,85,1
0,45,2,1,20,0,0,0,0,313,100,71,21.68,79,78,0
0,39,2,1,9,0,0,0,0,226,114,64,22.35,85,NA,0
1,41,2,0,0,0,0,0,0,195,139,88,26.88,85,65,0
0,43,1,0,0,0,0,0,0,185,123.5,77.5,29.89,70,NA,0
1,52,1,0,0,0,0,1,0,260,141.5,89,26.36,76,79,0
    """
    with open('heart_data.csv', 'w') as f:
        f.write(csv_data)
    dataset = pd.read_csv('heart_data.csv', na_values='NA')

dataset.fillna(dataset.mean(), inplace=True)

def train_and_save_model():
    print("\n--- Initiating Model Training Protocol ---")
    X = dataset.drop('TenYearCHD', axis=1)
    y = dataset['TenYearCHD']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(solver='liblinear', max_iter=1000)
    model.fit(X_train, y_train)
    print("Model Training Complete.")
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy on test data: {accuracy * 100:.2f}%")
    model_filename = 'heart_disease_classifier.pkl'
    with open(model_filename, 'wb') as file:
        pickle.dump(model, file)
    print(f"Model saved to '{model_filename}'")

def predict_new_patient():
    print("\n--- New Patient Diagnosis Protocol ---")
    model_filename = 'heart_disease_classifier.pkl'
    if not os.path.exists(model_filename):
        print(f"ERROR: Model file not found at '{model_filename}'")
        print("Please run the training option first to create the model file.")
        return
    with open(model_filename, 'rb') as file:
        model = pickle.load(file)
    print("AI Diagnosis Model loaded successfully.")
    feature_columns = [
        'male', 'age', 'education', 'currentSmoker', 'cigsPerDay', 'BPMeds',
        'prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol', 'sysBP',
        'diaBP', 'BMI', 'heartRate', 'glucose'
    ]
    patient_data = {}
    print("Please enter the patient's data:")
    for col in feature_columns:
        while True:
            try:
                value = input(f" - Enter value for '{col}': ")
                patient_data[col] = float(value)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
    input_df = pd.DataFrame([patient_data])
    prediction = model.predict(input_df)
    probabilities = model.predict_proba(input_df)
    risk_probability = probabilities[0][1]
    print("\n--- DIAGNOSTIC REPORT ---")
    if prediction[0] == 1:
        print("RESULT: High Risk of 10-Year Coronary Heart Disease.")
    else:
        print("RESULT: Low Risk of 10-Year Coronary Heart Disease.")
    print(f"Confidence Score (Risk Probability): {risk_probability * 100:.2f}%")
    print("-------------------------")


# --- MAIN APPLICATION LOOP ---
while True:
    print('''
****************************************
** AI Heart Disease Diagnostic System **
****************************************
1. Train and Save AI Model
2. Diagnose a New Patient
0. Exit Program
****************************************''')
    try:
        chon = int(input("Select an option: "))
        if chon == 1:
            train_and_save_model()
        elif chon == 2:
            predict_new_patient()
        elif chon == 0:
            print("Exiting system. Stay safe.")
            break
        else:
            print("Invalid option. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")
