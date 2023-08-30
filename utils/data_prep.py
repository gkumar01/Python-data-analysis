#!/usr/bin/python 3
# -*- coding: utf-8 -*-

import logging
import os
import sys
import pandas as pd


__version__ = '1.0.0'

logger = logging.getLogger('__name__')
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))

class DataExtractor:
    def __init__(self,filename) -> None:
        self.filename = filename

        # check if file exsist:
        try:
            os.path.isfile(self.filename)
        except Exception as e:
            exec_type, _, _ = sys.exc_info()
            msg = '{}: {}'.format(exec_type.__name__, str(e))
            logger.exception(msg)
        logger.info('Filename:{}'.format(self.filename))
        # TODO: implement feteching data from tsv, xls and json
        # 
        self.df = self.__csv_file()
        # self.df = self.__tsv_file()

        return


    def __csv_file(self):
        df = pd.read_table(self.filename,
                    delimiter = ",",
                    index_col = False, #first column not as row index
                    header = 0,
                    comment = '#'
        )
        return df
        
    def __tsv_file(self):
        df = pd.read_table(self.filename,
                    delimiter = "\t",
                    index_col = False, #first column not as row index
                    header = 0,
                    comment = '#'
        )
        return df

    def get_data(self):
        """ """
        return self.df

if __name__ == '__main__':
    logger.info('data_prep.DataExtractor {}'.format(DataExtractor()))