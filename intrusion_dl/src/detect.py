import argparse
import torch
import numpy as np
import os
import sys
from intrusion_dl.src.model import IntrusionLSTM

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "intrusion_lstm.pt")
N_FEATURES = 8
SEQ_LENGTH = 20


def load_model():
    if not os.path.exists(MODEL_PATH):
        print("Model not found. Run training first.", file=sys.stderr)
        sys.exit(1)
    model = IntrusionLSTM(n_features=N_FEATURES)
    model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu", weights_only=True))
    model.eval()
    return model


def detect(flows: list[float]) -> dict:
    model = load_model()
    vec = np.array(flows, dtype=np.float32).reshape(1, -1, N_FEATURES)
    with torch.no_grad():
        out = model(torch.tensor(vec))
        proba = torch.softmax(out, dim=1)[0]
        pred = out.argmax(dim=1).item()
    return {
        "prediction": "Attack" if pred == 1 else "Normal",
        "confidence": round(float(proba[pred].item()), 4),
    }


def main():
    parser = argparse.ArgumentParser(description="Network intrusion detector")
    parser.add_argument("--flows", nargs="+", type=float, help="Flow feature vector")
    args = parser.parse_args()

    if args.flows:
        result = detect(args.flows)
        print(f"Prediction: {result['prediction']}")
        print(f"Confidence: {result['confidence']:.2%}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
