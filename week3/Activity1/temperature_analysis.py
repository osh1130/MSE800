import pandas as pd
import matplotlib.pyplot as plt
import argparse
import os

class TemperatureAnalyzer:
    def __init__(self, filepath, threshold=30.0):
        """Initialize analyzer with file path and temperature threshold."""
        self.filepath = filepath
        self.threshold = threshold
        self.df = None

    def load_data(self):
        """Load CSV data into a pandas DataFrame."""
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"File not found: {self.filepath}")
        self.df = pd.read_csv(self.filepath)

    def clean_data(self):
        """Clean the dataset by removing empty columns, parsing dates, and filling missing values."""
        # Drop unnecessary columns if they exist
        self.df = self.df.drop(columns=[
            'Grass Temperature [Deg C]',
            'Data Source (grass temp)',
            'Period (grass temp)'
        ], errors='ignore')

        # Convert observation time to datetime format
        self.df['Observation time UTC'] = pd.to_datetime(self.df['Observation time UTC'])

        # Set the datetime column as index for time-series operations
        self.df.set_index('Observation time UTC', inplace=True)

        # Fill missing mean temperature using average of max and min temperatures
        self.df['Mean Temperature [Deg C]'] = self.df['Mean Temperature [Deg C]'].fillna(
            (self.df['Maximum Temperature [Deg C]'] + self.df['Minimum Temperature [Deg C]']) / 2
        )

        # Interpolate missing values in relative humidity, if column exists
        if 'Mean Relative Humidity [percent]' in self.df:
            self.df['Mean Relative Humidity [percent]'] = self.df['Mean Relative Humidity [percent]'].interpolate()

        # Create new column for daily temperature range
        self.df['Daily Temp Range'] = self.df['Maximum Temperature [Deg C]'] - self.df['Minimum Temperature [Deg C]']

    def analyze_extreme_heat(self):
        """Identify and return records where max temperature exceeds the threshold."""
        return self.df[self.df['Maximum Temperature [Deg C]'] > self.threshold]

    def plot_monthly_trends(self, output_path="monthly_temp_trend.png"):
        """Generate and save a plot of monthly average temperature trends."""
        monthly_avg = self.df.resample('M').mean(numeric_only=True)
        plt.figure(figsize=(12, 6))
        plt.plot(monthly_avg.index, monthly_avg['Maximum Temperature [Deg C]'], label='Max Temp')
        plt.plot(monthly_avg.index, monthly_avg['Minimum Temperature [Deg C]'], label='Min Temp')
        plt.plot(monthly_avg.index, monthly_avg['Mean Temperature [Deg C]'], label='Mean Temp')
        plt.title('Monthly Average Temperature Trends')
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(output_path)
        print(f"Plot saved to {output_path}")


def main(filepath, threshold):
    """Main function to run temperature analysis using the TemperatureAnalyzer class."""
    try:
        analyzer = TemperatureAnalyzer(filepath, threshold)
        analyzer.load_data()
        analyzer.clean_data()
        analyzer.plot_monthly_trends()

        heat_days = analyzer.analyze_extreme_heat()
        print(f"Number of days with max temperature > {threshold}°C: {heat_days.shape[0]}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze daily temperature data from NIWA")
    parser.add_argument("--file", type=str, required=True, help="Path to CSV file")
    parser.add_argument("--threshold", type=float, default=30.0, help="Temperature threshold for extreme heat analysis")
    args = parser.parse_args()

    main(args.file, args.threshold)
