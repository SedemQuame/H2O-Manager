"""A simple program to plot data got from the water level
sensor and stored in the database"""

#Imported libraries.
import matplotlib.pyplot as plt
import datetime
import numpy as np

def graph(water_levels, dates):
    x = []
    
    i = 0
    
    while (i < len(water_levels)):
        x.append(i)
        i = i + 1
        
    plt.plot(water_levels)
    plt.xticks(x, dates, rotation = 'vertical', fontsize=6)
    #plt.xtickslabels(dates, rotation='vertical', fontsize=18)
    #plt.xticks(x, dates)
    plt.title("Graph of Date Vs Water Level.")
    plt.grid(b=True)
    plt.ylabel("Water Level History")
    plt.xlabel("Date On Which Level Was Recorded")
    plt.show()
 


