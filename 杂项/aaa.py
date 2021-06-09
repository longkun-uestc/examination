import numpy as np
if __name__ == '__main__':
    a = [1,2,3,4,5, 3,4]
    a = np.array(a)
    arg = np.argsort(a)[::-1]
    print(arg)
