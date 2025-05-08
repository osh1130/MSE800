import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from iris_loader import load_iris_data

def analyze_and_classify():
    # Load the cleaned iris dataset
    df = load_iris_data()

    # ------------------ Exploratory Data Analysis ------------------
    sns.pairplot(df, hue='class')
    plt.suptitle("Pairplot of Iris Features", y=1.02)
    plt.show()

    # ------------------ Machine Learning Classification ------------------
    # Convert class labels to numeric values
    df['class'] = df['class'].astype('category').cat.codes

    # Split data into features and target
    X = df.drop('class', axis=1)
    y = df['class']

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Random Forest model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = model.predict(X_test)
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

if __name__ == "__main__":
    analyze_and_classify()
