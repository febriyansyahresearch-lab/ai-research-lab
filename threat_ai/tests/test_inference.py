import pytest
from threat_ai.src.inference import ThreatInference, IOC


def test_ioc_creation():
    ioc = IOC("192.168.1.1", "ip", "abuseipdb")
    assert ioc.value == "192.168.1.1"
    assert ioc.score == 0.5


def test_correlation_match():
    engine = ThreatInference()
    event = {"src_ip": "malicious_c2_server", "reason": "port_scan_detected"}
    alert = engine.correlate(event)
    assert alert is not None
    assert alert["severity"] > 0


def test_correlation_no_match():
    engine = ThreatInference()
    event = {"src_ip": "192.168.1.1", "action": "ALLOW"}
    alert = engine.correlate(event)
    assert alert is None
