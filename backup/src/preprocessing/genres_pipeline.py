def remove_columns(df):
    #Remove the columns with no values in it
    for column in df.columns:
        if len(df[column].value_counts()) == 0:
            df.drop(column, axis=1, inplace = True)
    return df

def check_duplicates(df):
    #check if the same user appears twice
    indexes = df[df.duplicated()].index
    df.drop(indexes, inplace = True)
    return df
