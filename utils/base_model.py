#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import sys
import pandas as pd
import scipy as stats
import statsmodels.api as sm
from scipy import stats
# from statsmodels.formula.api import logit
# from sklearn.preprocessing import MinMaxScaler, StandardScaler
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import confusion_matrix, accuracy_score,classification_report

# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split

__version__ = '1.0.0'

logger = logging.getLogger('__name__')
logger.setLevel(logging.INFO)
# logger.addHandler(logging.StreamHandler(sys.stdout))


class BaseModelLogit:
    def __init__(self,X,Y) -> None:
        self.X = X
        self.Y = Y
        self.model_fit = None
        self.summary_results = None
        self.cm_df = None
        # logger.info('xx:{}'.format(self.X))
        self.X = self.X.apply(self.__minmaxscale_tranformation,axis=0)
        #add intercept
        self.X = sm.add_constant(self.X)
        # logger.info('tt:{}'.format(self.X))
        

    def __minmaxscale_tranformation(self,lst):
        """ Scale between 0 - 1 
        Note: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html
        """
        # scaler = MinMaxScaler()
        # model = scaler.fit(self.X)
        # self.X = model.transform(self.X)
        X_manual_scaled = (lst - lst.min()) / (lst.max() - lst.min())
        return X_manual_scaled
    
    def __standardscale_tranformation(self):
        """ """
        return
    
    
    def logit_summary(self):
        """ """
        self.model_fit = sm.Logit(self.Y, self.X).fit()
        res = self.model_fit.summary()
        #covert to dataframe
        self.summary_results = pd.DataFrame(res.tables[1].data)
        return self.summary_results 
    
    
    def confusion_matrix(self):
        """ """
        self.cm_df = pd.DataFrame(self.model_fit.pred_table(threshold=0.5))
        self.cm_df.columns = ['Predicted 0', 'Predicted 1']
        self.cm_df = self.cm_df.rename(index ={0: 'Actual 0', 1: 'Actual 1'})
        # logger.info('{}'.format(self.cm_df))

        return self.cm_df


if __name__ == '__main__':
   logger.info('base_model:{}'.format())