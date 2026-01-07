# Milestone 3: Anomaly Detection and Visualization

## Objective
To identify, label, and visualize anomalous health patterns in fitness device data using statistical, temporal, and clustering-based techniques.

## Steps Followed
1. Residual analysis using Prophet (actual vs predicted values)
2. Threshold-based anomaly detection using statistical deviation limits
3. Cluster-based anomaly identification using DBSCAN
4. Anomaly labeling (Normal vs Anomalous)
5. Interactive time-series visualization of anomalies

## Tools Used
- Python
- Pandas, NumPy
- Facebook Prophet
- Scikit-learn
- Plotly, Matplotlib

## Key Insights
- Heart rate anomalies correlate with sharp deviations from predicted trends
- Sleep anomalies indicate irregular or insufficient sleep patterns
- DBSCAN effectively isolates rare behavioral clusters
- Combined anomaly labeling improves detection reliability

## Visual Outputs
- Heart rate time-series with anomaly markers
- Sleep pattern visualization highlighting abnormal segments
