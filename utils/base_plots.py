#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import sys
__version__ = '1.0.0'

logger = logging.getLogger('__name__')
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))

class DataPlot:

    def __init__(self) -> None:
        pass