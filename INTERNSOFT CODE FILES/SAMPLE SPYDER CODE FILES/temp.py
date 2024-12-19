# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
azmi = pd.read_csv('Apple Stock Price History.csv',usecols=[0,1,2,3,4])


POHL_avg = azmi[['Price','Open','High', 'Low']]. mean(axis = 1)

obs = np.arange (1, len(azmi) +1,1)

plt.plot(obs,POHL_avg, 'b', label = 'MY FIRST PLOT')
