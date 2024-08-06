import numpy as np

def cosine_distance(a, b):
    cosine = np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))
    return cosine

a = np.array([5,3,1,5])
b = np.array([-5,3,1,4])

print(cosine_distance(a,b))
