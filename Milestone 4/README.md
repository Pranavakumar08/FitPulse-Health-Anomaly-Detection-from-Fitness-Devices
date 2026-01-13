# Milestone 4: Dashboard for Insights

### Note:
The original dataset used in Milestone 1 had 3000 users' data which has been reduced to a dataset of 50 users in Milestone 4 (stored in data folder) for fast processing.

## Objective
The objective of this milestone is to develop an interactive dashboard for real-time visualization and detection of health anomalies using fitness device data.

## Dashboard Workflow
1. User uploads fitness data (CSV)
2. Automated preprocessing and datetime handling
3. Prophet-based trend modeling
4. Residual-based anomaly detection
5. Interactive visualization with anomaly markers
6. Downloadable anomaly summary report

## Tools & Libraries Used
- Streamlit
- Prophet
- Plotly
- Pandas
- Scikit-learn
- Google Colaboratory

## Key Insights
- Heart rate anomalies highlight abnormal physiological stress
- Sleep anomalies reveal irregular sleep patterns
- Step count deviations identify inactivity or excessive exertion

## Screenshots
- Dashboard UI: screenshots/dashboard_ui.png
- Report Download: screenshots/report_download.png
