#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import sys
import seaborn as sns
import matplotlib.pyplot as plt

__version__ = '1.0.0'

logger = logging.getLogger('__name__')
logger.setLevel(logging.INFO)
# logger.addHandler(logging.StreamHandler(sys.stdout))

class BasePlot:
    """Wrapper class for basic plotting """
    def __init__(self, tbl,outfile) -> None:
        self.tbl = tbl
        self.outfile = outfile
        

    @staticmethod
    def corrplot(tbl,outfile):
        """ Pairwise correlation plot for predictor variable """
        heatmap = sns.heatmap(tbl.corr(), 
                              vmin=-1, 
                              vmax=1, 
                              annot=True, 
                              cmap='BrBG')
        heatmap.set_title('Correlation Heatmap', 
                          fontdict={'fontsize':18}, 
                          pad=12
                          )
        plt.savefig(outfile, dpi=300, bbox_inches='tight')
        return
    
    # @staticmethod
    # def 