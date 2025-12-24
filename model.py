import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import math

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len=5000):
        super().__init__()
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2) * (-math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0)
        self.register_buffer('pe', pe)

    def forward(self, x):
        return x + self.pe[:, :x.size(1)]

class TransformerModel(nn.Module):
    def __init__(self, input_dim, d_model, n_heads, num_layers, output_dim):
        super().__init__()
        self.embedding = nn.Linear(input_dim, d_model)
        self.pos_encoder = PositionalEncoding(d_model)
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=n_heads,
            dim_feedforward=2048,
            dropout=0.1,
            batch_first=True
        )
        self.transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        self.fc_out = nn.Linear(d_model, output_dim)

    def forward(self, x):
        x = self.embedding(x)
        x = self.pos_encoder(x)
        x = self.transformer_encoder(x)
        x = x.mean(dim=1)
        return self.fc_out(x)

def generate_synthetic_data(samples, seq_len, features):
    x = np.random.randn(samples, seq_len, features)
    y = np.sum(x, axis=(1,2))
    y = (y > 0).astype(int)
    return torch.tensor(x, dtype=torch.float32), torch.tensor(y, dtype=torch.long)

model = TransformerModel(
    input_dim=16,
    d_model=128,
    n_heads=8,
    num_layers=6,
    output_dim=2
).to(device)

optimizer = optim.AdamW(model.parameters(), lr=3e-4)
criterion = nn.CrossEntropyLoss()

x_train, y_train = generate_synthetic_data(2048, 32, 16)
x_train, y_train = x_train.to(device), y_train.to(device)

model.train()
for epoch in range(50):
    optimizer.zero_grad()
    outputs = model(x_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer.step()

weights = torch.cat([p.flatten() for p in model.parameters()])
projection = torch.linalg.norm(weights)

print(loss.item(), projection.item())
