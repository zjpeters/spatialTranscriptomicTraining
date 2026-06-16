#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 09:58:19 2026

@author: zjpeters
"""
import os
import numpy as np
from matplotlib import pyplot as plt

dataLocation = os.path.join(os.sep,'media','zjpeters','Expansion','trainingST')

myList = ['cherry', 'apple', 'banana']

bananaIdx = myList.index('banana')
print(myList[-1])

myList.append('strawberry')
print(myList[-1])
