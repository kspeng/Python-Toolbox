'''
Probability Density Function
Cummulated Density Function

Date: 2018-08-26
By: Kuo
'''
import numpy as np
from scipy import stats
from scipy import signal
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

# some fake data
data = np.random.randn(1000)
# evaluate the histogram
pdf, base = np.histogram(data, bins=40)
pdf = pdf/np.max(pdf)
#evaluate the cumulative
cdf = np.cumsum(pdf)
cdf = cdf/np.max(cdf)

# plot pdf
ax.plot(base[:-1], pdf, c='blue', label='pdf')
# plot cdf
ax.plot(base[:-1], cdf, 'r-', lw=5, alpha=0.2, label='cdf')

ax.legend(loc='best', frameon=False)
plt.show()
