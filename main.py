import os
import shutil

pasta_origem = "/storage/emulated/0/Download"

tipos = {
    "PDFs": [".pdf"],
    "Imagens": [".jpg", ".png", ".jpeg"],
    "Musicas": [".mp3"],
    "Videos": [".mp4"],
    "Outros": []
}

for arquivo in os.listdir(pasta_origem):
    caminho_arquivo = os.path.join(pasta_origem, arquivo)

    if os.path.isfile(caminho_arquivo):
        movido = False

        for pasta, extensoes in tipos.items():
            if any(arquivo.lower().endswith(ext) for ext in extensoes):
                os.makedirs(os.path.join(pasta_origem, pasta), exist_ok=True)
                shutil.move(caminho_arquivo, os.path.join(pasta_origem, pasta))
                movido = True
                break

        if not movido:
            os.makedirs(os.path.join(pasta_origem, "Outros"), exist_ok=True)
            shutil.move(caminho_arquivo, os.path.join(pasta_origem, "Outros"))
