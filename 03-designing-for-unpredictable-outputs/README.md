# Lecture 3 code: validate and repair LLM output

Inspired by the book *System Design for the LLM Era* by Sampriti Mitra; this code and its examples are our own.

`validate_output.py` treats a JSON schema as a contract for a StudyMate quiz question. It checks every reply (valid JSON, required fields, types, value ranges), sends the exact errors back in a repair prompt, stops after 3 tries, and falls back to a safe default. Grading is done by plain code, never by the model.

* Python 3.8+, standard library only, no API key: `python validate_output.py`
* `fake_model()` is a stand-in for a real LLM. It replies with broken JSON, then an out-of-range answer, then a correct reply, so you can see each path.
* To use a real model, replace `fake_model()` with your provider's call and keep `validate()` exactly as it is.
