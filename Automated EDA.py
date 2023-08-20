import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def load_data(file_path):
    # Load data from various formats (CSV, Excel, SQL)
    if file_path.endswith('.csv'):
        data = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
        data = pd.read_excel(file_path)
    elif file_path.endswith('.db'):
        # Load data from SQL database
        # Implement code to connect to SQL database and fetch data
        pass
    else:
        raise ValueError("Invalid file format. Only CSV, Excel, and SQL databases are supported.")

    return data

def preprocess_data(data):
    # Identify data types of each column
    data_types = data.dtypes

    # Handle missing values
    data = data.dropna()

    # Encode categorical features
    categorical_columns = data.select_dtypes(include=['object']).columns
    data = pd.get_dummies(data, columns=categorical_columns)

    # Scale numerical features
    numerical_columns = data.select_dtypes(include=['int64', 'float64']).columns
    data[numerical_columns] = (data[numerical_columns] - data[numerical_columns].mean()) / data[numerical_columns].std()

    return data

def visualize_data(data):
    # Generate visualization dashboard for each column type
    for column in data.columns:
        if data[column].dtype == 'object':
            # Categorical column
            fig = px.histogram(data, x=column)
            fig.show()
        else:
            # Numerical column
            fig, axes = plt.subplots(1, 2, figsize=(10, 5))
            sns.boxplot(data[column], ax=axes[0])
            sns.histplot(data[column], ax=axes[1])
            plt.show()
            

# Main function
def main():
    file_path = "path_to_your_data_file"
    data = load_data(file_path)
    preprocessed_data = preprocess_data(data)
    visualize_data(preprocessed_data)

if __name__ == "__main__":
    main()

