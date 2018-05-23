# -*- coding: utf-8 -*-
"""
Created on Wed May 23 13:01:24 2018

Data holder generator class that can be used with fit_generator. The instance
generates random batches from the datasets contained in the h5 files. Since
only one batch is read and returned at a time, the whole dataset doesn't need 
to be loaded onto memory.

@author: Carlos Ledezma
"""
import numpy as np
import h5py
from random import sample

''' Data holder generator class'''
class DataHolderGen:
    def __init__(self,fname,batch_size,max_epochs):
        self.file = h5py.File(fname,'r') # Open the h5 file
        self.data_x = self.file['x'] # Read x data
        self.data_y = self.file['y'] # Read training data
        self.num_examples = self.data_y.shape[0] # Number of examples in the dataset
        self.batch_size = batch_size # Batch size to yield in every iteration
        self.index = max_epochs # Maximum number of epochs allowed by the instance
       
    # Generator structure requires the __iter__ and a __next__ methods
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0: # When the max number of iterations inform the loop
            raise StopIteration
        self.index -= 1 
        
        # Create a list of non-repeated random numbers in the range [0,num_examples] of the size of the desired batch
        batch = sample(range(self.num_examples),self.batch_size)
        batch.sort()
        
        # Return the arrays in the shape that fit_gen uses (data, target)
        return (self.data_x[batch,...],
                self.data_y[batch,...])
        
    # Close file when object is deleted    
    def __del__(self):
        # In case the generator is used less than max_epocohs
        self.file.close()

''' Example'''

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