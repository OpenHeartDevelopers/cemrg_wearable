import os 
import pandas as pd
import datetime 
import dateutil

import matplotlib.pyplot as plt
import seaborn as sns

def get_subject_dataset(filein, subject, timestr, ycol, remove_zero=True) : 
    df=pd.read_csv(filein)
    return get_subject_dataset_from_df(df, subject, timestr, ycol, remove_zero)

def get_subject_dataset_from_df(df, subject, timestr, ycol, remove_zero=True) :
    casedf=df[df['SUBJECT CODE']==subject]
    
    if subject not in df['SUBJECT CODE'].values:
        print(f"DataFrame does not contain entry with subject code {subject}")
        return 0
    
    if remove_zero: 
        casedf=casedf[casedf[ycol]!=0]

    casedf['timestamp'] = pd.to_datetime(casedf[timestr].str[:-15], format='mixed', utc=True, dayfirst=True)
    
    # Find the minimum date in the 'timestamp' column
    min_date = casedf['timestamp'].min()
    max_date = casedf['timestamp'].max()
    # Calculate the time difference in hours between each datetime and the minimum date
    casedf['hours'] = (casedf['timestamp'] - min_date).dt.total_seconds() / 3600
    
    casedf['days'] = (casedf['timestamp'] - min_date).dt.total_seconds() / (3600*24)
    # Optionally, you can round the hours to integers
    #casedf['hours'] = casedf['hours'].round().astype(int)   

    return casedf


def get_list_of_dates(casedf: pd.DataFrame) : 
    # get number of unique dates in the dataframe
    list_of_dates = [d.split('T')[0] for d in casedf['RECEIVED DATE']]
    
    # convert the list of dates to a set to get unique dates
    unique_dates = set(list_of_dates)
    
    # get the number of unique dates
    num_unique_dates = len(unique_dates)

    return num_unique_dates, unique_dates

def process_atom5_wearable_data(path_to_data, casename, y_data_key): 
    """
    Process Atom5 wearable data.
    
    Parameters:
    - path_to_data (str): The path to the directory containing the wearable data files.
    - casename (str): The name of the case to process.
    - y_data_key (str): The key corresponding to the type of data to extract.
    
    Returns:
    - pd.DataFrame: A DataFrame containing the processed wearable data for the specified case.
    
    This function reads the wearable data files from the specified directory, extracts the data for the specified case, and processes the timestamp information based on the data type provided.
    """
    mypath=os.path.join(path_to_data, 'wearable')
    format='%Y-%m-%dT%H:%M:%SZ'

    y_data_dic = {
        'BEATS PER MIN': 'heartrate_logged',
        'SPO2': 'spo2',
        'TOTALSTEPS': 'steps_logged',
        'LONGITUDE': 'steps_logged',
        'LATITUDE': 'steps_logged'
    }

    timecolname_dic = {
        'BEATS PER MIN': 'TIMESTAMP',
        'SPO2': 'TIMESTAMP',
        'TOTALSTEPS': 'DATA SOURCE',
        'LONGITUDE': 'DATA SOURCE',
        'LATITUDE': 'DATA SOURCE'
    }

    strnum_dic = {
        'BEATS PER MIN': 15,
        'SPO2': 15,
        'TOTALSTEPS': 9,
        'LONGITUDE': 9,
        'LATITUDE': 9
    }

    file_names = os.listdir(mypath)
    common_name = os.path.commonprefix(file_names)
    print(common_name)

    y_data = y_data_dic[y_data_key.upper()]
    timecolname = timecolname_dic[y_data_key.upper()]
    strnum = strnum_dic[y_data_key.upper()]

    file_to_load = f'{common_name}-{y_data}-report.csv'

    df=pd.read_csv(os.join(mypath, file_to_load))

    #display(df['SUBJECT CODE'].unique())
    case_table=df[df['SUBJECT CODE']==casename]

    # Extract the date part of the timestamp and convert to datetime
    case_table['time'] = pd.to_datetime(case_table[timecolname].str[:-strnum], format=format, utc=True)

    return case_table


def get_name(dir: str, prefix: str, some_date:str) -> str: 
    
    mypath = os.path.join(dir, f'{prefix}-data-{some_date}', 'wearable')
    bpm = f'{prefix}-{some_date}-raw-garmin-data-heartrate_logged-report.csv'
    spo2 = f'{prefix}-{some_date}-raw-garmin-data-spo2-report.csv'
    steps = f'{prefix}-{some_date}-raw-garmin-data-steps_logged-report.csv'

    mydic ={
        'path' : mypath,
        'bpm' : bpm,
        'spo2' : spo2,
        'steps' : steps
    }

    return mydic



