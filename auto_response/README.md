# Auto Response

Autonomous security response using Reinforcement Learning.

## Approach
- Q-Learning agent for incident response decisions
- Simulated security environment (states: normal, scanning, breach, containment)
- Actions: monitor, block, isolate, report
- Learns optimal response policy

## Usage
```bash
python -m auto_response.src.train
python -m auto_response.src.simulate
```
