<h1>Milestone 1</h1>
This Milestone explores basic data preprocessing.
<h2>Data</h2>
The Milestone 1 folder contains a data folder within which are a raw data file (or source data) file named "health_fitness_dataset.zip" and cleaned data file named "cleaned_health_fitness_data.csv". The sorce data is zipped since the dataset is huge. The dataset is sourced from: https://www.kaggle.com/datasets/jijagallery/fitlife-health-and-fitness-tracking-dataset?resource=download
<h2>Operations</h2>
The operations performed on the data for preprocessing using python are in data_preprocess.ipynb file. Since the dataset is mainly a clean one, no major data cleaning is needed. Only two things are done:<br>
1. The 'health_condition' column is removed due to an abundance of null data.<br>
2. The type of 'date' column is converted from object to datetime.
<h2>Requirementss</h2>
The Data preprocessing only requires 2 python libraries: Pandas and Scikit-learn.
