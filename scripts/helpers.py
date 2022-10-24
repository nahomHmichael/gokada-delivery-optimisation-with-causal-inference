import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import logging
import numpy as np
import math as m
import holidays
from datetime import datetime
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Normalizer
class Helper:
    """
    summary: helper class for EDA
    """
    def __init__(self) -> None:
        self.ng_holidays = holidays.country_holidays('NG')
    
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
        # ng_holidays = holidays.country_holidays('NG')
        try:
            dt = datetime.strptime(Date, '%Y-%m-%d %H:%M:%S').date()
            if dt in self.ng_holidays:
                return 1
            else: 
                return 0
        except Exception as e:
             return 0
    def isWeekend(self, Date):
        dt = datetime.strptime(Date, '%Y-%m-%d %H:%M:%S')
        if dt.weekday() < 5:
            return 0
        else:  
            return 1
        
    def show_corr(self, df, title, size=[17,10], range=None):
 
        try:
            # correlation matrix
            if range is None:
                corr_matrix = df.corr()
            else:
                if(range[1] == -10):
                    corr_matrix = df.iloc[:,range[0]:].corr()
                else:
                    corr_matrix = df.iloc[:,range[0]:range[1]].corr()
            matrix = np.triu(corr_matrix)
            fig, ax = plt.subplots(figsize=(size[0], size[1]))
            plt.title(title)
            ax = sns.heatmap(corr_matrix, annot=True, mask=matrix)
        except:
                print('not successful')
                
    def label_encoder(self,df,columns=None):
        if columns == None:
            columns = df.select_dtypes(exclude = ['number'])
        le = LabelEncoder()

        for col in columns:
            df[col] = le.fit_transform(df[col])

        return df
    def normalizer(self,df,columns):
    
        nrm = Normalizer()
        df_norm = df.copy(deep=True)
        df_norm[columns] = pd.DataFrame(nrm.fit_transform( df_norm[columns]), columns=columns)
        return df_norm

        
        