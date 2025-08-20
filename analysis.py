def time_diff(dataframe):
    """Orders the DF values by 'visit_id' and 'date_time' (inplace). Then groups by 'visit_id' and applies
    .diff() on column 'date_time'. Stores the values in a new column 'time_diff'.\n
    Returns the updated dataframe"""

    ## This will be useful for analysing the average duration users spend on each step.

    dataframe.sort_values(by=['visit_id', 'date_time'], ignore_index=True, inplace=True)
    dataframe['time_diff'] = dataframe.groupby('visit_id')['date_time'].diff().dt.total_seconds()
    return dataframe

def step_diff(dataframe):
    """Modifies the categorical column 'process_step' to int values. Then groups by 'visit_id' and applies
    .diff() on column 'process_step'. Stores the values in new columns 'step_diff' and 'step_cum_sum'.\n
    Returns the updated dataframe"""

    ## This will be useful for analysing if there's a step where users go back to a previous step, it may 
    ## indicate confusion or an error.

    dataframe['process_step'].replace({
        'start':0,
        'step_1':1,
        'step_2':2,
        'step_3':3,
        'confirm':4
    }, inplace=True)

    dataframe['step_diff'] = dataframe.groupby('visit_id')['process_step'].diff()
    dataframe['step_cum_sum'] = dataframe.groupby('visit_id')['step_diff'].cumsum()
    return dataframe