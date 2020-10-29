import numpy as np
from matplotlib import pyplot as plt

skeleton_data = np.load("a1_s1_t1_skeleton.npy")
t = np.swapaxes(skeleton_data,1,2)
print("Old shape %s, New shape %s"%(skeleton_data.shape, t.shape))
# Normalization
t -= np.min(t)
t /= np.max(t)
# Displaying
plt.imshow(t, interpolation='nearest')
plt.show()

