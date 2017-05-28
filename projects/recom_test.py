import pandas as import pd

table  = pd.read_csv('movie_path')
# for summarizing the table
rating_df = pd.pivot_table(table , index = 'user_id' , columns = 'movie_id' , aggfunction = np.max)
