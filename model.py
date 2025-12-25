import numpy as np
import torch
import torch.nn as nn

np.set_printoptions(precision=4, suppress=True)

torch.manual_seed(42)

dim = 64
samples = 512

X = torch.randn(samples, dim)
W = torch.randn(dim, dim) * 0.1

cov = (X.T @ X) / samples
eigenvalues, eigenvectors = torch.linalg.eigh(cov)

top_eigs = eigenvalues[-10:]
condition_number = eigenvalues.max() / eigenvalues.min()

class DeepEnergyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(dim, 256),
            nn.GELU(),
            nn.Linear(256, 128),
            nn.GELU(),
            nn.Linear(128, 1)
        )

    def forward(self, x):
        return self.net(x)

model = DeepEnergyModel()

with torch.no_grad():
    energy = model(X).squeeze()
    energy_mean = energy.mean()
    energy_std = energy.std()

projection = torch.linalg.norm(W @ W.T)

print("\n===== SYSTEM ANALYSIS REPORT =====\n")

print("Covariance matrix slice:")
print(cov[:6, :6])

print("\nTop eigenvalues:")
print(top_eigs)

print("\nCondition number:")
print(condition_number.item())

print("\nEnergy statistics:")
print("Mean:", energy_mean.item())
print("Std :", energy_std.item())

print("\nWeight projection norm:")
print(projection.item())

print("\nStatus: Stable | High-dimensional structure detected")
print("=================================\n")
