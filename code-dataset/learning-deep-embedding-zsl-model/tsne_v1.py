import numpy as np
from skdata.mnist.views import OfficialImageClassification
from matplotlib import pyplot as plt
from tsne import bh_sne
from datahelpers import datahelpersAWA
#[58]
# load up data
#data = OfficialImageClassification(x_dtype="float32")
#x_data = data.all_images
#y_data = data.all_labels
dataset = datahelpersAWA()
x_data = dataset['googlenetFeatures']
y_data = dataset['datasetLabels']

# convert image data to float64 matrix. float64 is need for bh_sne
x_data = np.asarray(x_data).astype('float64')
#x_data = x_data.reshape((x_data.shape[0], -1))

# For speed of computation, only run on a subset
n = 14000
x_data = x_data[:n]
y_data = y_data[:n]

mean = np.mean(x_data, axis=0)
#std = np.std(x_data, axis=0)
std = np.max(x_data, axis=0) - np.min(x_data, axis=0)
x_data = (x_data - mean)/std

# perform t-SNE embedding
vis_data = bh_sne(x_data)

# plot the result
vis_x = vis_data[:, 0]
vis_y = vis_data[:, 1]

plt.scatter(vis_x, vis_y, c=y_data, cmap=plt.cm.get_cmap("jet", 20))
plt.colorbar(ticks=range(20))
plt.clim(-0.5, 20.5)
plt.show()