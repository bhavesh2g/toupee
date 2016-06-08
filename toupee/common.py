#!/usr/bin/python
"""
Alan Mosca
Department of Computer Science and Information Systems
Birkbeck, University of London

All code released under Apachev2.0 licensing.
"""
__docformat__ = 'restructedtext en'

import numpy
import yaml
import theano
import theano.tensor as T
from data import sharedX

class Toupee:
    
    def __init__(self):
        self.reset()

    def reset(self):
        self.epoch_hooks = []
        self.reset_hooks = []

    def add_epoch_hook(self,hook):
        if hook not in self.epoch_hooks:
            self.epoch_hooks.append(hook)

    def add_reset_hook(self,hook):
        if hook not in self.reset_hooks:
            self.reset_hooks.append(hook)

class Results:

    def __init__(self,params):
        self.train_history = []
        self.validation_history = []
        self.test_history = []
        self.training_costs = []
        self.params = params

    def set_observation(self,train,validation,test,cost):
        self.train_history.append(train)
        self.validation_history.append(validation)
        if test is not None:
            self.test_history.append(test)
        self.training_costs.append(cost)

    def set_final_observation(self,valid,test,epoch):
        self.best_valid = valid
        self.best_test = test
        self.best_epoch = epoch
        self.params = self.params.serialize()

class ConfiguredObject(yaml.YAMLObject):

    def _default_value(self, param_name, value):
        if param_name not in self.__dict__:
            self.__dict__[param_name] = value

def serialize(o):
    if isinstance(o, numpy.float32):
        return float(o)
    else:
        try:
            return numpy.asfarray(o).tolist()
        except:
            if isinstance(o, object):
                if 'serialize' in dir(o) and callable(getattr(o,'serialize')):
                    print o
                    return o.serialize()
                if 'tolist' in dir(o) and callable(getattr(o,'tolist')):
                    return o.tolist()
                try:
                    return json.loads(json.dumps(o.__dict__,default=serialize))
                except:
                    return str(o)
            else:
                raise Exception("don't know how to save {0}".format(type(o)))

if 'toupee_global_instance' not in locals():
    toupee_global_instance = Toupee()
