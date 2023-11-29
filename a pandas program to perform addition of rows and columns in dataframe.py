import pandas as pd
data = {'Name': ['A', 'B', 'C', 'D'], 'Age': [28, 26, 24, 30], 'Qualification': ['Msc', "MA', 'Msc', 'Msc'])
df = pd.DataFrame(data)]
print(df)
address = ['Delhi', 'Bangalore', 'Chennai', 'Patna', 'Mumbai']
df=df.append({ 'Name' : 'E', 'Age' : 25, 'Qualification' : 'B.Tech'}, ignore_index=True)
df['Address'] = address
print(df)