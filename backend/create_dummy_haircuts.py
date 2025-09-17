import cv2
import numpy as np
from pathlib import Path

# Pasta onde os cortes ficarão salvos
output_dir = Path(__file__).resolve().parent / "app" / "assets" / "haircuts"
output_dir.mkdir(parents=True, exist_ok=True)

def create_dummy_haircut(filename: str, color: tuple[int, int, int]):
    """
    Cria um PNG com uma forma colorida simulando um "corte de cabelo".
    - filename: nome do arquivo (ex: "buzzcut.png")
    - color: cor no formato (B, G, R)
    """
    img = np.zeros((300, 400, 4), dtype=np.uint8)  # 4 canais = BGRA

    # Desenha uma forma oval simulando cabelo
    cv2.ellipse(img, (200, 150), (180, 100), 0, 0, 360, (*color, 255), -1)

    # Salva com transparência
    path = output_dir / filename
    cv2.imwrite(str(path), img)
    print(f"Created {path}")

# Criar cortes de teste
create_dummy_haircut("buzzcut.png", (0, 0, 255))   # vermelho
create_dummy_haircut("mohawk.png", (0, 255, 0))    # verde
create_dummy_haircut("undercut.png", (255, 0, 0))  # azul
