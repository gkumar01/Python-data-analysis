#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import sys
import pandas as pd

# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split

__version__ = '1.0.0'

logger = logging.getLogger('__name__')
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))


class Models:

    def __init__(self) -> None:
        pass

if __name__ == '__main__':
   logger.info('base_model:{}'.format())