# -*- coding: utf-8 -*-

''' Example'''

from readFromH5 import DataHolderGen

''' Create the new data holder'''
data_gen = DataHolderGen('valid.h5',batch_size=100,max_epochs=5)

''' Iterate and show the first element of the batch (just to show that it's different
in every iteration'''
it = 0
for x,y in data_gen:
    print('it =', it)
    print('x.shape =', x.shape)
    print('x[0,...] =', x[0,...])
    print('y.shape =', y.shape)
    print('y[0,...] =', y[0,...])
    it += 1