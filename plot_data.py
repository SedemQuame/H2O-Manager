"""A simple program to plot data got from the water level
sensor and stored in the database"""

#Imported libraries.
import matplotlib.pyplot as plt
import datetime
import numpy as np
"""import numpy as np
import pandas as pd
import seaborn as sns"""


def graph(water_levels, dates):
    x = []
    
    i = 0
    while (i < len(dates)):
        x.append(i)
        i = i + 1
        
    plt.stem(water_levels)
    plt.xticks(x, dates, rotation = 30)
    #plt.xtickslabels(dates, rotation='vertical', fontsize=18)
    #plt.xticks(x, dates)
    plt.title("Graph of Date Vs Water Level.")
    plt.grid(b=True)
    plt.ylabel("Water Level History")
    plt.xlabel("Dates")
    plt.show()
 


