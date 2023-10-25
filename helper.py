import os
import pandas as pd


def get_dataframe(dir_path):
    '''
        dir_path = path to directory
        This function return dataframe
    '''
    files = [filename for filename in os.listdir(dir_path)]
    
    data = {'path' : files}
    
    df = pd.DataFrame(data) # creating dataframe

    #separating features

    temp = []
    for x in df['path']:
        temp.append(x.split('_'))
    
    
    temp = pd.DataFrame(temp)
    
    columns = ['age','gender','race','date']
    
    temp.columns = columns

    df = pd.concat([temp,df],axis = 1)

    df = df.drop(['date'],axis =1) #unnecessary feature
    
    return df
    
