import os
import tarfile
import urllib.request
import numpy as np
import pandas as pd

# TODO: Create constants
#DOWNLOAD_ROOT_URL = 'https://raw.githubusercontent.com/ageron/handson-ml2/master/'
#FILE_PATH_TO_DATA = os.path.join('datasets', 'housing')
#FULL_FILE_URL = f'{DOWNLOAD_ROOT_URL}datasets/housing/housing.tgz'

# TODO: Create class 
class Fades:
    def __init__(self, data_url, file_path):
        ''' Fetch Any Data, Extract, Store '''
        
        self.data_url = data_url
        self.file_path = file_path

    # TODO: Create method to get data and extract
    def fetch_data(self):
        ''' Method downloads a single compressed file from a given url 
        and extracts it into a given file path. '''
        
        data_url = self.data_url 
        file_path = self.file_path
        
        os.makedirs(file_path, exist_ok=True)
        tgz_path = os.path.join(file_path, 'housing.tgz')
        urllib.request.urlretrieve(data_url, tgz_path)
        data_tgz = tarfile.open(tgz_path)
        data_tgz.extractall(path=file_path)
        data_tgz.close()
            
        
    # TODO: Create method to convert data to DataFrame
    def convert_csv_to_df(self):
        ''' Converts extracted csv data to Data Frame object. '''
        
        # TODO: Add try/except
        csv_path = os.path.join(self.file_path, 'housing.csv')
        return pd.read_csv(csv_path)
    
    def split_train_test(self, data, split_ratio):
        ''' Splits given data into testing and training sets. 
        Returns training sets, testing sets respectively.'''
        shuffled_indices = np.random.permutation(len(data))
        test_set_size = int(len(data) * split_ratio)
        test_indices = shuffled_indices[:test_set_size]
        train_indices = shuffled_indices[test_set_size:]
        return data.iloc[train_indices], data.iloc[test_indices]
    
#fetch_it = Fades(data_url=FULL_FILE_URL, file_path=FILE_PATH_TO_DATA)
#fetch_it.fetch_data()
#fetch_it.convert_csv_to_df()