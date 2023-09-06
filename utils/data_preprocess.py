#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import sys
import pandas as pd
import os

__version__ = '1.0.0'

logger = logging.getLogger('__name__')
logger.setLevel(logging.INFO)
# logger.addHandler(logging.StreamHandler(sys.stdout))

class DataPreprocess:
    """ Wrapper class for generation basic summary stats """
    def __init__(self, tbl) -> None:
        self.tbl = tbl


    @classmethod    
    def get_tbl_description(cls, tbl):
        """ Wrapper function to provide summary stat
        Args: dataframe
        return: dataframe
        raises: None. 
        """
        try:
            des = tbl.describe()
            #add cv
            des.loc['cv'] = des.loc['std'] / des.loc['mean']
            
        except Exception as e:
            exec_type, _, _ = sys.exc_info()
            msg = '{}: {}'.format(exec_type.__name__, str(e))
            logger.exception(msg)
            logger.info('Please call get_tbl_describtion using panda dataframe')
            sys.exit(1)
            
        return des
    