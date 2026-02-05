import pandas as pd
import numpy as np 
df = pd.read_csv(r"C:\Users\jana0\Downloads\Stress-Lysis.csv")
print(df.head())
print("shape (rows, columns): ", df.shape)
print(df.columns)
df.info()
