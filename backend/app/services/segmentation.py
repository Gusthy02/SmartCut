"""
Segmentation service.
Primeira versão simples: apenas retorna a imagem original.
Depois podemos trocar por MediaPipe SelfieSegmentation ou outro modelo.
"""

import cv2
import numpy as np

def remove_background(image_bytes: bytes) -> np.ndarray:
    """Recebe bytes, decodifica e retorna imagem sem fundo (aqui: apenas ecoa)."""

    npimg = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    # 🚧 Versão mock: não remove fundo, apenas devolve imagem original
    # Futuro: aplicar segmentação real

    return img