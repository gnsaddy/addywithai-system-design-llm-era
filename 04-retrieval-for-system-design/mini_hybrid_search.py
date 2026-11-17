# Mini hybrid search over StudyMate notes: keyword + vector + rank fusion. Stdlib.
# toy_embed() stands in for a real embedding model (real ones: ~1,024 numbers).
import math, re

NOTES = """Osmosis moves water through a membrane. Photosynthesis: leaves turn
sunlight into sugar. Mitochondria release energy as ATP. Lab BIO-204: the
osmosis potato experiment. Plants store extra sugar as starch in roots."""

def chunk(text):  # one sentence per chunk (real apps: ~200-500 tokens + overlap)
    return [s.strip() for s in re.split(r"(?<=\.)\s+", " ".join(text.split()))]

def words(text):
    return re.findall(r"[a-z0-9-]+", text.lower())

DOCS = chunk(NOTES)

def keyword_scores(query):  # BM25-style: rare matching words count more
    n = len(DOCS)
    df = {w: sum(w in words(d) for d in DOCS) for w in set(words(query))}
    return [sum(math.log(1 + n / df[w]) for w in set(words(query))
                if w in words(d)) for d in DOCS]

MEANING = {"water": (1, 0, 0), "osmosis": (1, 0, 0), "membrane": (1, 0, 0),
           "plants": (0, 1, 0), "leaves": (0, 1, 0), "sugar": (0, 1, .3),
           "food": (0, 1, .3), "starch": (0, 1, .3), "sunlight": (0, 1, 0),
           "energy": (0, 0, 1), "atp": (0, 0, 1), "potato": (.3, .6, 0)}

def toy_embed(text):
    v = [sum(MEANING.get(w, (0, 0, 0))[i] for w in words(text)) for i in range(3)]
    size = math.sqrt(sum(x * x for x in v)) or 1
    return [x / size for x in v]

def vector_scores(query):  # cosine similarity: close meaning = high score
    q = toy_embed(query)
    return [sum(a * b for a, b in zip(q, toy_embed(d))) for d in DOCS]

def rank(scores):
    order = sorted(range(len(DOCS)), key=lambda i: -scores[i])
    return [i for i in order if scores[i] > 0]

def hybrid(query, k=60):  # reciprocal rank fusion: merge two ranked lists
    fused = {}
    for ranked in (rank(keyword_scores(query)), rank(vector_scores(query))):
        for pos, i in enumerate(ranked):
            fused[i] = fused.get(i, 0) + 1 / (k + pos + 1)
    return sorted(fused, key=lambda i: -fused[i])

for query in ["how do plants make food", "BIO-204"]:
    print(f"query: {query}")
    print("  keyword:", [DOCS[i][:22] for i in rank(keyword_scores(query))][:2])
    print("  vector: ", [DOCS[i][:22] for i in rank(vector_scores(query))][:2])
    print("  hybrid: ", [DOCS[i][:22] for i in hybrid(query)][:2])

docs, chunks_per_doc, dims = 100_000, 20, 1024  # sizing the index (example)
gb = docs * chunks_per_doc * dims * 4 / 1e9
print(f"index: {docs * chunks_per_doc:,} chunks x {dims} dims = {gb:.1f} GB")
