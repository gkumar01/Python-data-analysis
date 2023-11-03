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
    def __init__(self, tbl, outfile) -> None:
        self.tbl = tbl
        self.outfile = outfile

    # calling the destructor
    def __del__(self):
        return

    @classmethod
    def corrplot(cls, tbl, outfile):
        """ Pairwise correlation plot for predictor variable """
        plt.figure()
        heatmap = sns.heatmap(tbl.corr(),
                              vmin=-1,
                              vmax=1,
                              annot=True,
                              cmap='BrBG')
        heatmap.set_title('Correlation Heatmap',
                          fontdict={'fontsize': 18},
                          pad=12
                          )
        plt.savefig(outfile, dpi=300, bbox_inches='tight')
        plt.clf()
        return

    @classmethod
    def accuracy_plot(cls, tbl, lable, outfile):
        """ """
        logger.info('{}'.format(tbl))
        plt.figure()
        heatmap = sns.heatmap(tbl,
                              annot=True,
                              cmap='BrBG',
                              fmt='g',  # disable scientific notation
                              cbar=False  # remove side bar
                              )
        heatmap.set_title('Accuracy Score: {}%'.format(lable),
                          fontdict={'fontsize': 20},
                          pad=12
                          )
        plt.savefig(outfile, dpi=300, bbox_inches='tight')
        plt.clf()
        return
