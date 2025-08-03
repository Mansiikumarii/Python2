import pandas as pd
csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv'
df = pd.read_csv(csv_path)
df.head()  # Display the first few rows of the DataFrame
df.tail()  # Display the last few rows of the DataFrame

xlsx_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n9LOuKI9SlUa1b5zkaCMeg/Product-sales.xlsx'
df = pd.read_excel(xlsx_path)
df.head()
x = df['Quantity']  # Access column 'Quantity'
print(x)  # Get unique values in column 'Quantity'

x= df['Product']  # Get unique values in column 'Product'
print(x)
x = df[['Product', 'Quantity']]  # Access multiple columns
print(x)

y = df[['Product', 'Quantity','Category']]  # Access multiple columns
print(y)

df.iloc[0,0]  # Access rows by index
df.iloc[1,0]  # Access another row by index

#accessing column by name
z=df.loc[0, 'Product']  # Access first row of 'Product' column
print(z)

#perform slicing using both the index and the name of the column
print(df.iloc[0:2,0:3])  # Slicing first two rows and first three columns
print(df.loc[0:2,'OrderID':'Category'])  # Slicing first three rows and specific columns by name