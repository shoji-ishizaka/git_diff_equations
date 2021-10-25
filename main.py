'''
Created on 2021/10/25

@author: shoji
'''

import matplotlib.pyplot as plt
import numpy as np
import def_differential_equations as def_equ
                             
CalcuFunc = def_equ.Calcu_Func()                                # Instance of calculating simultaneous differential equations by Runge-Kutta method

time_start = CalcuFunc.get_time_start()                         # First day
time_end = CalcuFunc.get_time_end()                             # End day
number_of_culculation = CalcuFunc.get_number_of_cuculation()    # Number of calculations
time_increment = CalcuFunc.get_increment()                      # Time interval

TList = []                                                      # Time data for plotting
SList = []                                                      # Number of uninfected individuals for plotting
IList = []                                                      # Number of infected individuals for plotting
RList = []                                                      # Number of recovered individuals for plotting

time = time_start
X = np.array( CalcuFunc.get_init_values_list())                 # List of initial values.
for i in range( 1, number_of_culculation + 1):                  # Solve the equation.
    X = X + CalcuFunc.Dev( X)
    
    ''' plotting'''
    TList.append( time)
    SList.append( X[0])
    IList.append( X[1])
    RList.append( X[2])
    time = time + time_increment

''' plotting'''
plt.plot( TList, SList)                                         # Plotting number of uninfected individuals vs day.
plt.plot( TList, IList)                                         # Plotting number of infected individuals vs day.
plt.plot( TList, RList)                                         # Plotting number of recovered individuals vs day.
plt.show()

if __name__ == '__main__':
    pass
