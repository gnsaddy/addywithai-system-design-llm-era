# Lecture 2 code: token budget for StudyMate

Inspired by the book *System Design for the LLM Era* by Sampriti Mitra; this code and its examples are our own.

`token_budget.py` turns tokens into design numbers: does one request fit the context window, what does each feature cost per request and per day, and how long until the first token and the full answer.

* Python 3.8+, standard library only, no API key: `python token_budget.py`
* All prices, speeds and the window size are **example numbers**. Replace them with your provider's real ones.
* `estimate_tokens()` is a rough rule (about 4 characters per English token). Real tokenizers differ by model.
