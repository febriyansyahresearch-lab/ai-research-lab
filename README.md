# AI Research Lab

**Febriyansyah** — MTI, IT Security Leader (15+ yrs, Banking)

Academic research and practical experimentation at the intersection of **Artificial Intelligence** and **Cybersecurity**. This repository demonstrates MTI-level competency across five core areas: Machine Learning, Computer Vision, Deep Learning, AI Reasoning, and Reinforcement Learning — all applied to real-world security problems.

## Research Areas & Projects

### 1. Malware Detection — ML (`malware_ml/`)
Traditional ML approach using engineered features:
- PE header parsing (entropy, section sizes, import tables)
- Feature engineering from raw binaries
- RandomForest classifier with balanced class weighting
- CLI for scanning PE files

**References:** Nataraj et al. (2011), "Malware Images"; Kaggle Microsoft Malware Challenge

### 2. Malware Vision — CV (`malware_vision/`)
Computer vision approach inspired by the MalImg method:
- Binary-to-grayscale image conversion (64×64)
- Visual pattern recognition for malware family classification
- Synthetic data generation for Ramnit, Lollipop, Kelihos, Vundo families
- CNN-ready feature extraction pipeline

**References:** Nataraj et al. (2011), "A Survey on Malware Analysis Using Image Processing" — IJERT

### 3. Intrusion Detection — DL (`intrusion_dl/`)
Deep learning for network security:
- LSTM-based sequence classification on traffic flows
- Synthetic network flow generation (8 features, 20-timestep sequences)
- Binary classification: Normal vs Attack
- PyTorch implementation with GPU support

**References:** Hochreiter & Schmidhuber (1997), "LSTM"; CIC-IDS-2017 dataset methodology

### 4. Threat Intelligence — AI (`threat_ai/`)
Symbolic AI for security operations:
- Attack graph construction and path analysis (BFS, risk-weighted search)
- Rule-based threat inference engine (5 correlation rules)
- IOC (Indicator of Compromise) management and scoring
- Real-time alert correlation

**References:** MITRE ATT&CK framework; Noel & Jajodia (2004), "Attack Graph Analysis"

### 5. Autonomous Response — RL (`auto_response/`)
Reinforcement learning for SOAR:
- Q-Learning agent for incident response decisions
- 4-state security environment (normal → scanning → breach → contained)
- 4 actions: monitor, block, isolate, report
- Learns optimal response policy through episode training

**References:** Sutton & Barto (2018), "Reinforcement Learning"; SOAR frameworks (Splunk Phantom, Palo Alto XSOAR)

## Repository Structure

```
ai-research-lab/
├── malware_ml/         ML: feature-based malware detection
├── malware_vision/     CV: image-based malware classification  
├── intrusion_dl/       DL: LSTM network intrusion detection
├── threat_ai/          AI: attack graph & threat inference
├── auto_response/      RL: Q-Learning incident response
└── references/         Academic references & methodology notes
```

## Technical Stack

| Area | Libraries | Concepts |
|---|---|---|
| ML | scikit-learn, numpy | Entropy, PE parsing, RandomForest |
| CV | numpy, (torchvision) | Binary-to-image, MalImg, CNN |
| DL | PyTorch | LSTM, sequence classification |
| AI | Pure Python | Graph search, rule engine, IOC |
| RL | Pure Python | Q-Learning, Markov decision process |

## Setup & Validation

```bash
pip install -r requirements.txt

# Train all models
python -m malware_ml.src.train
python -m malware_vision.src.train
python -m intrusion_dl.src.train
python -m auto_response.src.train

# Run all tests
pytest malware_ml/tests/ malware_vision/tests/ intrusion_dl/tests/ threat_ai/tests/ auto_response/tests/ -v
```

## About the Author

**Febriyansyah** — IT security leader with 15+ years in the banking sector. Currently pursuing a Master's in Information Technology (MTI) with research focus on AI/ML applications for cybersecurity, fraud detection, and threat intelligence.

- Email: febriyansyah.research@gmail.com
- Research interests: ML for security, computer vision for malware, autonomous response systems, threat intelligence automation

## License

MIT — see [LICENSE](LICENSE)
