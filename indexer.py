import os
import gzip
import json
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re

#if you have not downloaded these then do so
# nltk.download('punkt')
# nltk.download('stopwords')

def preprocess_text(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t.isalpha()]
    stop_words = set(stopwords.words('english'))
    tokens = [t for t in tokens if t not in stop_words]
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(t) for t in tokens]
    return tokens

def extract_docs_from_file(file_content):
    docs = []
    #file gets split via <DOC> parts
    raw_docs = re.findall(r"<DOC>(.*?)</DOC>", file_content, re.DOTALL)
    for raw_doc in raw_docs:
        docno_match = re.search(r"<DOCNO>(.*?)</DOCNO>", raw_doc)
        if not docno_match:
            continue
        doc_id = docno_match.group(1).strip()
        soup = BeautifulSoup(raw_doc, "html.parser")
        text = soup.get_text(" ", strip=True)
        docs.append((doc_id, text))
    return docs

def build_index(data_dir='data'):
    inverted_index = {}
    doc_count = 0

    for subdir in ['WT01', 'WT02', 'WT03']:
        subdir_path = os.path.join(data_dir, subdir)
        print(f"Folder is being analyzed: {subdir_path}")

        if not os.path.exists(subdir_path):
            print(f"Sorry, Folder can not be found: {subdir_path}")
            continue

        for filename in os.listdir(subdir_path):
            if not filename.lower().endswith('.gz'):
                continue

            file_path = os.path.join(subdir_path, filename)

            try:
                with gzip.open(file_path, 'rt', encoding='utf-8', errors='ignore') as f:
                    file_content = f.read()

                docs = extract_docs_from_file(file_content)

                for doc_id, text in docs:
                    tokens = preprocess_text(text)
                    if not tokens:
                        print(f"There are no tokens in {doc_id}")
                        continue

                    for token in tokens:
                        if token not in inverted_index:
                            inverted_index[token] = {}
                        inverted_index[token][doc_id] = inverted_index[token].get(doc_id, 0) + 1

                    doc_count += 1

            except Exception as e:
                print(f"Sorry, there is an error processing {filename}: {e}")

    index_data = {
        "doc_count": doc_count,
        "index": inverted_index
    }

    return index_data

if __name__ == "__main__":
    index_data = build_index(data_dir="data")
    with open("index.json", "w", encoding="utf-8") as out:
        json.dump(index_data, out)
    print(f" Done Indexing {index_data['doc_count']} documents. It has been saved to index.json")
