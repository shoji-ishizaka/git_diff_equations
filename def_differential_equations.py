'''
Created on 2021/10/25

@author: shoji
'''
import numpy as np
import analize_xml as axm

class Calcu_Func:
    h1List = np.array([])
    h2List = np.array([])
    h3List = np.array([])

    time_start = 0.0                                                            # Start day
    time_end = 0.0                                                              # End day
    number_of_cuculation = 0                                                    # Number of calculations
    time_increment = 0.0
    
    init_values_list = []
    function_list = []

    def __init__( self):
        axm.make_expression()
        
        self.time_start = axm.time_start
        self.time_end = axm.time_end                                            # Days
        self.number_of_cuculation = axm.number_of_cuculation                    # Number of calculations
        self.time_increment = ( self.time_end - self.time_start) / self.number_of_cuculation
        self.init_values_list = axm.init_values_list
        
        for formula in axm.formula_list:                                        # making the function from string.
            self.function_list.append( eval( formula))
            
    def get_time_start(self):
        return self.time_start
    
    def get_time_end(self):
        return self.time_end   
    
    def get_number_of_cuculation(self):
        return self.number_of_cuculation  

    def get_increment(self):
        return self.time_increment

    def get_init_values_list(self):
        return self.init_values_list
    
    def get_function_list(self):
        return self.function_list
    
    def Dev1( self, sir):
        hList = np.array([])
        for function in self.function_list:
            hList = np.append( hList, function( sir))
        self.h1List = hList
        return self.time_increment * hList

    def Dev2( self, sir):
        hList = np.array([])
        for function in self.function_list:
            hList = np.append( hList, function( sir + 0.5 * self.h1List))
        self.h2List = hList
        return self.time_increment * hList

    def Dev3( self, sir,):
        hList = np.array([])
        for function in self.function_list:
            hList = np.append( hList, function( sir + 0.5 * self.h2List))
        self.h3List = hList
        return self.time_increment * hList

    def Dev4( self, sir):
        hList = np.array([])
        for function in self.function_list:
            hList = np.append( hList, function( sir + 0.5 * self.h3List))
        return self.time_increment * hList

    def Dev( self, sir):
        d1 = self.Dev1( sir)
        d2 = self.Dev2( sir)
        d3 = self.Dev3( sir)
        d4 = self.Dev4( sir)
        
        return ( d1 + 2 * d2 + 2 * d3 + d4) / 6
