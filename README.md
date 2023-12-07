# Mean-Variance-Standard Deviation Calculator

This is the boilerplate for the Mean-Variance-Standard Deviation Calculator project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator

import numpy as np

def calculate(list):
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")
  ra = np.array(list).reshape(3,3)





  calculations = {
    'mean': [ra.mean(axis=0).tolist(), ra.mean(axis=1).tolist(), ra.mean()],
    'variance': [ra.var(axis=0).tolist(), ra.mean(axis=1).tolist(), ra.var()],
    'standard deviation': [ra.std(axis=0).tolist(), ra.std(axis=1).tolist(), ra.std()],
    'max': [ra.max(axis=0).tolist(), ra.max(axis=1).tolist(), ra.max()],
    'min': [ra.min(axis=0).tolist(), ra.min(axis=1).tolist(), ra.min()],
    'sum': [ra.sum(axis=0).tolist(), ra.sum(axis=1).tolist(), ra.sum()]
  }
  return calculations