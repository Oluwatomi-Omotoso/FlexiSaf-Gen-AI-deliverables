### 1. Basic Line Plots using matplotlib

- **Single & Multiple Lines:** Demonstrates plotting 1D NumPy arrays using `plt.plot()`.
- **Plot Customization:** Combines multiple line series on a single axis, customizes figure dimensions (`figsize=(14,9)`), applies styled line patterns (e.g., `---.`), modifies line widths, adds bold titles, and configures legends.

### 2. Scatter Plots with Dynamic Sizing

- **Random Data Generation:** Uses `np.arange()` and `np.random.randint()` to construct coordinate sets.
- **Bubble Charts:** Uses `plt.scatter()` to vary point markers dynamically using a third randomized size array (`s=size`).

### 3. Seaborn Statistical Visualizations

- **Dataset Integration:** Uses Seaborn's built-in `tips` dataset (`sns.load_dataset('tips')`).
- **Histograms & KDE:**
  - Displays tip frequency distributions using `sns.histplot()`.
  - Integrates Kernel Density Estimation (`kde=True`) to visualize continuous probability distributions across custom bin ranges.
- **Categorical Bar Charts:**
  - Uses `sns.barplot()` to inspect average `total_bill` amounts per day of the week.
  - Adds standard deviation error bars (`errorbar='sd'`) and applies color palettes (`palette='viridis'`).

