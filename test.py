import numpy as np

#a = np.array([0, 3, 4, 3, 4, 3, 0, 8, 2, 5, 0, 5, 5, 3, 8, 8, 4, 4, 5, 4, 5, 0,5, 8, 1])
#b = np.array([4, 4, 4, 6, 8, 1, 5, 4, 2, 2, 7, 7, 0, 5, 2, 8, 8, 5, 8, 5, 1, 2,1, 1, 5])
#c = a*b
#d = c.reshape(5,5)
#print(d)

b = np.array([[[4], [4], [4]],[[6],[8],[1]]])
print(b.shape)
print(b.shape[0],b.shape[1])
c = b.reshape(b.shape[0],b.shape[1])
print(c.shape)
print(c)
print(b)

#test11
print(c)
