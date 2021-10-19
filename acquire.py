#Disable warnings
import warnings
warnings.filterwarnings("ignore")

#Libraries for processing data
import pandas as pd

#Libraries for obtaining data from SQL databse
import env
import os

#First we establish a connection to the SQL server
def get_connection(db, user=env.user, host=env.host, password=env.password):
    '''
     We establish a connection to the SQL database, using my information stored in the env file.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


def get_cohort_data():
    '''
    We will run a SQL query that obtains data for the logs and the
    corresponding data for every user.
    '''

    #Establish file name
    filename = "logs.csv"
    
    #SQL query 
    sql = ''' 
    SELECT * 
    FROM logs
    LEFT JOIN cohorts ON logs.cohort_id=cohorts.id;
    '''

    #If file exists, return fi;e
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        #Read SQL query
        df = pd.read_sql(sql, get_connection('curriculum_logs'))
        #eliminate duplicate columns
        df = df.loc[:,~df.columns.duplicated()]
        return df
    return df