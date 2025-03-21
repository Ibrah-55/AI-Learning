import pandas as pd 
import numpy as np
data = pd.read_csv('data/president_heights.csv')
heights = data['height(cm)']
print("Heights: ", heights)
print("Mean height:       ", heights.mean())
print("Standard deviation:", heights.std())
print("Minimum height:    ", heights.min())
print("Maximum height:    ", heights.max())
print("25th percentile:   ", np.percentile(heights, 25))
print("Median:            ", np.median(heights))
print("75th percentile:   ", np.percentile(heights, 75))