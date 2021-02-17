import os
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
import statistics

# Set your path to the folder containing the .csv files
PATH = './Data/' # Use your path

# Fetch all files in path
fileNames = os.listdir(PATH)

# Filter file name list for files ending with .csv
fileNames = [file for file in fileNames if '.csv' in file]

Correio = pd.DataFrame(pd.read_csv(PATH + fileNames[0]))
Metropoles = pd.DataFrame(pd.read_csv(PATH + fileNames[1]))

print(Metropoles.head())


