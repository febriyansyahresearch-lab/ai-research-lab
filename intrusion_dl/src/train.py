import torch
import torch.nn as nn
import torch.optim as optim
import os
from intrusion_dl.src.model import IntrusionLSTM
from intrusion_dl.src.data import get_loaders


MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "models")


def train(epochs: int = 10):
    train_loader, test_loader = get_loaders(batch_size=32)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = IntrusionLSTM().to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(epochs):
        model.train()
        total_loss = 0
        for X, y in train_loader:
            X, y = X.to(device), y.to(device)
            optimizer.zero_grad()
            loss = criterion(model(X), y)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        print(f"Epoch {epoch+1}/{epochs}, Loss: {total_loss/len(train_loader):.4f}")

    model.eval()
    correct = total = 0
    with torch.no_grad():
        for X, y in test_loader:
            X, y = X.to(device), y.to(device)
            preds = model(X).argmax(dim=1)
            correct += (preds == y).sum().item()
            total += y.size(0)
    print(f"Test Accuracy: {100 * correct / total:.2f}%")

    os.makedirs(MODEL_DIR, exist_ok=True)
    torch.save(model.state_dict(), os.path.join(MODEL_DIR, "intrusion_lstm.pt"))
    print("Model saved to models/intrusion_lstm.pt")


if __name__ == "__main__":
    train()
