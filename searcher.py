import json
import math
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def preprocess_text(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t.isalpha()]
    stop_words = set(stopwords.words('english'))
    tokens = [t for t in tokens if t not in stop_words]
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(t) for t in tokens]
    return tokens

def parse_topics(topics_file):
    topics = []
    with open(topics_file, 'r') as f:
        content = f.read()
    parts = content.split("<top>")
    for part in parts:
        part = part.strip()
        if not part:
            continue
        num_match  = re.search(r"<num>\s*Number:\s*(\d+)", part)
        title_match = re.search(r"<title>\s*(.*?)\s*(?=<desc>)", part, flags=re.DOTALL)
        desc_match  = re.search(r"<desc>\s*Description:\s*(.*?)\s*(?=<narr>)", part, flags=re.DOTALL)
        narr_match  = re.search(r"<narr>\s*Narrative:\s*(.*?)\s*</top>", part, flags=re.DOTALL)
        if not num_match:
            continue
        topic_id = num_match.group(1).strip()
        title_text = title_match.group(1).strip() if title_match else ""
        desc_text  = desc_match.group(1).strip() if desc_match else ""
        narr_text  = narr_match.group(1).strip() if narr_match else ""
        query_text = f"{title_text} {desc_text} {narr_text}".strip()
        topics.append({
            "id": topic_id,
            "title": title_text,
            "desc": desc_text,
            "narr": narr_text,
            "query": query_text
        })
    return topics

def rank_documents(query_tokens, index, doc_count):
    scores = {}
    for term in query_tokens:
        if term not in index:
            continue
        df = len(index[term])
        if df == 0:
            continue
        idf = math.log2(doc_count / df)
        for doc_id, tf in index[term].items():
            score = tf * idf
            scores[doc_id] = scores.get(doc_id, 0.0) + score
    ranked_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return ranked_docs

def save_output(results, output_file):
    with open(output_file, 'w') as f:
        for topic_id, doc_id, rank, score in results:
            line = f"{topic_id} Q0 {doc_id} {rank} {score:.6f} Group6"
            f.write(line + "\n")

if __name__ == "__main__":
    with open("index.json", "r") as jf:
        index_data = json.load(jf)
    doc_count = index_data["doc_count"]
    index = index_data["index"]

    topics = parse_topics("topics.txt")

    trec_results = []
    for topic in topics:
        topic_id = topic["id"]
        query_text = topic["query"]
        query_tokens = preprocess_text(query_text)
        ranked_docs = rank_documents(query_tokens, index, doc_count)
        top_docs = ranked_docs[:1000]
        for rank, (doc_id, score) in enumerate(top_docs, start=1):
            trec_results.append((topic_id, doc_id, rank, score))

    save_output(trec_results, "output.txt")
    print(f"The search results for {len(topics)} topics have been saved to output.txt")
