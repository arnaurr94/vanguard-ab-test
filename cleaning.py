import pandas as pd

def clean_web_duplicates(web_data_df):
    return web_data_df.drop_duplicates(
            subset=['client_id','visitor_id','visit_id','process_step','date_time'])

def clean_web_session_duplicates(web_data_df):
    return web_data_df.drop_duplicates(
            subset=['client_id','visitor_id','visit_id','process_step'],
            keep='last')

def normalize_column_names(df):
    """
    Return a new DataFrame whose column names are all lowercase,
    have no surrounding whitespace, and use underscores instead of spaces.
    """
    # Make a copy to avoid modifying the original DataFrame (optional)
    df = df.copy()
    
    # Generate normalized names
    normalized_cols = (
        df.columns
          .str.lower()                   # lowercase
          .str.strip()                   # remove leading/trailing spaces
          .str.replace(' ', '_')  # spaces → underscores
    )
    
    # Assign and return
    df.columns = normalized_cols
    return df

def drop_not_participating_clients(clients_df):
    return clients_df.dropna(subset=['variation'])

def drop_null_clients(demo_df):
    # Count nulls in each row, then keep rows with ≤1 null
    mask = demo_df.isnull().sum(axis=1) <= 1
    return demo_df[mask]

def convert_client_age_to_int(demo_df):
    copy_of_demo_df = demo_df.copy()
    copy_of_demo_df['clnt_age'] = copy_of_demo_df['clnt_age'].round(0).astype('Int64')
    return copy_of_demo_df

def convert_datetime_to_date_time(web_data_df):
    web_data_df['date_time'] = web_data_df['date_time'].astype('datetime64[s]')
    return web_data_df

# renaming the colums
def rename_demo_columns(df):

    new_names = {
        'clnt_tenure_yr': 'tenure_yr',
        'clnt_tenure_mnth': 'tenure_months',
        'clnt_age': 'age',
        'gendr': 'gender',
        'num_accts': 'num_accounts',
        'bal': 'balance',
        'calls_6_mnth': 'calls_6_months',
        'logons_6_mnth': 'logins_6_months'
    }
    return df.rename(columns=new_names)


def test_outliers(data):
    """
    Return a Series whose index correspond to the rows deemed outliers of the input DatFrame. 
    """ 
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    lower_boundary = Q1 - (IQR * 1.5)
    higher_boundary = Q3 + (IQR * 1.5)
    outliers = data[(data<lower_boundary) | (data>higher_boundary)]
    return outliers

def drop_outliers(data, column):
    """
    Returns an updated Dataframe with no outliers (found through test_outliers). 
    """ 
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)
    IQR = Q3 - Q1
    lower_boundary = Q1 - (IQR * 1.5)
    higher_boundary = Q3 + (IQR * 1.5)
    outliers = column[(column<lower_boundary) | (column>higher_boundary)]
    return data.drop(labels=outliers.index)
