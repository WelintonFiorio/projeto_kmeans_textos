# src/convert_reuters.py

import os
from bs4 import BeautifulSoup
from sklearn.model_selection import train_test_split


def parse_reuters_sgm(file_path):
    with open(file_path, 'r', encoding='latin1') as f:
        soup = BeautifulSoup(f, "html.parser")
    reuters_docs = soup.find_all("reuters")

    documentos = []
    for doc in reuters_docs:
        topics = doc.topics.find_all("d")
        text_tag = doc.find("text")
        if topics and text_tag:
            text_body = text_tag.get_text()
            for t in topics:
                documentos.append((t.get_text(), text_body))
    return documentos


def salvar_docs(doc_list, base_out="data/C50/C50train"):
    for categoria, texto in doc_list:
        path_cat = os.path.join(base_out, categoria)
        os.makedirs(path_cat, exist_ok=True)
        # cria arquivo com nome único
        i = len(os.listdir(path_cat)) + 1
        file_path = os.path.join(path_cat, f"{i}.txt")
        with open(file_path, "w", encoding="latin1") as f:
            f.write(texto)


if __name__ == "__main__":
    sgm_folder = "data/reuters21578"
    sgm_files = [os.path.join(sgm_folder, f) for f in os.listdir(sgm_folder) if f.endswith(".sgm")]

    all_docs = []
    for f in sgm_files:
        all_docs.extend(parse_reuters_sgm(f))

    # Dividir em treino/teste (80%/20%)
    train_docs, test_docs = train_test_split(all_docs, test_size=0.2, random_state=42)

    salvar_docs(train_docs, base_out="data/C50/C50train")
    salvar_docs(test_docs, base_out="data/C50/C50test")

    print("Conversão concluída!")
