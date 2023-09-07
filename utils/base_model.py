#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import sys
import pandas as pd
import numpy as np
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
        self.data_summary = None
        self.cm_df = None
        # logger.info('xx:{}'.format(self.X))
        self.X = self.X.apply(self.__minmaxscale_tranformation,axis=0)
        #add intercept
        self.X = sm.add_constant(self.X)
        # logger.info('tt:{}'.format(self.X))
        self.metric = {
            'Accuracy' : None,
            'Precision' : None,
            'Specificity' : None,
            'Recall' : None,
            'F1_score' : None
        }
        

    def __minmaxscale_tranformation(self,lst):
        """ scale variable between 0 to 1. 
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
        """ Wrapper instance function for logit model fit """
        self.model_fit = sm.Logit(self.Y, self.X).fit()
        res = self.model_fit.summary()
        #covert to dataframe
        self.summary_results = pd.DataFrame(res.tables[1].data)


        data_summary = pd.concat([self.model_fit.pvalues[1:].T.to_frame(),
                          self.model_fit.params[1:].T.to_frame()],
                          axis=1
                          )
        
        data_summary.columns = ['Pvalue','Params']
        data_summary.index.name = 'Features'
        data_summary.reset_index()

        data_summary['Odds'] = np.exp(data_summary['Params'])
        data_summary['Percent'] = np.exp(data_summary['Odds'])
        data_summary.sort_values(by=['Odds'], ascending=False).reset_index(drop=True)

        logger.info('xxx{}'.format(data_summary))
        return (self.summary_results,data_summary)
    
    
    def confusion_matrix(self):
        """ Wrapper instance function for classification summary """
        mat = self.model_fit.pred_table(threshold=0.5).astype(int)
        # logger.info('{} : {} : {}'.format(
        #     mat[1][1], mat[ :,1].sum(), mat[1:,].sum())
        #                             )
        self.cm_df = pd.DataFrame(mat)
        self.cm_df.columns = ['Predicted 0', 'Predicted 1']
        self.cm_df = self.cm_df.rename(index ={0: 'Actual 0', 1: 'Actual 1'})
        # logger.info('{}'.format(self.cm_df))
        self.metric['Accuracy'] = round(100 * np.trace(mat)/mat.sum(), 2)
        self.metric['Precision'] = round(100 * mat[1][1]/mat[:,1].sum(), 2)
        self.metric['Specificity'] = round(100 * mat[0][0]/mat[0:,].sum(), 2)
        self.metric['Recall'] = round(100 * mat[1][1]/mat[1:,].sum(), 2)
        self.metric['F1_score'] = \
            round(2*(self.metric['Precision']*self.metric['Recall'])/ \
                  (self.metric['Precision'] + self.metric['Recall']) \
                  ,4)
        
        # logger.info('Metric:{}'.format(self.metric))

        return self.cm_df
    
    def get_metric(self):
        return self.metric


if __name__ == '__main__':
   logger.info('base_model:{}'.format())