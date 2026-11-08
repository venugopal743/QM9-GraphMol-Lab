from pathlib import Path

from torch_geometric.datasets import QM9


# Project root directory
ROOT_DIR = Path(__file__).resolve().parents[1]

# Directory where the QM9 dataset is stored
DATA_DIR = ROOT_DIR / "data"


def load_qm9():
    """Load the QM9 molecular dataset."""

    dataset = QM9(root=str(DATA_DIR / "qm9"))

    print("QM9 dataset loaded successfully!")
    print(f"Number of molecules: {len(dataset)}")
    print(f"Number of atom features: {dataset.num_node_features}")
    print(f"Number of target properties: {dataset[0].y.shape[1]}")

    return dataset


if __name__ == "__main__":
    dataset = load_qm9()

    molecule = dataset[0]

    print("\nFirst molecule:")
    print(molecule)

    print(f"\nNumber of atoms: {molecule.num_nodes}")
    print(f"Number of edges: {molecule.num_edges}")
    print(f"Node feature shape: {molecule.x.shape}")
    print(f"Target shape: {molecule.y.shape}")
    print("\nQM9 target properties:")
    target_names = [
    "mu",
    "alpha",
    "homo",
    "lumo",
    "gap",
    "r2",
    "zpve",
    "u0",
    "u298",
    "h298",
    "g298",
    "cv",
    "u0_atom",
    "u298_atom",
    "h298_atom",
    "g298_atom",
    "a",
    "b",
    "c",
    ]

    print("\nQM9 target properties:")
    for index, name in enumerate(target_names):
        print(f"{index}: {name}")