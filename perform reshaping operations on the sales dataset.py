import pandas as pd
data={'Store':['S1','S4','S3','S1','S2','S3','S1','S2','S3'],‘Year':[2016,2016,2016,2017,2017,2017,2018,
2018,2018], 'Total_sales(Rs)' : [12000,330000,420000,20000,10000,450000,30000,11000,89000],
'Total_profit(Rs)':[1100,5500,21000,32000,9000,45000,3000,1900,23000]}
df-pd.DataFrame(data)
print (df)
S1df = df[df.Store== 'S1' ]
print ($1df)
Sum=S1df[ 'Total_sales(Rs)' ].sum()
print (Sum)
S3df - df[df.Store== 'S3']
print (S3df)
Sum1=S3df[ ' Total_sales (Rs)' ].sum()
print (Sum1)
Sum2=S2df[ ' Total sales (Rs) ' ].sum()
print (Sum2)
pivot1=df.pivot(index='Store' ,columns='Year' ,values= 'Total_sales (Rs)')
print (pivot1)
print (pivot1.loc['S1'].sum())
print (pivot1.loc['S3'].max())
S1total = pivot1. loc['S1'].sum()
S2total = pivot1. loc['S2'].sum()
18
S3total = pivot1. loc['S3'].sum()
S4total = pivot1. loc['S4'].sum()
M=max (S1total,S2total,S3total, S4total)
print (M)