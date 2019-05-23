import numpy as np

t = np.arange(12).reshape((3,4)).astype("float")
t[1,2:] = np.nan
print(t)
def fill_ndarray(t):
    for i in range(t.shape[1]):
        temp_col = t[:,i]
        nan_num = np.count_nonzero(temp_col!=temp_col)
        if nan_num != 0:
            tem_not_nan_col = temp_col[temp_col==temp_col]  #当前一列不为nan的array

            #选中当前为nan的位置，把赋值为不为nan的中位数
            temp_col[np.isnan(temp_col)] = tem_not_nan_col.mean()

    return(t)
