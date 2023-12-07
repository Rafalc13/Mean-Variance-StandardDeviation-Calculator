import numpy as np

def calculate(list):
  if len(list) < 9:
    raise ValueError( "List must contain nine numbers.")
  ra = np.array(list).reshape(3,3)

  mean = [ra.mean(axis=0).tolist(), ra.mean(axis=1).tolist(), ra.mean()]
  variance = [ra.var(axis=0).tolist(), ra.var(axis=1).tolist(), ra.var()]
  standard_deviation = [ra.std(axis=0).tolist(), ra.std(axis=1).tolist(), ra.std()]
  max = [ra.max(axis=0).tolist(), ra.max(axis=1).tolist(), ra.max()]
  min = [ra.min(axis=0).tolist(), ra.min(axis=1).tolist(), ra.min()]
  sum = [ra.sum(axis=0).tolist(), ra.sum(axis=1).tolist(), ra.sum()]

  
  return {
    'mean': mean,
    'variance': variance,
    'standard deviation': standard_deviation,
    'max': max,
    'min': min,
    'sum': sum
  }