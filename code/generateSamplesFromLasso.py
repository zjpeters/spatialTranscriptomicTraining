#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 09:28:15 2026

@author: zjpeters
"""
import os
import pandas as pd
import sys
sys.path.insert(0, "/home/zjpeters/Documents/stanly/code")
import stanly
sourcedata = os.path.join('/','media','zjpeters','Expansion','sorXeniumJyoti','sourcedata')
rawdata = os.path.join('/','media','zjpeters','Expansion', 'trainingST','rawdata')

#%% import sample info from participants.tsv

participants = pd.read_csv(os.path.join('/','media','zjpeters','Expansion','sorXeniumJyoti', 'rawdata', 'participants.tsv'), delimiter='\t')
#%% import original sample

sample = stanly.importXeniumData(os.path.join(sourcedata, 'sample-01'))
processedSample = stanly.processXeniumData(sample, 0, rawdata)
del(sample)
#%% use lasso tool

sampleIdx = 0
lasso = stanly.SelectUsingLasso(processedSample, f"{participants['participant_id'][sampleIdx]}", rawdata)
lasso.applyLasso()
lassoSample = lasso.outputMaskedSample(processedSample)
