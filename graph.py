import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    'serie1' : [1, 3, 4, 3, 5],
    'serie2' : [2, 4, 5, 2, 4],
    'serie3' : [3, 2, 3, 1, 3]
}

df=pd.DataFrame(data)
df.plot(kind='bar')
plt.show()