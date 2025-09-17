"""
Hair overlay service.
Responsável por aplicar PNG transparente (haircut) sobre a cabeça detectada.
"""

import cv2
import numpy as np


def apply_haircut(image: np.ndarray, haircut_path: str, face_bbox: tuple[int, int, int, int]):
    """Aplica o haircut sobre a região do rosto detectada."""
    x, y, w, h = face_bbox

    # carrega corte de cabelo (PNG com transparência)
    overlay_rgba = cv2.imread(haircut_path, cv2.IMREAD_UNCHANGED)
    if overlay_rgba is None:
        return image

    # redimensiona o overlay para a largura do rosto (ajuste simples)
    scale_factor = 1.5  # aumenta um pouco além do rosto
    new_w = int(w * scale_factor)
    new_h = int(overlay_rgba.shape[0] * (new_w / overlay_rgba.shape[1]))
    overlay_resized = cv2.resize(overlay_rgba, (new_w, new_h))

    # separa canais BGR e alfa
    bgr = overlay_resized[:, :, :3]
    mask = overlay_resized[:, :, 3] / 255.0

    # define posição (acima do rosto)
    y1 = max(0, y - new_h // 2)
    y2 = min(image.shape[0], y1 + new_h)
    x1 = max(0, x - (new_w - w) // 2)
    x2 = min(image.shape[1], x1 + new_w)

    # corta overlay se ultrapassar borda
    overlay_crop = bgr[0:(y2 - y1), 0:(x2 - x1)]
    mask_crop = mask[0:(y2 - y1), 0:(x2 - x1)]

    roi = image[y1:y2, x1:x2]

    # aplica overlay (alpha blending)
    for c in range(3):
        roi[:, :, c] = (roi[:, :, c] * (1 - mask_crop) + overlay_crop[:, :, c] * mask_crop)

    image[y1:y2, x1:x2] = roi
    
    return image
