from matplotlib import pyplot as plt
from astropy.io import fits
from matplotlib.colors import LogNorm
import numpy as np

hdu = fits.open("data.fits")
# hdu.info()

data = np.array([[]])
for i in range(1,101):
    data = np.append(data, hdu[i].data)

print(data.shape)
data = data.reshape(100,200,200)
median_data = np.median(data, axis=0)
mean_data = np.mean(data, axis=0)

fig, axes = plt.subplots(ncols=3, nrows=2, figsize=(12, 12))

axes[0][0].imshow(mean_data, cmap='gray')
axes[1][0].imshow(median_data,  cmap='gray')
axes[0][0].set_title("Среднее изображение")
axes[1][0].set_title("Медианное изображение")



seq = []; slice_median = []; slice_mean = []
for i in range(200):
    seq.append(i)
    slice_median = np.append(slice_median, median_data[100][i]/2 + median_data[101][i]/2 )
    slice_mean = np.append(slice_mean, mean_data[100][i]/2 + mean_data[101][i]/2)

growth_curves_median = np.zeros(100); growth_curves_mean = np.zeros(100)
for r in range(100):
    for i in range(200):
        for j in range(200):
            if((100 - i)*(100 - i) + (100 - j)*(100 - j) < r*r):
                growth_curves_mean[r] += mean_data[i,j]
                growth_curves_median[r] += median_data[i,j]


# for j in range(100):
#     growth_curves_mean = np.append(growth_curves_mean, mean_data[100-j:100+j,100-j:100+j].sum())
#     growth_curves_median = np.append(growth_curves_median, median_data[100-j:100+j,100-j:100+j].sum())


axes[0][1].plot(seq,slice_mean)
axes[1][1].plot(seq,slice_median)
axes[0][2].plot(seq[:100],growth_curves_mean)
axes[0][2].semilogx()
axes[1][2].plot(seq[:100],growth_curves_median)
axes[1][2].semilogx()



plt.show()