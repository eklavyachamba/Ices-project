import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\sunit\Desktop\Astro stage 2\col_density_final_boss2.csv')

df = df[(df['H2O_N'] > 0) & (df['CO2_N'] > 0) & (df['CO_N'] > 0) & (df['H2_N'] > 0)].copy()

df = df.sort_values(by='H2_N')

df['H2O_abund'] = df['H2O_N'] / df['H2_N']
df['CO2_abund'] = df['CO2_N'] / df['H2_N']
df['CO_abund']  = df['CO_N']  / df['H2_N']

df['H2O_abund_err_lower'] = df['H2O_abund'] * (df['H2O_N_err_lower'] / df['H2O_N'])
df['H2O_abund_err_upper'] = df['H2O_abund'] * (df['H2O_N_err_upper'] / df['H2O_N'])
df['CO2_abund_err_lower'] = df['CO2_abund'] * (df['CO2_N_err_lower'] / df['CO2_N'])
df['CO2_abund_err_upper'] = df['CO2_abund'] * (df['CO2_N_err_upper'] / df['CO2_N'])
df['CO_abund_err_lower']  = df['CO_abund']  * (df['CO_N_err_lower']  / df['CO_N'])
df['CO_abund_err_upper']  = df['CO_abund']  * (df['CO_N_err_upper']  / df['CO_N'])


fig, ax1 = plt.subplots(figsize=(9, 6))

# Matplotlib handles asymmetric errors by taking a list of [lower_error, upper_error]
ax1.errorbar(df['H2_N'], df['H2O_N'], yerr=[df['H2O_N_err_lower'], df['H2O_N_err_upper']],
             fmt='o', color='#1f77b4', label='$H_2O$', capsize=3, alpha=0.8, markersize=6)
ax1.errorbar(df['H2_N'], df['CO2_N'], yerr=[df['CO2_N_err_lower'], df['CO2_N_err_upper']],
             fmt='s', color='#ff7f0e', label='$CO_2$', capsize=3, alpha=0.8, markersize=6)
ax1.errorbar(df['H2_N'], df['CO_N'],  yerr=[df['CO_N_err_lower'],  df['CO_N_err_upper']],  
             fmt='^', color='#2ca02c', label='$CO$',  capsize=3, alpha=0.8, markersize=6)

ax1.set_xlabel('Total Hydrogen Column Density $N(H_2)$', fontsize=12)
ax1.set_ylabel('Ice Column Density', fontsize=12)
ax1.set_title('Ice Column Density vs. Total Cloud Depth', fontsize=14)
ax1.legend(loc='upper left', frameon=True)
ax1.grid(True, linestyle='--', alpha=0.4)

plt.tight_layout()
plt.savefig('Final_Column_Density_Growth.png', dpi=200)
plt.show()

# ==========================================
# 4. PLOT 2: ABUNDANCE VS. CLOUD DEPTH
# ==========================================
fig, ax2 = plt.subplots(figsize=(9, 6))

ax2.errorbar(df['H2_N'], df['H2O_abund'], yerr=[df['H2O_abund_err_lower'], df['H2O_abund_err_upper']],
             fmt='o', color='#1f77b4', label='$H_2O$', capsize=3, alpha=0.8, markersize=6)
ax2.errorbar(df['H2_N'], df['CO2_abund'], yerr=[df['CO2_abund_err_lower'], df['CO2_abund_err_upper']],
             fmt='s', color='#ff7f0e', label='$CO_2$', capsize=3, alpha=0.8, markersize=6)
ax2.errorbar(df['H2_N'], df['CO_abund'],  yerr=[df['CO_abund_err_lower'],  df['CO_abund_err_upper']],  
             fmt='^', color='#2ca02c', label='$CO$',  capsize=3, alpha=0.8, markersize=6)

ax2.set_xlabel('Total Hydrogen Column Density $N(H_2)$', fontsize=12)
ax2.set_ylabel('Ice Abundance (Ice / $H_2$)', fontsize=12)
ax2.set_title('Ice Abundances vs. Total Cloud Depth', fontsize=14)
ax2.legend(loc='upper right', frameon=True)
ax2.grid(True, linestyle='--', alpha=0.4)

plt.tight_layout()
#plt.savefig('Final_Abundance_Growth.png', dpi=200)
plt.show()

# ==========================================
# 5. TERNARY PLOT: ICE COMPOSITION
# ==========================================
import ternary
import matplotlib.pyplot as plt

# --- Normalize to percentages ---
df['sum_ice'] = df['H2O_N'] + df['CO2_N'] + df['CO_N']

df['f_H2O'] = 100 * df['H2O_N'] / df['sum_ice']
df['f_CO2'] = 100 * df['CO2_N'] / df['sum_ice']
df['f_CO']  = 100 * df['CO_N']  / df['sum_ice']

points = list(zip(df['f_H2O'], df['f_CO2'], df['f_CO']))

# --- Figure ---
scale = 100
fig, tax = ternary.figure(scale=scale)
fig.set_size_inches(7, 6)

# --- Color mapping (cleaner than viridis for papers) ---
norm = plt.Normalize(df['H2_N'].min(), df['H2_N'].max())
cmap = plt.cm.plasma   # 🔥 nicer than viridis for contrast
colors = cmap(norm(df['H2_N']))

# --- Scatter ---
tax.scatter(points, c=colors, s=50, edgecolors='k', linewidths=0.3, alpha=0.9)

# --- Boundary & grid ---
tax.boundary(linewidth=1.5)
tax.gridlines(multiple=10, color="gray", linestyle='--', linewidth=0.5, alpha=0.6)

# --- Axis labels (match your image style) ---
tax.left_axis_label("% CO", fontsize=12, offset=0.14)
tax.right_axis_label("% CO2", fontsize=12, offset=0.14)
tax.bottom_axis_label("% H2O", fontsize=12, offset=0.04)

# --- Ticks ---
tax.ticks(axis='lbr', multiple=20, linewidth=1, tick_formats="%d")

tax.clear_matplotlib_ticks()

# --- Title ---
tax.set_title("Ice Composition (Ternary)", fontsize=14, pad=15)

# --- Colorbar (fixed properly) ---
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])

cbar = plt.colorbar(sm, ax=tax.get_axes(), fraction=0.046, pad=0.08)
cbar.set_label(r'$N(H_2)$', fontsize=11)

plt.tight_layout()
plt.savefig('Ternary_Final_Publication.png', dpi=300)
plt.show()