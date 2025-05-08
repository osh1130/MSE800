from iris_loader import load_iris_data
from iris_analysis import analyze_and_classify

def main():
    print("Loading and describing the Iris dataset...")
    df = load_iris_data()

    print("\nAnalyzing and classifying the Iris dataset...")
    analyze_and_classify()

if __name__ == "__main__":
    main()
