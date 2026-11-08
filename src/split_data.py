import torch
from torch.utils.data import random_split

from dataset import QM9GapDataset


SEED = 42

TRAIN_RATIO = 0.80
VAL_RATIO = 0.10
TEST_RATIO = 0.10


def split_dataset(dataset):
    """Split QM9 into training, validation, and test sets."""

    total_size = len(dataset)

    train_size = int(TRAIN_RATIO * total_size)
    val_size = int(VAL_RATIO * total_size)
    test_size = total_size - train_size - val_size

    generator = torch.Generator().manual_seed(SEED)

    train_dataset, val_dataset, test_dataset = random_split(
        dataset,
        [train_size, val_size, test_size],
        generator=generator,
    )

    return train_dataset, val_dataset, test_dataset


if __name__ == "__main__":
    dataset = QM9GapDataset()

    train_dataset, val_dataset, test_dataset = split_dataset(dataset)

    print("QM9 dataset split completed!")
    print(f"Total molecules: {len(dataset)}")
    print(f"Training molecules: {len(train_dataset)}")
    print(f"Validation molecules: {len(val_dataset)}")
    print(f"Test molecules: {len(test_dataset)}")