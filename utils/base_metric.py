#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import sys
import pandas as pd
import numpy as np
import scipy as stats
import statsmodels.api as sm
from scipy import stats

__version__ = '1.0.0'

logger = logging.getLogger('__name__')
logger.setLevel(logging.INFO)


class BaseMetric:

    def __init__(self) -> None:
        self.entropy = None
        self.gini_impurity = None
        return

    def __confusion_matrix(self):
        return

    def __entropy(self, p) -> float:
        self.entropy = -1*sum(self.p*np.log(self.p))
        return self.entropy

    def __gini_index(self, p) -> float:
        self.gini_impurity = sum(self.p(1-self.p))
        return self.gini_impurity
