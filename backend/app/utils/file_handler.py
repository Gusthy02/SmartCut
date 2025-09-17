import os
from pathlib import Path

def save_temp_file(content: bytes, filename: str, folder: str = 'temp'):
    os.makedirs(folder, exist_ok=True)
    filepath = Path(folder) / filename
    with open(filepath, 'wb') as f:
        f.write(content)

    return filepath