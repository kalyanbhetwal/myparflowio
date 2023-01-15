

import numpy as np

arr3d = np.array([[[1, 2], [4, 5], [7, 8]], 
                   [[10, 11], [13, 14], [16, 17]], 
                  [[19, 20], [22, 23], [25, 26]],
                  [[1, 2], [3, 4], [4, 6]] ])
    
for k in range(2):
    for j in range(3):
        sum = 0;
        for i in range(4):
            sum+= arr3d[i][j][k]
            #print(arr3d[i][j][k])
        print(sum/4)
print('--------')
mean = arr3d.mean(axis=0)
print(mean)
print(mean.shape)