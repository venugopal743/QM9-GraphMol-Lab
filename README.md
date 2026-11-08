# Graph Neural Networks for Molecular Property Prediction with Uncertainty Quantification and Explainability

A research-oriented project for predicting molecular properties from molecular graphs using Graph Neural Networks (GNNs), with a focus on **uncertainty quantification** and **model explainability**.

The project uses the **QM9 molecular dataset** and currently focuses on predicting the **HOMO-LUMO gap (`gap`)**.

---

## Project Overview

Molecules can naturally be represented as graphs:

- **Atoms → Nodes**
- **Chemical bonds → Edges**
- **Molecular properties → Prediction targets**

This project investigates how Graph Neural Networks can learn molecular representations and predict quantum-chemical properties directly from molecular graph structures.

The final system will combine:

1. Molecular graph representation
2. Graph Neural Network prediction
3. Uncertainty quantification
4. Explainability
5. Model evaluation
6. Interactive web demonstration

---

## Dataset

### QM9

The project uses the **QM9 dataset**, containing approximately **130,000 small organic molecules**.

Dataset statistics:

- Molecules: **130,831**
- Atom features: **11**
- Molecular target properties: **19**

The primary prediction target is:

> **HOMO-LUMO gap (`gap`)**

QM9 target index:

```text
4 → gap
