# Information Retrieval Project

## Overview

This project develops a simple document ranking and retrieval system for an information retrieval task.
Given a set of 20 topics and a set of documents, the system retrieves the highest-ranked documents for every topic based on weighting functions and ranking algorithms.

The outcome is an output file of the top-ranked documents per topic in standard TREC format.

## Objectives

* Parse the topics (queries) and extract fields such as title, description, and narrative.
* Use a retrieval algorithm that compares documents using similarity and weighting functions (e.g., TF-IDF, BM25, cosine similarity).
* Rank the documents by score and return the top ones.
* Generate an output file in the TREC standard format.

## Output Format

Results file will contain ranked documents in the following format:

TopicID Q0 DocID Rank Score GroupID

* TopicID → Query/topic ID (e.g., 401)
* Q0 → Fixed string ("Q0") as per format requirement
* DocID → Document identifier retrieved
* Rank → Rank position of document for the topic
* Score → Retrieval score assigned to the document
* GroupID → Team/author identifier

Sample line:

401 Q0 WT24-B28-147 1 6.7146 Group01

## Features

* Title, description, narrative flexible in creating queries.
* Support for top-k document retrieval (max. 1000 docs per topic).
* Modular design: retrieval components and ranking components replaceable.

## How to Run

1. Place your collection of documents in the `/data` directory.
2. Execute query parser to pre-process topic queries.
3. Execute retrieval engine with your chosen weighting function.
4. Results will be in the provided format.

## Example Result Snippet

401 Q0 DOC123 1 7.83 Group01
401 Q0 DOC987 2 7.10 Group01
401 Q0 DOC654 3 6.95 Group01

## Authors

* Saad Shahid
* Brandon Lu
* Frank
* Tri Nguyen
* Mark

Course: ITEC3020 – Web Technologies
Final Project, York University

Data files are not provided because they are too big.
