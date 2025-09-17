import cv2
import numpy as np
import mediapipe as mp
import io

mp_selfie_segmentation = mp.solutions.selfie_segmentation

def process_image(image_bytes: bytes):
    
    # Lê bytes e converte em imagens
    npimg = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    # Segmentação com MediaPipe
    with mp_selfie_segmentation.SelfieSegmentation(model_selection=1) as segment:
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = segment.process(rgb)

        mask = results.segmentation_mask
        condition = mask > 0.6

        # fundo branco, recortando pessoa/cabelo
        bg = np.ones(img.shape, dtype=np.uint8) * 255
        output = np.where(condition[..., None], img, bg)

    # Retorna a imagem como stream
    _, encoded = cv2.imencode('.jpg', output)
    return io.BytesIO(encoded.tobytes())