import requests

# URL da API
BASE_URL = "http://localhost:8000/image"

# 1. Listar cortes
r = requests.get(f"{BASE_URL}/haircuts")
print("Haircuts:", r.json())

# 2. Enviar imagem para processar
with open("meu_rosto.jpg", "rb") as f:
    files = {"file": f}
    r = requests.post(f"{BASE_URL}/process?haircut=buzzcut.png", files=files)

if r.status_code == 200:
    with open("resultado.jpg", "wb") as out:
        out.write(r.content)
    print("✅ Imagem processada salva em resultado.jpg")
else:
    print("❌ Erro:", r.json())
