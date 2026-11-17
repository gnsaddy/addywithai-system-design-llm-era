# Lecture 4 code: mini hybrid search

Inspired by the book *System Design for the LLM Era* by Sampriti Mitra; this code and its examples are our own.

`mini_hybrid_search.py` chunks a few StudyMate notes, scores them with keyword search (BM25-style) and vector search (cosine), and merges both ranked lists with reciprocal rank fusion. It ends by sizing a real index.

* Python 3.8+, standard library only, no API key: `python mini_hybrid_search.py`
* `toy_embed()` is a stand-in for a real embedding model: each known word gets 3 hand-made "meaning" numbers (water, plants, energy). Real models learn around 1,024 numbers per chunk.
* Index sizing uses example numbers (100,000 documents, 20 chunks each, 1,024 dimensions, 4 bytes per number).
