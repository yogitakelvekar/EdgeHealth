# Cardiovascular Health Data ETL Pipeline

This project is an ETL (Extract, Transform, Load) pipeline that processes a cardiovascular health dataset provided by the Department of Health and Social Care for the year 2021. The goal is to identify the top 5 Clinical Commissioning Groups (CCGs) with the highest mortality rates from heart disease and stroke combined, and generate a chart to visualize these results.

## Table of Contents
- [Installation](#installation)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [Methodology](#methodology)
- [License](#license)

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/cardiovascular-health-etl.git
```

## 2. Install Dependencies

Navigate to the project folder and install the required Python packages:

```bash
pip install -r requirements.txt
```

The required libraries are:

- **pandas**
- **seaborn**
- **matplotlib**
- **openpyxl** (for reading Excel files)

## Project Structure

```bash
cardiovascular-health-etl/
│
├── data/                                   # Folder containing the input data
│   └── Cardiovascular_health_indicators_2021.xlsx
│
├── output/                                 # Folder where the output chart will be saved
│   └── top_5_ccgs_mortality_rate_chart.png
│
├── etl/
│   ├── data_extractor.py                   # Module for extracting data from the Excel file
│   ├── data_transformer.py                 # Module for transforming the data (calculating mortalities)
│   └── data_visualizer.py                  # Module for visualizing the results
│
├── main.py                                 # Main script that runs the ETL pipeline
├── requirements.txt                        # File listing the required dependencies
├── README.md                               # This file
└── tests/                                  # Optional folder for test scripts (if applicable)
```

## How to Run

Make sure the dataset is placed in the `data/` folder as `Cardiovascular_health_indicators_2021.xlsx`.

Run the pipeline by executing the following command in the terminal:

```bash
python main.py
```

Once the script completes, the chart will be saved in the output/ folder as top_5_ccgs_mortality_rate_chart.png.

## Methodology

### Data Extraction
- The dataset is loaded from an Excel file using the `openpyxl` engine.

### Data Transformation
- Total mortalities from heart disease and stroke are calculated.
- Mortality rates are then computed by dividing the total mortalities by the population of the CCG.
- The top 5 CCGs with the highest mortality rates are identified.

### Data Visualization
- A bar chart is created using Seaborn to display the top 5 CCGs and their mortality rates.
