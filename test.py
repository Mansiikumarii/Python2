import pandas as pd

df=pd.DataFrame({'a':[11,21,31],'b':[21,22,23]})
df.to_csv('test.csv', index=False)
print("DataFrame saved to 'test.csv'")
df.head(3)  # Display the first 3 rows of the DataFrame
df.tail(3)  # Display the last 3 rows of the DataFrame 
df['a']  # Access column 'a'
df['a'].unique()  # Get unique values in column 'a'
print(df[df['a'] < 2])  # Filter rows where column 'a' is greater than 2




  