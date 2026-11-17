# Toy GraphRAG for StudyMate: notes -> entity graph -> walk it to answer. Stdlib.
# fake_extract() stands in for an LLM that pulls (entity, relation, entity) facts.
import re
from collections import defaultdict

NOTES = ["Asha scored low on Osmosis.", "Osmosis is covered in Chapter 3.",
         "Chapter 3 needs Diffusion.", "Diffusion is covered in Chapter 2.",
         "Ravi scored low on Photosynthesis.",
         "Photosynthesis is covered in Chapter 5."]
RELATIONS = ["scored low on", "is covered in", "needs"]

def fake_extract(note):  # a real app asks an LLM for these triples
    for rel in RELATIONS:
        m = re.match(rf"(.+?) {rel} (.+?)\.$", note)
        if m:
            return [(m.group(1), rel, m.group(2))]
    return []

graph = defaultdict(list)  # entity -> [(relation, entity), ...]
def add_note(note):
    for a, rel, b in fake_extract(note):
        graph[a].append((rel, b))

for note in NOTES:
    add_note(note)

def vector_like(question):  # stand-in for vector search: shared words only
    q = set(question.lower().strip("?").split())
    return [n for n in NOTES if q & set(n.lower().strip(".").split())]

def walk(start, hops=3):  # follow edges from one entity, hop by hop
    path, node = [], start
    for _ in range(hops):
        if not graph[node]:
            break
        rel, nxt = graph[node][0]
        path.append(f"{node} --{rel}--> {nxt}")
        node = nxt
    return path

question = "What should Asha revise?"
print("vector hits:", vector_like(question))
path = walk("Asha", hops=4)
print("graph path:")
for step in path:
    print("  " + step)
context = vector_like(question) + path  # combine both for the prompt
print(f"context for the LLM: {len(context)} facts")

add_note("Chapter 2 needs Water basics.")  # fresh note: extract only this one
print("after update:", walk("Asha", hops=5)[-1])
