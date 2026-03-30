# Scipy functions

---

# 1. Linear Algebra (`scipy.linalg`)

* `linalg.inv()` → Matrix inverse
* `linalg.det()` → Determinant
* `linalg.eig()` → Eigenvalues & eigenvectors
* `linalg.eigh()` → Eigenvalues (symmetric matrices)
* `linalg.svd()` → Singular Value Decomposition
* `linalg.solve()` → Solve linear equations
* `linalg.lstsq()` → Least squares solution
* `linalg.norm()` → Matrix/vector norm

---

# 2. Optimization (`scipy.optimize`)

* `optimize.minimize()` → General minimization
* `optimize.maximize()` → (via negative minimization)
* `optimize.curve_fit()` → Curve fitting
* `optimize.least_squares()` → Least-squares optimization
* `optimize.root()` → Solve nonlinear equations
* `optimize.fsolve()` → Solve system of equations
* `optimize.linprog()` → Linear programming

---

# 3. Integration (`scipy.integrate`)

* `integrate.quad()` → Single-variable integration
* `integrate.dblquad()` → Double integration
* `integrate.tplquad()` → Triple integration
* `integrate.odeint()` → Solve ODEs
* `integrate.solve_ivp()` → Modern ODE solver

---

# 4. Interpolation (`scipy.interpolate`)

* `interpolate.interp1d()` → 1D interpolation
* `interpolate.interp2d()` → 2D interpolation
* `interpolate.griddata()` → Interpolation on scattered data
* `interpolate.splrep()` / `splev()` → Spline representation & evaluation

---

# 5. Statistics (`scipy.stats`)

* `stats.describe()` → Summary statistics
* `stats.mean()` → Mean
* `stats.median()` → Median
* `stats.mode()` → Mode
* `stats.variance()` → Variance
* `stats.std()` → Standard deviation
* `stats.norm()` → Normal distribution
* `stats.t()` → t-distribution
* `stats.chi2()` → Chi-square distribution
* `stats.ttest_ind()` → Independent t-test
* `stats.ttest_rel()` → Paired t-test
* `stats.pearsonr()` → Correlation coefficient
* `stats.spearmanr()` → Rank correlation

---

# 6. Signal Processing (`scipy.signal`)

* `signal.convolve()` → Convolution
* `signal.correlate()` → Correlation
* `signal.butter()` → Butterworth filter
* `signal.filtfilt()` → Apply filter
* `signal.find_peaks()` → Peak detection
* `signal.spectrogram()` → Spectral analysis

---

# 7. Sparse Matrices (`scipy.sparse`)

* `sparse.csr_matrix()` → Compressed Sparse Row matrix
* `sparse.csc_matrix()` → Compressed Sparse Column matrix
* `sparse.lil_matrix()` → List of Lists format
* `sparse.eye()` → Sparse identity matrix
* `sparse.diags()` → Diagonal sparse matrix
* `sparse.linalg.spsolve()` → Solve sparse system

---

# 8. Spatial Algorithms (`scipy.spatial`)

* `spatial.distance.euclidean()` → Euclidean distance
* `spatial.distance.cdist()` → Pairwise distances
* `spatial.KDTree()` → Nearest neighbor search
* `spatial.ConvexHull()` → Convex hull computation

---

# 9. FFT (Fast Fourier Transform) (`scipy.fft`)

* `fft.fft()` → Fast Fourier Transform
* `fft.ifft()` → Inverse FFT
* `fft.fftfreq()` → Frequency bins
* `fft.fftshift()` → Shift zero frequency

---

# 10. Image Processing (`scipy.ndimage`)

* `ndimage.imread()` → Read image (deprecated; use imageio)
* `ndimage.gaussian_filter()` → Gaussian blur
* `ndimage.rotate()` → Rotate image
* `ndimage.zoom()` → Zoom image
* `ndimage.label()` → Label regions

---

# 11. Special Functions (`scipy.special`)

* `special.expit()` → Sigmoid function
* `special.gamma()` → Gamma function
* `special.beta()` → Beta function
* `special.jv()` → Bessel function
* `special.erf()` → Error function

---

# 12. Constants (`scipy.constants`)

* `constants.pi` → π
* `constants.e` → Euler’s number
* `constants.c` → Speed of light
* `constants.G` → Gravitational constant
* `constants.h` → Planck constant

