import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import logging
import numpy as np
import math as m
import holidays
from datetime import datetime
class Helper:
    """
    summary: helper class for EDA
    """
    def __init__(self) -> None:
        pass
    
    def get_df_info(self, df):
        
        return (df.describe().T.style.bar(subset=['mean'], color='#205ff2').background_gradient(subset=['std'],
                                                                                                cmap='Reds').background_gradient(subset=['50%'], cmap='coolwarm'))
        
    
  
    def percent_missing(self, df):

        total_cells = m.prod(df.shape)
        missing_count = df.isnull().sum()
        total_missing = missing_count.sum()
        print("Total Percentage of Missing values: " +
                f"{round(((total_missing/total_cells)*100))}" +"% ")
        
    def is_holiday(self,Date):
        ng_holidays = holidays.country_holidays('NG')
        try:
            dt = datetime.strptime(Date, '%Y-%m-%d %H:%M:%S').date()
            if dt in ng_holidays:
                return 1
            else: return 0
        except Exception as e:
             return 0

    
    