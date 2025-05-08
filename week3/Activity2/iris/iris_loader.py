import pandas as pd
import os

# Set the relative file path to the iris.data file
file_path = os.path.join(os.path.dirname(__file__), "iris.data")

# Define column names for the dataset
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

def load_iris_data():
    """Reads the iris dataset from a local .data file and returns a DataFrame."""
    df = pd.read_csv(file_path, names=columns)

    # Display the first 5 rows of the dataset
    # print("First 5 rows of the dataset:")
    # print(df.head())

    # Extract and display all unique flower class names
    flower_names = df['class'].unique()
    print("\nUnique flower names:")
    print(flower_names)

    # Summary statistics of numerical features
    # print("\nSummary statistics:")
    # print(df.describe())

    return df
