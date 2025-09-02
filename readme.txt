# Information Retrieval Project

## 📌 Overview

This project implements a simple **document ranking and retrieval system** for an information retrieval assignment.
Given a set of **20 topics** and a **document collection**, the system retrieves the most relevant documents for each topic using weighting functions and ranking algorithms.

The output is a results file containing the **top ranked documents** for each topic in a standardized format.

## 🎯 Objectives

* Parse queries (topics) and extract useful fields such as **title**, **description**, and **narrative**.
* Implement a retrieval method that scores documents using similarity and weighting functions (e.g., TF-IDF, BM25, cosine similarity).
* Rank documents by score and output the top results.
* Generate an output file following the **TREC standard format**.

## 📂 Output Format

The results file will contain ranked documents in the following format:

```
TopicID Q0 DocID Rank Score GroupID
```

* **TopicID** → ID of the query/topic (e.g., 401)
* **Q0** → A fixed string (“Q0”) as per format requirement
* **DocID** → Identifier of the retrieved document
* **Rank** → Rank position of the document for the topic
* **Score** → Retrieval score assigned to the document
* **GroupID** → Identifier of the team/author

Example line:

```
401 Q0 WT24-B28-147 1 6.7146 Group01
```

---

## ⚙️ Features

* Flexible use of **title, description, narrative** for query formulation.
* Support for **top-k document retrieval** (up to 1000 docs per topic).
* Modular design: retrieval functions and ranking functions can be swapped easily.

---

## 🚀 How to Run

1. Place your collection of documents in the `/data` folder.
2. Run the query parser to prepare topic queries.
3. Execute the retrieval engine with your chosen weighting function.
4. Results will be written in the specified format.

---

## 📊 Example Result Snippet

```
401 Q0 DOC123 1 7.83 Group01
401 Q0 DOC987 2 7.10 Group01
401 Q0 DOC654 3 6.95 Group01
...
```

---

## 👥 Authors

* Saad Shahid
* Brandon Lu
* Frank
* Tri Nguyen
* Mark

Course: **ITEC3020 – Web Technologies**
Final Project, York University

---

Data files are not present because they are too large.
