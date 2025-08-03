import requests
import pandas as pd
data2 = requests.get("https://official-joke-api.appspot.com/jokes/ten")
result2 = data2.json()
df3 = pd.DataFrame(result2)
df3.drop(columns=["type","id"], inplace=True)
print(df3)
df3.to_csv("jokes.csv", index=False)
joke = df3.loc[df3['setup'] == 'Why did the chicken cross the road?']
if not joke.empty:
    print(joke.iloc[0]['punchline'])
    print(joke.iloc[0]['setup'])
else:
    print("Joke not found in the current API response. ")