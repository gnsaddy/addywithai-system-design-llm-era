# Lecture 5 code: toy GraphRAG

Inspired by the book *System Design for the LLM Era* by Sampriti Mitra; this code and its examples are our own.

`graph_rag_toy.py` turns six StudyMate notes into (entity, relation, entity) triples, builds a small graph, and walks it to answer "What should Asha revise?". Vector-style search finds 1 note; the graph walk finds a 4-hop path to the real answer. It ends with an incremental update: one new note is extracted and the walk grows by one hop, with no rebuild.

* Python 3.8+, standard library only, no API key: `python graph_rag_toy.py`
* `fake_extract()` is a stand-in for an LLM that extracts triples (it matches 3 sentence patterns). In a real app, ask the model for JSON triples and validate them (see Lecture 3).
* `vector_like()` is a stand-in for vector search (shared words only). See Lecture 4 for real hybrid search.
