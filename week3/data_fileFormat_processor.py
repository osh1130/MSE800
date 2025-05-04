import pandas as pd
from PIL import Image
import os

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.file_type = self.detect_file_type()

    def detect_file_type(self):
        if self.file_path.endswith('.csv'):
            return 'csv'
        elif self.file_path.endswith('.parquet'):
            return 'parquet'
        elif self.file_path.endswith('.txt'):
            return 'text'
        elif self.file_path.endswith('.png') or self.file_path.endswith('.jpg'):
            return 'image'
        else:
            raise ValueError("Unsupported file format.")


    def load_data(self):
        if self.file_type == 'csv':
            self.data = pd.read_csv(self.file_path)
        elif self.file_type == 'parquet':
            self.data = pd.read_parquet(self.file_path)
        elif self.file_type == 'text':
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.data = f.read()
        elif self.file_type == 'image':
            self.data = Image.open(self.file_path)
        print(f"[✔] Data loaded successfully from {self.file_path}")


    def process(self):
        if self.data is None:
            raise ValueError("No data loaded.")

        if self.file_type in ['csv', 'parquet']:
            self.process_tabular_data()
        elif self.file_type == 'text':
            self.process_text_file()
        elif self.file_type == 'image':
            self.process_image_file()

    def process_tabular_data(self):
        print(" Tabular Data Summary:")
        print(self.data.info())
        print("\nMissing Values:")
        print(self.data.isnull().sum())
        print("\nDescriptive Statistics:")
        print(self.data.describe())

    def process_text_file(self):
        print(" Text File Summary:")
        num_lines = len(self.data.splitlines())
        num_words = len(self.data.split())
        num_underscores = self.data.count('__')
        print(f"Lines: {num_lines}, Words: {num_words}, '__' count: {num_underscores}")

    def process_image_file(self):
        print(" Image File Info:")
        print(f"Format: {self.data.format}")
        print(f"Size: {self.data.size} (Width x Height)")
        print(f"Mode: {self.data.mode}")

def main():
    file_path = input("Enter your file path: ").strip()
    file_path = os.path.join("week3", file_path)
    processor = DataProcessor(file_path)
    processor.load_data()
    processor.process()

if __name__ == "__main__":
    main()
