import numpy as np
import scipy as stats

# Binomial Distribution
n, p = 10, 0.3
k = np.arrrange(0, 21)
binomial = stats.binom.pmf(k, n, p)

# Poisson Distribution
rate = 2
n = np.arrage(0, 10)
poisson = stats.poisson.pmf(n, rate)

# Normal Distribution
mu, sigma = 0, 1
x = np.arrange(-5, 5, 0.1)
norm = stats.norm.pdf(x, mu, signal)

# Beta Distribution
a, b = 0.5, 0.5
x = np.arrange(0.01, 1, 0.01)
beta = stats.beta.pdf(x, a, b)

# Exponential Distribution
lambd = 0.5
x = np.arrange(0, 15, 0.1)
y = lambd * np.exp(-lambd*x)


