import pandas as pd
df=pd.read_csv('C:/Users/admin/Downloads/Student.csv')
g1=df.groupby('Name')
print (g1.first())
print(g1.size())
print(df.groupby (['Maths']).aggregate('mean'))
group1=df.groupby(['Maths'])
print(df.groupby(['Physics']).aggregate('mean'))
print(df.groupby(by= 'Name')['Chemistry'].aggregate(['mean' , 'var' , 'std' , 'quantile']))