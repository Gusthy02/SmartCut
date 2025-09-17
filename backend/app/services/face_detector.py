"""
Face detection service.
Usa HaarCascade do OpenCV (gratuito) para detectar rosto.
Retorna bounding box (x, y, w, h) ou None.
"""

import cv2
import numpy as np
from pathlib import Path


# HaarCascade já vem no OpenCV (cv2.data.haarcascades)
CASCADE_PATH = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(CASCADE_PATH)


def detect_face_bbox(image: np.ndarray, min_confidence: float = 0.6):
    """Detecta o rosto principal e retorna (x, y, w, h)."""
    if image is None:
        
        return None

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    if len(faces) == 0:
        
        return None

    # pega o maior rosto detectado (mais provável de ser o cliente)
    x, y, w, h = max(faces, key=lambda f: f[2] * f[3])
    
    return (x, y, w, h)
