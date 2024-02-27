import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the dataset as a Pandas dataframe
df = pd.read_csv('/content/transactions.csv')

# Return the column names as a list
column_names = list(df.columns)

# Return the first k rows from the dataframe
def get_first_k_rows(k):
    return df.head(k)

# Return a random sample of k rows from the dataframe
def get_random_sample(k):
    return df.sample(k)

# Return a list of unique transaction types
unique_transaction_types = df['type'].unique().tolist()

# Return a Pandas series of the top 10 transaction destinations with frequencies
top_destinations = df['nameDest'].value_counts().head(10)

# Return all the rows from the dataframe for which fraud was detected
fraudulent_transactions = df[df['isFraud'] == 1]

# Bonus: Return a dataframe with the number of distinct destinations each source has interacted with
distinct_destinations = df.groupby('nameOrig')['nameDest'].nunique().reset_index()
distinct_destinations = distinct_destinations.sort_values(by='nameDest', ascending=False)

# Display the results
print("Column Names:", column_names)
print("\nFirst 5 Rows:")
print(get_first_k_rows(5))
print("\nRandom Sample of 5 Rows:")
print(get_random_sample(5))
print("\nUnique Transaction Types:", unique_transaction_types)
print("\nTop 10 Transaction Destinations with Frequencies:")
print(top_destinations)
print("\nRows with Fraud Detected:")
print(fraudulent_transactions)
print("\nDistinct Destinations Each Source Has Interacted With (Top 5):")
print(distinct_destinations.head(5))


# Function to create Transaction Types Bar Chart
def plot_transaction_types_bar_chart():
    plt.figure(figsize=(10, 6))
    df['type'].value_counts().plot(kind='bar', color='skyblue')
    plt.title('Transaction Types Bar Chart')
    plt.xlabel('Transaction Type')
    plt.ylabel('Frequency')
    plt.show()
    return "This bar chart illustrates the distribution of different transaction types, providing insight into the most common types of transactions."

# Function to create Transaction Types Split by Fraud Bar Chart
def plot_transaction_types_fraud_bar_chart():
    plt.figure(figsize=(10, 6))
    pd.crosstab(df['type'], df['isFraud']).plot(kind='bar', stacked=True, color=['green', 'red'])
    plt.title('Transaction Types Split by Fraud Bar Chart')
    plt.xlabel('Transaction Type')
    plt.ylabel('Frequency')
    plt.legend(['Not Fraud', 'Fraud'])
    plt.show()
    return "This bar chart shows the distribution of transaction types, with each bar split by fraud status. It helps identify if certain transaction types are more prone to fraud."

# Function to create Origin vs Destination Account Balance Delta Scatter Plot for Cash Out Transactions
def plot_balance_delta_scatter_plot():
    cash_out_data = df[df['type'] == 'CASH_OUT']
    plt.figure(figsize=(10, 6))
    plt.scatter(cash_out_data['newbalanceOrig'], cash_out_data['newbalanceDest'], alpha=0.5, color='orange')
    plt.title('Origin vs Destination Account Balance Delta Scatter Plot (Cash Out Transactions)')
    plt.xlabel('Origin Account Balance Delta')
    plt.ylabel('Destination Account Balance Delta')
    plt.show()
    return "This scatter plot visualizes the relationship between origin and destination account balance deltas for Cash Out transactions. It helps in understanding the flow of money in these transactions."

# Example usage of the functions
print(plot_transaction_types_bar_chart())
print(plot_transaction_types_fraud_bar_chart())
print(plot_balance_delta_scatter_plot())


import matplotlib.pyplot as plt

# Function to create a custom visual
def visual_custom():
    # Calculate the average transaction amount for each transaction type
    avg_amount_by_type = df.groupby('type')['amount'].mean().sort_values()

    # Plotting bar chart for average transaction amount by type
    plt.figure(figsize=(10, 6))
    avg_amount_by_type.plot(kind='bar', color='skyblue')
    plt.title('Average Transaction Amount by Transaction Type')
    plt.xlabel('Transaction Type')
    plt.ylabel('Average Transaction Amount')
    plt.show()

    return "This bar chart illustrates the average transaction amount for each transaction type. It provides insights into the typical size of transactions for different types, helping to identify patterns and outliers."

# Example usage of the custom visual
print(visual_custom())
