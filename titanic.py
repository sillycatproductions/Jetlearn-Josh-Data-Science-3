import pandas as pd

data = pd.read_csv('titanic.csv') #loading data from a local csv file
print(data.head(50)) #number in brackets = number of info it will display
print(data.info())

naa = data[['Name','Age']] #stores certain databases in a dataframe
print(naa.head(1))
print(naa.shape)

above50 = data[data['Age'] > 50] #conditional result that only displays certain values that follow a condition (in this case it is anyone who is above 50 years of age)
print(above50.head(10))
print(above50.shape)

class1 = data[data['Pclass'].isin([1])] #isin means if a value = to the number (in this case if there are any Pclass passengers in first class)
print(class1.head(10))

print(class1[['Name', 'Pclass']].head()) #shows specific data in the conditional value (in this case name and pclass)

c2a3 = data[(data['Pclass'] == 2) | (data['Pclass'] == 3)] #the straight line (|)  = or (in this case if pclass is 2 | 3 means if pclass is 2 or 3)
print(c2a3.head(10))