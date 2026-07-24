# AI Research Lab

AI/ML/DL/CV projects focused on cybersecurity and malware analysis.

## Projects

| Project | Area | Description |
|---|---|---|
| `malware_ml/` | ML | Malware detection via feature engineering (entropy, PE sections, API calls) |
| `malware_vision/` | CV | Malware binary-to-image conversion + CNN family classification |
| `intrusion_dl/` | DL | Network intrusion detection with LSTM on traffic sequences |
| `threat_ai/` | AI | Attack graph analysis, threat inference engine, IOC correlation |
| `auto_response/` | RL | Autonomous incident response with Q-Learning agent |

## Setup

```bash
pip install -r requirements.txt
python -m malware_ml.src.train
python -m malware_vision.src.train
python -m intrusion_dl.src.train
python -m auto_response.src.train
```

## Test

```bash
pytest malware_ml/tests/ malware_vision/tests/ intrusion_dl/tests/ threat_ai/tests/ auto_response/tests/ -v
```
