# Threat AI — Artificial Intelligence for Threat Intelligence

**Research Area:** AI Reasoning for Cybersecurity  
**Academic Level:** MTI Graduate Research  

## Problem Statement

Security operations centers (SOCs) face alert fatigue. AI-driven threat intelligence automates correlation, prioritization, and attack path analysis.

## Methodology

### Attack Graph Analysis
- **Graph Model**: Directed graph of network nodes with risk-weighted edges
- **Path Finding**: BFS for shortest attack path
- **Risk Analysis**: Highest-risk path using weighted priority search

### Threat Inference Engine
- **Rule Base**: 5 correlation rules covering known malicious IPs, port scans, brute force, data exfiltration, suspicious processes
- **IOC Management**: Structured indicator storage with scoring
- **Alert Correlation**: Rule matching with severity calculation

## Key Concepts

- MITRE ATT&CK mapping
- Graph-based security analysis
- Rule-based expert systems for SOC automation

## References

- MITRE ATT&CK Framework. https://attack.mitre.org/
- Noel & Jajodia (2004). "Managing attack graph complexity"

## Usage

```python
from threat_ai.src.graph import AttackGraph
from threat_ai.src.inference import ThreatInference
```
