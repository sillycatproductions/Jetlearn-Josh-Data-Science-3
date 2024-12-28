import pandas as pd #pandas now identified as pd

df = pd.DataFrame({'Name':['AAAAAAA','BBBBBBBBB','CCCCCCC'], 'Age':[1,98345,1],'Structure':['pear','also pear','perchance a pear']}) #dataframe

print(df.head()) #shows a graph
print(df.shape) #shows the dimensions of the graph
print(df['Name']) #shows one aspect of a database
print(df['Age'].max()) #shows the maximum value of a database
print(type(df['Age'])) #shows what the type of data is stored in the dataframe/database
print(df['Age'].shape) #prints the shape the database is
print(df.info()) #gives a typical summary of the data
print(df.describe()) #gives the important calculations on the numerical columns
