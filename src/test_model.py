import torch
from torch_geometric.data import Batch

from dataset import QM9GapDataset
from model import GCNModel


# Load the QM9 dataset
dataset = QM9GapDataset()

# Get the first four molecules individually
molecules = [dataset[i] for i in range(4)]

# Combine the molecules into one batch
batch = Batch.from_data_list(molecules)

# Create the GCN model
model = GCNModel()

# Run a forward pass
with torch.no_grad():
    output = model(
        batch.x,
        batch.edge_index,
        batch.batch,
    )

print("Model test successful!")
print(f"Input node features: {batch.x.shape}")
print(f"Number of molecules in batch: {batch.num_graphs}")
print(f"Model output shape: {output.shape}")
print(f"Model output: {output}")