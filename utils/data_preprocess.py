#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import sys
import pandas as pd
import numpy as np
import os
from collections import Counter

__version__ = '1.0.0'

logger = logging.getLogger('__name__')
logger.setLevel(logging.INFO)
# logger.addHandler(logging.StreamHandler(sys.stdout))

class DataPreprocess:
    """ Wrapper class for generation basic summary stats """
    def __init__(self, tbl) -> None:
        self.tbl = tbl
    

    @classmethod
    def __cal_mode(cls, sample_lst) -> int:
        """ """
        c = Counter(sample_lst)
        m = [k for k, v in c.items() if v == c.most_common(1)[0][1]]
        return m.pop()

    @classmethod
    def __cal_skewness(cls, sample_lst) -> bool:
        """ skewness = 3*(mean - median)/std
        The acceptable value of skewness is considered to be between -3 and +3
        """
        sk = 3*(np.mean(sample_lst) - np.median(sample_lst))/np.std(sample_lst)
        val = False if sk > -3 and sk < 3 else True
        return val

    @classmethod    
    def get_tbl_description(cls, tbl):
        """ Wrapper function to provide summary stat
        Median/Mode added for checking skweness.
        Mean ~ Median ~ Mode (Normal distribution)
        Mode > Median > Mean (left-skewed data)
        Mean > Median > Mode (right-skewed data) 
        Args: dataframe
        return: dataframe
        raises: None.
         
        """
        try:
            des = tbl.describe()
            #add cv
            des.loc['cv'] = des.loc['std'] / des.loc['mean']
            #add median
            des.loc['median'] = des.apply(np.median, axis=0)
            #add mode
            des.loc['mode'] = des.apply(cls.__cal_mode,axis=0)
            #add skewness
            des.loc['skewed'] = des.apply(cls.__cal_skewness, axis=0)

            des = des.T #Transpose
            logger.info('{}'.format(des.head()))
            des = des[['count','mean','median','mode','std','cv','min','25%','50%','75%','max','skewed']]
            
        except Exception as e:
            exec_type, _, _ = sys.exc_info()
            msg = '{}: {}'.format(exec_type.__name__, str(e))
            logger.exception(msg)
            logger.info('Please call get_tbl_describtion using panda dataframe')
            sys.exit(1)
            
        return des
    