from datetime import datetime


THREAT_RULES = [
    {"name": "Known Malicious IP", "weight": 0.9, "fields": ["src_ip"], "keywords": ["malicious", "c2", "botnet"]},
    {"name": "Port Scan Detected", "weight": 0.7, "fields": ["reason"], "keywords": ["port_scan", "scanning"]},
    {"name": "Brute Force Attempt", "weight": 0.85, "fields": ["reason"], "keywords": ["brute_force", "auth_failure"]},
    {"name": "Data Exfiltration", "weight": 0.95, "fields": ["bytes_out", "destination"], "keywords": ["large_transfer", "unknown_dest"]},
    {"name": "Suspicious Process", "weight": 0.75, "fields": ["process_name"], "keywords": ["powershell", "wscript", "cmd"]},
]


class IOC:
    def __init__(self, value: str, ioc_type: str, source: str = ""):
        self.value = value
        self.ioc_type = ioc_type
        self.source = source
        self.timestamp = datetime.now()
        self.score = 0.5

    def __repr__(self):
        return f"IOC({self.ioc_type}: {self.value}, score={self.score})"


class ThreatInference:
    def __init__(self):
        self.iocs: list[IOC] = []
        self.alerts: list[dict] = []

    def add_ioc(self, ioc: IOC):
        self.iocs.append(ioc)

    def correlate(self, event: dict) -> dict | None:
        total_weight = 0.0
        matched_rules = []

        for rule in THREAT_RULES:
            for field in rule["fields"]:
                val = str(event.get(field, "")).lower()
                if any(kw in val for kw in rule["keywords"]):
                    matched_rules.append(rule)
                    total_weight += rule["weight"]
                    break

        if not matched_rules:
            return None

        severity = min(total_weight / len(matched_rules), 1.0) if matched_rules else 0

        alert = {
            "event": event,
            "matched_rules": [r["name"] for r in matched_rules],
            "severity": round(severity, 2),
            "timestamp": datetime.now().isoformat(),
        }
        self.alerts.append(alert)
        return alert

    def get_alerts(self, min_severity: float = 0.0) -> list[dict]:
        return [a for a in self.alerts if a["severity"] >= min_severity]
