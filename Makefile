.PHONY: setup test train-all lint clean

setup:
	pip install -r requirements.txt

test:
	pytest malware_ml/tests/ malware_vision/tests/ intrusion_dl/tests/ threat_ai/tests/ auto_response/tests/ rag_chatbot/tests/ -v

train-all:
	python -m malware_ml.src.train
	python -m malware_vision.src.train
	python -m intrusion_dl.src.train
	python -m auto_response.src.train

lint:
	ruff check . --ignore E501 || true

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
