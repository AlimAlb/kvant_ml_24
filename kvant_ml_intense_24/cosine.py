import numpy as np

a = np.array([1,2,3])
b = np.array([-3,2,1])

print(np.dot(a,b))
# 1*3 + 2*4 + 3*5 = 26
# cos(a) = (a,b)/(|a||b|)

cosine = np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))

print(cosine)
