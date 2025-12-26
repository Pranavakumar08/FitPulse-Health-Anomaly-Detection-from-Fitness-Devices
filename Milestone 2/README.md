# Milestone 2: Feature Extraction and Modeling

## Objective
Extract meaningful time-series features from fitness device data and model behavioral trends to support anomaly detection.

## Datasets Used
- health_fitness_dataset.csv (raw data)
- cleaned_health_fitness_data.csv (preprocessed data)

## Steps Performed
- Time-series feature extraction using TSFresh
- Feature selection using variance thresholding
- Trend modeling using Facebook Prophet
- Behavioral clustering using KMeans and DBSCAN
- Dimensionality reduction using PCA

## Tools and Libraries
- Python
- Pandas, NumPy
- TSFresh
- Facebook Prophet
- Scikit-learn
- Matplotlib

## Key Observations
- Seasonal patterns visible in heart rate, steps, and sleep
- Clustering distinguishes normal and atypical behavior patterns
- Residuals from Prophet forecasts indicate anomalies

(Include screenshots of plots and outputs here)
