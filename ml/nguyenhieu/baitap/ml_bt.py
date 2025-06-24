import pandas as pd
from sklearn.linear_model import LogisticRegression # LinearRegression works by fitting a straight line to the data, it fits when we want to predict value that can be anywhere on a scale such as salary. But here, our target "TenYearCHD" is either 0 or 1, straight line is a wrong tool. So we use LogisticRegression (an "S"-shaped curve)
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Since we can't build a model with non-numeric data or empty cell. We need to tell pandas to treat "NA" as NaN value right when we load the data.
# After that, we need a strategy for NaN, a common way is to fill them with the average of the column
def deal_with_na(file_path):
    dataset = pd.read_csv(file_path, na_values='NA')

    # fill missing value
    dataset.fillna(dataset.mean(), inplace=True)

    return dataset


def main():
    file_path = 'btim.csv'

    dataset = deal_with_na(file_path)

    dataset.info()

    # 1. Define features x and target y
    # x is all columns except our target 'TenYearCHD'
    X = dataset.drop("TenYearCHD", axis=1)
    # y is only the 'TenYearCHD' column
    y = dataset['TenYearCHD']

    # 2. Split the data (80% for training, 20% for testin   
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. Crete the model instance
    model = LogisticRegression(solver='liblinear', max_iter=1000)

    # 4. Train the model
    model.fit(X_train, y_train)

    print("Model training is complete. Systems are green.")

    # 5. Make predictions on the test data
    y_pred = model.predict(X_test)

    # 6. Evaluate the predictions
    # Accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuraacy: {accuracy * 100:.2f}%")

    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    print(cm)

    print("--- Interpreting the Matrix ---")
    print(f"True Negatives (Correctly predicted NO): {cm[0][0]}")
    print(f"False Positives (Incorrectly predicted YES): {cm[0][1]}")
    print(f"False Negatives (Incorrectly predicted NO): {cm[1][0]}")
    print(f"True Positives (Correctly predicted YES): {cm[1][1]}")


if __name__ == "__main__":
    main()
