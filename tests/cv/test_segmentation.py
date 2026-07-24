import pytest
import numpy as np
from src.cv.segmentation import SimpleSegmenter


def test_segmenter_output_shape():
    image = np.random.randint(0, 255, (32, 32, 3), dtype=np.uint8)
    seg = SimpleSegmenter(n_clusters=3)
    result = seg.kmeans_segment(image)
    assert result.shape == image.shape
    assert result.dtype == np.uint8
