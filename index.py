python
import pandas as pd
import matplotlib.pyplot as plt

# Load the transportation data
transport_data = pd.read_csv('Public_Transportation_Usage_Statistics_2023.csv')

# Load the financial data
finance_data = pd.read_excel('Indices Summary - Mar 2022 - Nov 2025.xlsx')

# Preprocess data if necessary
transport_data['Date'] = pd.to_datetime(transport_data['Date'])
finance_data['Date'] = pd.to_datetime(finance_data['Date'])

# Merge datasets on the Date column
merged_data = pd.merge(transport_data, finance_data, on='Date', how='inner')

# Analyze correlation between transportation usage and market index
correlation = merged_data['Passengers'].corr(merged_data['FADX15_Close'])
print(f'Correlation between transportation usage and FADX15 index: {correlation}')

# Visualize the data
plt.figure(figsize=(12, 6))
plt.plot(merged_data['Date'], merged_data['Passengers'], label='Transportation Usage')
plt.plot(merged_data['Date'], merged_data['FADX15_Close'], label='FADX15 Index')
plt.xlabel('Date')
plt.ylabel('Values')
plt.title('Integrated Analysis of Transportation Usage and Financial Market Index')
plt.legend()
plt.show()
