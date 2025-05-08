# Temperature Analysis

This Python project analyzes daily temperature data from NIWA (National Institute of Water and Atmospheric Research, New Zealand). It performs data cleaning, temperature trend visualization, and extreme heat event detection.

---

## 📦 Requirements

Ensure you are using Python 3.7+ and install the following packages:

```bash
pip install pandas matplotlib
```

Alternatively, you can create and activate a virtual environment:

```bash
python -m venv mse800env
# On macOS/Linux
source mse800env/bin/activate
# On Windows
mse800env\Scripts\activate
pip install pandas matplotlib
```

---

## 🚀 How to Run

Assuming you're in the project folder `week3/Activity1`, run the script using:

```bash
python temperature_analysis.py --file 45935__Temperature__daily.csv
```

Optional: You can also set a different threshold (default is 30°C):

```bash
python temperature_analysis.py --file 45935__Temperature__daily.csv --threshold 28
```

---

## 📊 Features

- Load and clean NIWA daily climate data
- Fill missing values using interpolation or estimation
- Calculate daily temperature range
- Plot monthly temperature trends
- Detect and count days exceeding an extreme heat threshold

---

## 📈 Output

- A line chart of monthly temperature trends saved as: `monthly_temp_trend.png`
- Console output showing how many days exceeded the threshold

---

## 📁 Example Data Format

Your CSV file should contain at least the following columns:

- `Observation time UTC`
- `Maximum Temperature [Deg C]`
- `Minimum Temperature [Deg C]`
- `Mean Temperature [Deg C]`
- `Mean Relative Humidity [percent]` (optional)

---

## 🙏 Acknowledgments

Data sourced from [NIWA DataHub](https://data.niwa.co.nz/pages/clidb-on-datahub).  
Developed as part of a Python-based data science course (MSE800).

---

## 📜 License

For academic and non-commercial use.
