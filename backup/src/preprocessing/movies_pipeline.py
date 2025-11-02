def remove_columns(df):
    #Remove the columns with no values in it
    for column in df.columns:
        if len(df[column].value_counts()) == 0:
            df.drop(column, axis=1, inplace = True)
    return df

def check_duplicates(df):
    #check if the same movie appears twice
    indexes = df[df.duplicated()].index
    df.drop(indexes, inplace = True)
    return df

def drop_irrelevant_columns(df):
    #Drop the "video_release_date" column (no value in it)
    df.drop('video_release_date', axis=1, inplace = True)
    return df

def timestamp_modification(df):
    #Create 3 date columns from the timestamp column
    import pandas as pd
    df['release_date'] = pd.to_datetime(df['release_date'])
    df['release_date_year']=df['release_date'].dt.year
    df['release_date_month']=df['release_date'].dt.month
    return df

def title_modification(df):
    #change the title column to lowercase letters
    df['title']=df['title'].str.lower()
    #remove the year from the title name
    df['title'] = df['title'].str.replace(r'\s*\(\d{4}\)$', '', regex=True)
    return df
