import pandas as pd
import numpy as np
def get_kb(p1, p2):
    k = (p1[1]-p2[1])/(p1[0]-p2[0])
    b = p1[1]-(k*p1[0])
    return k, b

def get_dsc(k, b, ap):
    return k*ap+b

if __name__ == '__main__':
    x1, y1 = 40.92, 74.03
    x2, y2 = 32.82, 63.96
    k, b = get_kb((x1, y1), (x2, y2))
    print(k, b)
    ap = [37.55, 38.2, 40.67, 40.74, 41.97, 38.08, 41.48, 40.89, 38.83, 40.14, 41.15, 40.88, 41.49, 40.91, 41.87, 40.73]
    ap = [19.9, 21.3, 20.4, 23.5, 31.0, 36.3, 32.1, 38.6]
    ap = [22.7, 23.1, 19.9, 31.0, 37.5, 36.8, 37.2, 38.6, 41.5]
    dsc = [get_dsc(k, b, x) for x in ap]
    print(dsc)
    data = np.array([ap, dsc])
    data = data.T
    df = pd.DataFrame(data)
    df.to_excel('2.xlsx')
