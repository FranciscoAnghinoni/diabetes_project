# Diabetes Analysis Dashboard

## Project Overview

This interactive dashboard provides comprehensive analysis of the Pima Indians Diabetes Database, which contains diagnostic measurements for females at least 21 years old of Pima Indian heritage. The dashboard visualizes relationships between different health metrics and diabetes diagnosis, allowing users to explore and understand factors that contribute to diabetes risk.

## Features

- **Data Overview**: Displays summary statistics and sample records from the dataset
- **Feature Distributions**: Visualizes the distribution of key features like Glucose, BMI, and Age grouped by diabetes outcome
- **Interactive Feature Analysis**: Allows users to:
  - Select any two features to compare in a scatter plot
  - Filter data using a dynamic threshold slider
  - Toggle regression trendline on/off
  - View correlation analysis between selected features
- **SQL Query Demonstration**: Shows SQL query capabilities with live results
- **Correlation Matrix**: Displays relationships between all features
- **Outcome Distribution**: Shows proportion of positive and negative diabetes diagnoses
- **Feature Impact Analysis**: Ranks features by their correlation with diabetes outcome

## Data Description

The dataset includes several medical predictors and one target variable:

- **Pregnancies**: Number of times pregnant
- **Glucose**: Plasma glucose concentration (2 hours in an oral glucose tolerance test)
- **BloodPressure**: Diastolic blood pressure (mm Hg)
- **SkinThickness**: Triceps skin fold thickness (mm)
- **Insulin**: 2-Hour serum insulin (mu U/ml)
- **BMI**: Body mass index (weight in kg/(height in m)²)
- **DiabetesPedigreeFunction**: Diabetes pedigree function (a function which scores likelihood of diabetes based on family history)
- **Age**: Age in years
- **Outcome**: Class variable (0 or 1) indicating presence of diabetes

## Setup

1. Install the required dependencies:

   ```
   pip install preswald pandas numpy plotly statsmodels
   ```

2. Configure your data connections in `preswald.toml`

   - The app expects a CSV data source named "diabetes_csv"
   - Verify the CSV path is correctly set in the configuration file

## Running the Dashboard

### Local Deployment

Run the application locally with:

```
preswald run
```

### Cloud Deployment

There are two options for deploying to Structured Cloud:

#### Option 1: Deploy with GitHub integration (Recommended)

1. Create a GitHub repository and push your code:

   ```
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/diabetes_project.git
   git push -u origin main
   ```

2. Deploy with GitHub integration:
   ```
   preswald deploy --target structured --github YOUR_USERNAME --api-key YOUR_API_KEY
   ```

#### Option 2: Deploy directly without GitHub

```
preswald deploy --target structured --api-key YOUR_API_KEY
```

**Note:** Replace `YOUR_USERNAME` with your GitHub username and `YOUR_API_KEY` with your Structured Cloud API key.

## Usage Guide

1. **Browse the Dataset**: Start by examining the sample data and summary statistics
2. **Explore Feature Distributions**: Review the histograms to understand how features are distributed
3. **Interactive Analysis**:
   - Use the dropdown menus to select which features to compare
   - Adjust the threshold slider to filter data points
   - Toggle the regression trendline checkbox to see trend lines
   - Review the correlation analysis below the scatter plot
4. **View the Correlation Matrix**: Identify which features have the strongest relationships
5. **Check Feature Impact**: See which features have the strongest correlation with diabetes diagnosis

## Technical Details

- Built using the Preswald framework for Python
- Visualizations created with Plotly Express
- Data manipulation with Pandas and NumPy
- Statistical analysis with statsmodels

## References

- Dataset: Pima Indians Diabetes Database (originally from the National Institute of Diabetes and Digestive and Kidney Diseases)
- Built with Preswald (https://www.preswald.com/)
