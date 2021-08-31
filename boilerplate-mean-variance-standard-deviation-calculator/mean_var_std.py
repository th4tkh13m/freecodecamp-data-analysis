import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    calculations = dict()
    arr = np.array(list)
    arr_res = arr.copy().reshape((3,3))
    functions = [np.mean, np.var, np.std, np.max, np.min, np.sum]
    keys = ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']
    for _ in range(len(keys)):
        calculations[keys[_]] = [functions[_](arr_res, axis=0).tolist(),
                                 functions[_](arr_res, axis=1).tolist(),
                                 functions[_](arr)]
        
    return calculations

print(calculate([0,1,2,3,4,5,6,7,8]))