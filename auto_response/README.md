# Auto Response — Reinforcement Learning for Autonomous Incident Response

**Research Area:** Reinforcement Learning for SOAR  
**Academic Level:** MTI Graduate Research  

## Problem Statement

Automated incident response (SOAR) requires adaptive decision-making under uncertainty. RL agents can learn optimal response policies through environmental interaction.

## Methodology

### Security Environment
A Markov Decision Process with 4 states:
| State | Description |
|---|---|
| Normal | Baseline, no threats detected |
| Scanning | Reconnaissance activity detected |
| Breach | Active compromise confirmed |
| Contained | Incident isolated, remediation ongoing |

### Agent Design
- **Algorithm**: Q-Learning (off-policy TD control)
- **Actions**: monitor, block_ip, isolate_host, report_incident
- **Reward Structure**: Correct actions rewarded (+1 to +5), incorrect penalized (-1)

### Training
- 500 episodes of experience replay
- ε-greedy exploration (ε=0.2)
- γ=0.95 (long-term reward focus)

## Key Concepts

- Markov Decision Process for security states
- Q-Learning for model-free RL
- SOAR playbook automation

## References

- Sutton & Barto (2018). "Reinforcement Learning: An Introduction"
- Splunk Phantom / Palo Alto XSOAR SOAR frameworks

## Usage

```bash
python -m auto_response.src.train
```
