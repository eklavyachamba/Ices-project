🌌 Interstellar Ice Infrared Spectroscopy Analysis

This repository contains tools for analyzing infrared (IR) spectra of interstellar ices, with a focus on extracting column densities, continuum fitting, and molecular feature characterization from observational data (e.g., JWST, ground-based telescopes).

📖 Overview

Interstellar ices (e.g., H₂O, CO, CO₂, CH₃OH) play a critical role in astrochemistry and star formation. Their vibrational modes produce distinct absorption features in the infrared, which can be analyzed to determine:

Molecular composition
Ice abundances (column densities)
Environmental conditions (temperature, radiation, density)

This codebase provides a pipeline to process spectra and quantify these properties.

⚙️ Features
📊 Continuum fitting (e.g., spline, PCHIP interpolation)
🔍 Optical depth calculation
📉 Column density estimation using band strengths
🧊 Analysis of key ice features:
CO (~4.67 µm)
CO₂ (~15.2 µm)
H₂O (~3.0 µm)
📈 Visualization of spectra and fitted continua
⚠️ Handling of saturation effects (e.g., CO₂ red wing method)
Requirements
Python ≥ 3.8
NumPy
SciPy
Pandas
Matplotlib
🔬 Methodology
1. Continuum Fitting

A baseline continuum is fitted using interpolation methods such as:

Savitzky-Golay smoothing
PCHIP interpolation
2. Optical Depth Calculation
τ(ν)=-ln(I_obs/I_cont)
3. Column Density
N=∫τ(ν)dν/A

Where:

N: Column density (cm⁻²)
A: Band strength (cm molecule⁻¹)
τ: Optical depth
4. Saturation Handling


For saturated features (e.g., CO₂), the red wing is used and scaled appropriately to estimate total column density.
📈 Output
Continuum-fitted spectra plots
Optical depth profiles
Column density values (displayed on plots)
Processed data files
| Molecule | Feature (µm) | Notes                            |
| -------- | ------------ | -------------------------------- |
| H₂O      | 3.0          | Broad absorption                 |
| CO       | 4.67         | Narrow, sensitive to environment |
| CO₂      | 15.2         | Often saturated                  |
| CH₃OH    | ~3.53        | Weak, difficult detection        |

🔭 Future Work
JWST NIRSpec/NIRCam pipeline integration
Automated feature detection
Machine learning–based continuum fitting
Error propagation and uncertainty estimation
References
Boogert et al. (2015), ARA&A, Interstellar Ices
Öberg et al. (2011), Ice evolution in star-forming regions
JWST data documentation
