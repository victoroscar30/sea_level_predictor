import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    regression = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    slope = regression.slope
    intercept = regression.intercept
    x_pred = np.arange(1880, 2051)
    y_pred = slope * x_pred + intercept

    # Create second line of best fit
    df_recentlevel = df[df['Year']>=2000]
    regression_new = linregress(df_recentlevel['Year'],df_recentlevel['CSIRO Adjusted Sea Level'])
    slope_new = regression_new.slope
    intercept_new = regression_new.intercept
    x_pred_new = np.arange(2000, 2051)
    y_pred_new = slope_new * x_pred_new + intercept_new
    plt.plot(x_pred,y_pred,color = 'red')
    plt.plot(x_pred_new,y_pred_new,color = 'orange')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()