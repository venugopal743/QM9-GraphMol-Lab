from pathlib import Path

import torch
from torch_geometric.datasets import QM9
from torch_geometric.data import Data


ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"


class QM9GapDataset:
    """
    Wrapper around the QM9 dataset for HOMO-LUMO gap prediction.
    """

    TARGET_INDEX = 4

    def __init__(self):
        self.dataset = QM9(root=str(DATA_DIR / "qm9"))

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, index):
        molecule = self.dataset[index]

        # Select HOMO-LUMO gap as the prediction target.
        target = molecule.y[:, self.TARGET_INDEX]

        # Create a clean graph object.
        graph = Data(
            x=molecule.x,
            edge_index=molecule.edge_index,
            edge_attr=molecule.edge_attr,
            y=target,
            pos=molecule.pos,
            z=molecule.z,
        )

        return graph


if __name__ == "__main__":
    dataset = QM9GapDataset()

    print("QM9 GAP dataset loaded!")
    print(f"Number of molecules: {len(dataset)}")

    molecule = dataset[0]

    print("\nFirst processed molecule:")
    print(molecule)

    print(f"\nNode features: {molecule.x.shape}")
    print(f"Edge index: {molecule.edge_index.shape}")
    print(f"Edge features: {molecule.edge_attr.shape}")
    print(f"Target: {molecule.y}")
    print(f"Target shape: {molecule.y.shape}")