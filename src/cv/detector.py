import numpy as np


class SimpleObjectDetector:
    def __init__(self, threshold: float = 0.5):
        self.threshold = threshold

    def sliding_window(self, image: np.ndarray, window_size: tuple[int, int], stride: int = 8):
        h, w = image.shape[:2]
        win_h, win_w = window_size
        for y in range(0, h - win_h + 1, stride):
            for x in range(0, w - win_w + 1, stride):
                yield x, y, image[y:y + win_h, x:x + win_w]

    def detect(self, image: np.ndarray, classifier) -> list[dict]:
        detections = []
        for x, y, patch in self.sliding_window(image, (32, 32)):
            score = classifier.predict(patch)
            if score > self.threshold:
                detections.append({"bbox": (x, y, 32, 32), "score": float(score)})
        return detections
