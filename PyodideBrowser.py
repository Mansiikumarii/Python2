import pandas as pd
import requests

# URL of the CSV file
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv"

# Download the file
response = requests.get(url)

# Check if the download was successful
if response.status_code == 200:
    # Save the content to a local file
    with open("Product-sales.csv", "wb") as f:
        f.write(response.content)
    
    # Read the CSV using pandas
    df = pd.read_csv("Product-sales.csv")
    print(df.head())
else:
    print("Failed to download file:", response.status_code)
