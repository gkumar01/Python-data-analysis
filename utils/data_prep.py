#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import json
import os
import sys
import pandas as pd


__version__ = '1.0.0'

logger = logging.getLogger('__name__')
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))

class DataExtractor:
    """ Wrapper for tsv/csv/xls/json file data
    DataExtractor class provides a wraper for pandas dataframe
    """
    def __init__(self,filename:str) -> None:
        """ Intialize a data file for reading
        Arguments:
            filename: The path to the data file.
        """
        self.filename = filename
        self.__check_file_exists()
        self.df = self.__switch()

        return

    def __check_file_exists(self):
        """ check if file exist in the path,
          otherwise raise error 
        """
          # check if file exsist:
        try:
            os.path.isfile(self.filename)
        except Exception as e:
            exec_type, _, _ = sys.exc_info()
            msg = '{}: {}'.format(exec_type.__name__, str(e))
            logger.exception(msg)
            sys.exit(1)
        logger.info('Filename:{}'.format(self.filename))
        return

    def __csv_file(self):
        """ read csv file as dataframe """
        df = pd.read_table(self.filename,
                    delimiter = ",",
                    index_col = False, #first column not as row index
                    header = 0,
                    comment = '#'
        )
        return df
        
    def __tsv_file(self):
        """ read tsv file as dataframe """
        df = pd.read_table(self.filename,
                    delimiter = "\t",
                    index_col = False, #first column not as row index
                    header = 0,
                    comment = '#'
        )
        return df
    
    def __xls_file(self):
        """read xls file as dataframe """
        df = pd.read_excel(self.filename, 
                    engine="xlrd",
                    index_col = False, #first column not as row index
                )
        return df
    
    def __json_file(self):
        """ load json parameter file """
        data = None
        with open(self.filename, '+r') as fl:
            data = json.load(fl)
        return data
    
    def get_data(self):
        """ return data frame """
        return self.df
    
    def __switch(self):
        """ Wraper to check file extension to call file
        specific function to load data as dataframe 
        """
        df = None

        if self.filename.endswith('.csv'):
            df = self.__csv_file()
        elif self.filename.endswith('.tsv'):
            df = self.__tsv_file()
        elif self.filename.endswith('.xls'):
            df = self.__xls_file()
        elif self.filename.endswith('.json'):
            df = self.__json_file()

        
        if df is None:
            msg = 'data file extension not supported'
            logger.info(' :{}'.format(msg))    
            sys.exit(1)

        return df
    
    
    
class ParameterExtractor(DataExtractor):
    """Wraper specific to read parameter file """
    def __init__(self, paramfile) -> None:
        super().__init__(paramfile)
        return
    
    def get_parameter(self):
        """Load json parameter file 
        returns:
            dictionary
        """
        parameter = DataExtractor.get_data(self)
        return parameter 
         

class CreateOutput_label:
    """Wraper class to extract lable from data filename """
    def __init__(self) -> None:
        return    
    
    @staticmethod
    def get_lable(filename):
        # logger.info('Test:{}'.format(filename))
        flname = os.path.split(filename)
        lable = flname[-1].split(".")
        # logger.info('Test:{}'.format(lable[0]))
        return lable[0]

if __name__ == '__main__':
    logger.info('data_prep.DataExtractor {}'.format(DataExtractor()))