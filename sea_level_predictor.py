import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv(r'epa-sea-level.csv')


    # Create scatter plot
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    year_2050 = pd.Series([int(i) for i in range(1880, 2051)])

    res = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])

    plt.plot(year_2050, res.intercept + res.slope*year_2050, 'r', label='fitted line',color='blue')
    
    # Create second line of best fit
    df_2000 = df[df['Year']>=2000]
    year_2000 = pd.Series([int(i) for i in range(2000, 2051)])

    slope_y, intercept_y, r_y, p_y, std_err_y = linregress(df_2000['Year'],df_2000['CSIRO Adjusted Sea Level'])

    df_2000.append(year_2000, ignore_index=True)

    plt.plot(year_2000, intercept_y + slope_y*year_2000, 'r', label='new best fit line after year 2000', color="red")

    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.legend()

    plt.show()
      
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
