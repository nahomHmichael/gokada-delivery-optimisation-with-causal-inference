import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import logging
import numpy as np
import math as m

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
        

    
    