# STUDENT NUMBER -740090003

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_HRV_metrics(file_in):
    
    df = pd.read_csv(file_in)
    df['time_next'] = df['time'].shift(-1)
    df['type_next'] = df['type'].shift(-1)
    df['rr'] = df['time_next'] - df['time']
    df['rr_type'] =  df['type'] + df['type_next']
    df['rr_next'] = df['rr'].shift(-1)
    df['rr_next_type'] = df['rr_type'].shift(-1)
    df['diff'] = df['rr_next'] - df['rr']
    df['diff_squared'] = df['diff']**2
    df_NN_intervals= df.query("rr_type == 'NN'")
    n = len(df_NN_intervals)
    
    df_NN_ToNN_intervals = df_NN_intervals.query(" rr_next_type== 'NN'")
    if df_NN_intervals['rr'].count() < 500:
        mean_nn = None
        sd_nn = None
        mean_bpm = None
    else:
        mean_nn = df_NN_intervals['rr'].mean()
        sd_nn = df_NN_intervals['rr'].std()
        mean_bpm = 60*1000/mean_nn
     
    if df_NN_ToNN_intervals['diff'].count() < 500:
        RMSSD = None
        pNN20 = None
        pNN50 = None
    else:
        RMSSD = df_NN_ToNN_intervals['diff_squared'].mean() ** 0.5
        total = df_NN_ToNN_intervals['diff'].count()
        k = len( df_NN_ToNN_intervals.query("diff>20 or diff<-20") )
        pNN20 = (k/total)*100
        l = len( df_NN_ToNN_intervals.query("diff>50 or diff<-50") )
        pNN50 = (l/total)*100
    results = {
        'file': os.path.basename(file_in), # returns the file name from the path directory
        'n': n,
        'mean_nn': round(mean_nn),
        'mean_bpm':round(mean_bpm,1),
        'sd_nn': round(sd_nn,1),
        'RMSSD': round(RMSSD,1),
        'pNN20': round(pNN20,1),
        'pNN50': round(pNN50,1),        
    }   

    return results

def process_HRV_files(file_list_in, file_out):
    task_data = []
     #catch the error and print a statement about the missing file
    for file in file_list_in:
        try:
            task_data.append(calculate_HRV_metrics(file))
        except FileNotFoundError as error:            
            print("{}.The file {} cannot be found !!!".format(error,file))
            
    df = pd.DataFrame(task_data)            #saving the results into a dataframe
    df.to_csv(file_out, index = False)      #store the result in a csv format
    
    return file_out
    
    