# QM9·GraphMol LAB — Molecular GNN Research Platform

An end-to-end web application built around the QM9 Graph Neural Network (GNN) molecular property prediction research project with uncertainty quantification and explainability.

---

## 🔬 Core Capabilities & Features

### 1. 🌀 Overview (`#overview`)
- **Interactive Molecular Hero:** Animated floating molecular graph canvas with glowing atoms (C, O, N, H) and bond dynamics.
- **Key Empirical Research Metrics:**
  - **130,831** QM9 molecules cataloged across 19 quantum-chemical properties.
  - **0.934 Best R² score** achieved by the GCN Comparison run on 13,084 held-out test molecules.
  - **0.220 MC Dropout correlation** demonstrating significant correlation between epistemic variance and absolute test errors.
- **Research Foundations Grid:**
  - 11-Dimensional node feature vectors ($X \in \mathbb{R}^{N \times 11}$)
  - Message-passing graph neural networks (GCN, GraphSAGE, GAT)
  - Monte Carlo Dropout epistemic uncertainty ($p=0.2$, 50 stochastic passes)
  - Gradient-based atom attribution saliency

### 2. 🗄️ Dataset Explorer (`#dataset`)
- **Curated 16-Molecule Library:** Ethanol, Benzene, Acetone, Glycine, Pyridine, Formamide, Aniline, Methanol, Formaldehyde, Ethane, Methane, Urea, Toluene, Phenol, Aspirin, and Caffeine.
- **Search & Filter:** Search by compound name, chemical formula, or SMILES notation.
- **Selected Record Panel:**
  - Interactive 2D chemical structure graph renderer with atom symbols and bond connectivity.
  - Molecular metrics: Molecular weight, heavy atom count, dipole moment, and HOMO–LUMO gap.
  - **"Analyze in workspace"** button for immediate property prediction.
- **Custom CSV Dataset Inspector:**
  - Drag-and-drop or select any CSV file.
  - Automatic SMILES validation using RDKit, duplicate check, missing value audit, and table preview.

### 3. ⚗️ Interactive Workspace (`#workspace`)
- **Inference Input:** Enter any SMILES string or choose from sample chips (`CCO`, `c1ccccc1`, `NCC(=O)O`, `Nc1ccccc1`, `CC(=O)C`).
- **Model Architecture Variant:**
  - `GCN · best R² (0.934)`
  - `GraphSAGE · comparison (0.927)`
  - `Improved GCN (0.924)`
  - `GAT · comparison (0.908)`
- **Output Metrics & Uncertainty Quantification:**
  - **Predicted HOMO–LUMO Gap** (in eV)
  - **Uncertainty ($\pm\sigma$)** (in eV)
  - **Confidence Tier** (`high`, `moderate`, `low`)
  - **Visual $\pm 1.96\sigma$ Confidence Interval Bar** displaying 95% predictive bounds.
  - **"Explain atoms"** direct jump button to interpret structural contributions.

### 4. 🤖 AI Research Assistant (`#assistant`)
- **Intelligent Molecular Dialogue:**
  - Pre-loaded with research domain knowledge about QM9, HOMO–LUMO gap quantum physics, and model metrics.
  - Quick-prompt chips:
    - *Explain the C₆H₆ prediction*
    - *Why does GAT underperform GCN here?*
    - *How should I read the uncertainty?*
    - *What are the 11 QM9 atom features?*
  - Natural conversation interface supporting questions about specific molecules, failure modes, and GNN mechanisms.

### 5. 🔬 Explainability (`#explainability`)
- **Atom-Level Attribution Visualizer:**
  - Real-time interactive molecular graph highlighting atoms with glowing halos based on their influence on the HOMO–LUMO gap.
  - Color-coded legend: High heuristic weight (coral/magenta) vs lower weight (purple/blue).
  - Individual atom cards with numeric score and chemical role (e.g., *aromatic ring*, *carbonyl oxygen*, *amine donor*).
- **Research Artifacts:**
  - Displays original project figures: `explained_molecule.png` and `atom_importance.png`.
  - Explains loss gradient backpropagation $\partial \hat{y} / \partial X_v$.

### 6. 📊 Model Benchmarks (`#benchmarks`)
- **Evaluation Snapshot Table:** Test MAE, RMSE, and $R^2$ comparing GCN (0.934), GraphSAGE (0.927), Improved GCN (0.924), Original GCN (0.641), and GAT (0.588).
- **$R^2$ Architecture Progress Bars:** Gradient-filled visual meters.
- **Research Visualizations Gallery:**
  - Actual vs Predicted Scatter Fit (`actual_vs_predicted.png`)
  - Training & Validation MSE Convergence Curve (`training_validation_mse.png`)
  - Error Distribution Histogram (`error_distribution.png`)
  - Uncertainty vs Error Correlation (`uncertainty_vs_error.png`)
  - Error vs Molecule Size Breakdown (`error_vs_molecule_size.png`)
  - Atom Saliency Map (`atom_importance.png`)

---

## 🚀 How to Run the Website

### Option 1: Double-Click
Double-click `run_web.bat` in the project root directory.

### Option 2: Terminal / PowerShell
```powershell
cd C:\Users\chunc_yhjtd63\.gemini\antigravity\scratch\qm9-gnn-project\QM9-GNN-Molecular-AI
python run_web.py
```

Then open your browser to:
```text
http://127.0.0.1:8000
```
