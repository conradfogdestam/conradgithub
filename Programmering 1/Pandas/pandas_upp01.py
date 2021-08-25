import pandas as pd
import numpy as np

df = pd.read_csv('sysselsattning.csv')
np.sum(df,axis=1)
print(df)