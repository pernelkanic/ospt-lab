import pandas as pd
fruit_list = [(‘Orange’, 34, ‘Yes’ ),(‘Mango’, 24, ‘No’ ),(‘banana’, 14, ‘No’ ),(‘Apple’, 44, ‘Yes’ ),
(‘Pineapple’, 64, ‘No’),(‘Kiwi’, 84, ‘Yes’)] 
df = pd.DataFrame(fruit_list, columns = [‘Name’ , ‘Price’, ‘Stock’])
indexNames = df [df[‘Stock’] == ‘No’ ].index 
df.drop(indexNames , inplace=True) 
del df[‘Price’] 
print(df)