# simple utilisation of numpy and pandas

# import numpy as np
# # a = np.array(
# #     [[[1, 2, 3],
# #     [3, 4, 5]],
# #     [[6, 7, 8],
# #     [8, 9, 10]]]
# # )
# # print(a)

# # a = np.ones([5])
# # print(a)

import pandas as pd
data = {
    'col1': [1,2,3,4,5],
    'col2': [10,20,30,40,50],
    'col3': ['A','B','C','D','E']
}
df = pd.DataFrame(data)
print(df.describe())