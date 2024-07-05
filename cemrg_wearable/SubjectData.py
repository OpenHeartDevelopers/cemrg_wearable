import os 
import pandas as pd
import datetime 
import dateutil

import matplotlib.pyplot as plt
import seaborn as sns

import cemrg_wearable.common as common 
KEYS = common.get_data_keys()

class SubjectData:
    def __init__(self, data_path: str, data_date:str, casenum: str, data_key:str):
        self.data_path = data_path
        self.data_date = data_date
        self.casenum = casenum
        self.data_key = data_key
        self._path2files = ''
        self._case_df = None


    def get_data(self) -> pd.DataFrame:
        files_dict = common.get_name(self.data_path, 'cemrghealthy', self.data_date)
        self._path2files = files_dict['path']
