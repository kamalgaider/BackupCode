import pandas as pd

# CSV file used for below code contain - movieId :  all(customerId,Rating,Date)
#downloaded from -https://www.kaggle.com/laowingkin/netflix-movie-recommendation/data
dataframe1 = pd.read_csv('combined_data_1.txt', header = None, names = ['Cust_Id', 'Rating'], usecols = [0,1])
dataframe1['Rating'] = dataframe1['Rating'].astype(float)
print('Dataset shape(row,column): {}\n'.format(dataframe1.shape))

'''iloc is used to slice the dataframe- 
Syntax--> datafm.iloc[row,column] --> returns rows containing index & data'''
print('Dataset examples-\n')
print(dataframe1.iloc[::1500000, :])