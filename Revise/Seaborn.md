# Seaborn functions

---

# 1. Relational Plots

Used to visualize relationships between variables.

* `sns.scatterplot()` → Scatter plot
* `sns.lineplot()` → Line plot
* `sns.relplot()` → Figure-level relational plots (combines scatter/line)

---

# 2. Categorical Plots

Used for comparisons across categories.

* `sns.barplot()` → Bar plot (with aggregation)
* `sns.countplot()` → Count of observations
* `sns.boxplot()` → Box plot
* `sns.violinplot()` → Violin plot
* `sns.stripplot()` → Scatter with categorical axis
* `sns.swarmplot()` → Non-overlapping categorical scatter
* `sns.catplot()` → Figure-level categorical plots

---

# 3. Distribution Plots

Used to understand data distribution.

* `sns.histplot()` → Histogram
* `sns.kdeplot()` → Kernel density estimate
* `sns.displot()` → Figure-level distribution plot
* `sns.ecdfplot()` → Empirical cumulative distribution

---

# 4. Regression & Statistical Plots

Used to show statistical relationships.

* `sns.regplot()` → Regression plot
* `sns.lmplot()` → Linear model plot (figure-level)
* `sns.residplot()` → Residual plot

---

# 5. Matrix Plots

Used for visualizing matrices and correlations.

* `sns.heatmap()` → Heatmap (e.g., correlation matrix)
* `sns.clustermap()` → Hierarchical clustering heatmap

---

# 6. Multi-Plot Grids

Used to create structured visual layouts.

* `sns.FacetGrid()` → Grid of subplots by category
* `sns.PairGrid()` → Pairwise relationships grid
* `sns.pairplot()` → Quick pairwise plots
* `sns.jointplot()` → Bivariate + marginal distributions

---

# 7. Styling & Themes

Used to control appearance.

* `sns.set_theme()` → Set overall theme
* `sns.set_style()` → Style (white, dark, etc.)
* `sns.set_context()` → Context (paper, talk, poster)
* `sns.despine()` → Remove axis spines

---

# 8. Color Utilities

* `sns.color_palette()` → Generate color palettes
* `sns.light_palette()` → Light color variations
* `sns.dark_palette()` → Dark color variations
* `sns.cubehelix_palette()` → Perceptually uniform palette

---

# 9. Utility Functions

* `sns.load_dataset()` → Load built-in datasets
* `sns.get_dataset_names()` → List datasets

---

## Summary

* **Relationships** → `scatterplot`, `lineplot`, `relplot`
* **Categories** → `barplot`, `boxplot`, `violinplot`
* **Distributions** → `histplot`, `kdeplot`, `displot`
* **Statistics** → `regplot`, `lmplot`
* **Grids** → `pairplot`, `jointplot`, `FacetGrid`
* **Styling** → `set_theme`, `color_palette`


