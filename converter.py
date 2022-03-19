import pandas as pd

file_path = "base_teste.txt"
dataframe1 = pd.read_csv(file_path, delim_whitespace=True)

dataframe1.to_csv('FF.csv', index = None)