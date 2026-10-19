## 📌 Objectives

- **Data Exploration**: Load datasets, verify data types, and inspect missing values.
- **Descriptive Statistics**: Measure central tendency (mean, median, mode) and variability (range, variance, standard deviation).
- **Correlation Analysis**: Compute linear relationships between numerical features.
- **Statistical Modeling**: Apply basic linear regression concepts to analyze feature interactions.




## Workflow & Implementation
1. Data Exploration
- Loaded sample dataset via pd.read_csv().

- Verified structure using data.head() and checked column data types with data.info().

- Generated quick summary stats via data.describe().

2. Basic Statistics
- Calculated mean(), median(), and mode() for all numerical columns.

- Variability: Calculated std(), var(), and feature ranges (max() - min()).

3. Feature Relationships
Generated a pairwise correlation matrix using data.corr() to evaluate feature dependencies.
