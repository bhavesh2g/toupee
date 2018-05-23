# -*- coding: utf-8 -*-
"""
Created on Wed May 23 12:18:12 2018

This file will convert the existing training, test or validation sets (.npz)
into an h5 file that can be read by an instance of the DataHolderGen object

@author: Carlos Ledezma
"""

import h5py
import numpy as np

fname = 'valid.npz'
h5name = fname[:-4] + '.h5'
f = h5py.File(h5name,'w')
data = np.load(fname)

dsetX = f.create_dataset('x',data=data['x'])
dsetY = f.create_dataset('y',data=data['y'])


f.close()
