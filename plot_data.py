"""A simple program to plot data got from the water level
sensor and stored in the database"""

#Imported libraries.
import matplotlib.pyplot as plt

def graph(water_levels, dates):
    plt.plot(water_levels)
    plt.ylabel("Water Level History")
    plt.xlabel("Dates")
    plt.show()

