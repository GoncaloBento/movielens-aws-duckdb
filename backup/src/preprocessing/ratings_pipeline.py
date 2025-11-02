def remove_columns(df):
    #Remove the columns with no values in it
    for column in df.columns:
        if len(df[column].value_counts()) == 0:
            df.drop(column, axis=1, inplace = True)
    return df

def check_ratings(df):
    #check if the ratings are falling in between 1 and 5
    indexes = df[(df['ratings'] < 1) | (df['ratings'] > 5)].index
    df.drop(indexes,inplace=True)
    return df

def check_duplicates(df):
    #check if the same user don't evaluate the same movie twice
    for unique_user in df['userId'].unique():
        user_ratings = df[df['userId'] == unique_user]
        indexes = user_ratings[user_ratings['movieId'].duplicated()].index
        df.drop(indexes, inplace = True)
    return df

def timestamp_modification(df):
    #change the data type of the column rating_date and create two columns from the rating_date with the specific year and month --> easier to query
    df['rating_date'] = pd.to_datetime(df['timestamp'], unit='s')
    df['rating_year'] = df['rating_date'].dt.year
    df['rating_month'] = df['rating_date'].dt.month
    return df

