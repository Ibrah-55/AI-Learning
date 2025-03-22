import numpy as np
import pandas as pd 
import seaborn as sns

titanic = sns.load_dataset('titanic')   

print(titanic.head())
print(titanic.groupby('sex')[['survived']].mean())
print(titanic.groupby(['sex', 'class'])['survived'].aggregate('mean').unstack())

