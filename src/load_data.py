# src/load_data.py

import os

def carregar_textos(base_path):
    """
    Lê todos os arquivos .txt da pasta base_path e retorna listas de textos e caminhos.
    """
    textos = []
    arquivos = []

    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(".txt"):
                path = os.path.join(root, file)
                arquivos.append(path)
                with open(path, "r", encoding="latin1") as f:
                    textos.append(f.read())

    return textos, arquivos
