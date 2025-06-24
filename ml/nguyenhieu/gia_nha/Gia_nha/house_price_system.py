import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error
import pickle
import os

# --- GLOBAL DATA PREPARATION ---
def load_and_prep_data():
    try:
        df = pd.read_csv('data.csv')
    except FileNotFoundError:
        print("ERROR: 'data.csv' not found. Please make sure the file is in the same directory.")
        return None
    
    df = df.drop(['date', 'street', 'statezip', 'country'], axis=1)
    df = pd.get_dummies(df, columns=['city'], drop_first=True)
    return df

# --- MODEL TRAINING FUNCTION ---
def train_and_evaluate(df):
    if df is None:
        return
    print("\n--- Initiating Price Model Training ---")
    X = df.drop('price', axis=1)
    y = df['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    r2 = r2_score(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)
    print("Training Complete.")
    print(f"Model R-squared: {r2:.2f}")
    print(f"Model Mean Absolute Error: ${mae:,.2f}")
    
    model_filename = 'house_price_predictor.pkl'
    with open(model_filename, 'wb') as file:
        pickle.dump((model, X.columns), file)
    print(f"Model and column data saved to '{model_filename}'")

# --- INTERACTIVE PREDICTION FUNCTION ---
def predict_new_house_price():
    # (Paste the function from Chapter 3 here)
    print("\n--- House Price Estimator ---")
    model_filename = 'house_price_predictor.pkl'
    try:
        with open(model_filename, 'rb') as file:
            model, saved_columns = pickle.load(file)
        print("AI Price Estimator loaded.")
    except FileNotFoundError:
        print(f"ERROR: Model file '{model_filename}' not found. Please train first.")
        return
    
    house_data = {}
    print("Please enter the new house's data:")
    city_input = input(" - Enter city name (e.g., Seattle, Redmond): ")
    
    city_related_columns = [col for col in saved_columns if col.startswith('city_')]
    numerical_columns = [col for col in saved_columns if col not in city_related_columns]

    for col in numerical_columns:
        while True:
            try:
                value = input(f" - Enter value for '{col}': ")
                house_data[col] = float(value)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    input_df = pd.DataFrame(columns=saved_columns)
    input_df.loc[0] = 0
    for col, value in house_data.items():
        input_df.loc[0, col] = value

    city_column_name = f'city_{city_input}'
    if city_column_name in saved_columns:
        input_df.loc[0, city_column_name] = 1
    else:
        print(f"WARNING: City '{city_input}' was not in the original training data.")

    predicted_price = model.predict(input_df)
    print("\n--- ESTIMATED PRICE REPORT ---")
    print(f"The estimated house price is: ${predicted_price[0]:,.2f}")
    print("----------------------------")


# --- MAIN APPLICATION LOOP ---
def main():
    master_df = load_and_prep_data()
    if master_df is None:
        return # Exit if data loading failed

    while True:
        print('''
****************************************
** AI House Price Prediction System    **
****************************************
1. Train and Save Price Model
2. Estimate Price for a New House
0. Exit Program
****************************************''')
        try:
            chon = int(input("Select an option: "))
            if chon == 1:
                train_and_evaluate(master_df)
            elif chon == 2:
                predict_new_house_price()
            elif chon == 0:
                print("Exiting system.")
                break
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == '__main__':
    main()
