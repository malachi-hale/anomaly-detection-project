import pandas as pd

from sklearn.impute import SimpleImputer


def handle_missing_values(df, prop_required_column = .5, prop_required_row = .75):
    '''
    We will eliminate all columns with less than 50% non-null, and all rows with less than 75% non-null.
    '''
    threshold = int(round(prop_required_column*len(df.index),0))
    df.dropna(axis=1, thresh=threshold, inplace=True)
    threshold = int(round(prop_required_row*len(df.columns),0))
    df.dropna(axis=0, thresh=threshold, inplace=True)
    return df

def impute_null_values(df):
    '''
    We will use SimpleImputer to impute the mean value into the null values into each column.
    '''
    #We will use the mean imputer function.
    imputer = SimpleImputer(strategy='most_frequent')

    #We will create a for loop that will impute all the null values in each one of our columns.
    for col in df.columns:
        df[[col]] = imputer.fit_transform(df[[col]])
    
    return df


def to_datetime(df):
    '''
    This function converts all our time values to dateime format, as well as resets
    our index with the date and time the information was accessed.
    '''
    #Create column with date and time of day
    df['Time'] = pd.to_datetime(df['date'] + ' ' + df['time'])

    #Reset Index
    df = df.set_index("Time")

    ##Set the other columns to datetime
    df.start_date = pd.to_datetime(df.start_date)

    df.end_date = pd.to_datetime(df.end_date)

    df.created_at = pd.to_datetime(df.created_at)

    df.updated_at = pd.to_datetime(df.updated_at)

    return df

def prepare_data(df):
    '''
    This function calls our previous three functions to clean our data.
    '''
    #Handle missing values
    df = handle_missing_values(df)

    #Impute Null values
    df  = impute_null_values(df)

    #Reset Index and change columns to datetime
    df = to_datetime(df)

    return df
