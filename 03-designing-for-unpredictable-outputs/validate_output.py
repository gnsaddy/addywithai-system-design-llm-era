# Validate + repair LLM output for StudyMate quiz questions. Stdlib, no API key.
# fake_model() stands in for a real LLM: it makes the mistakes real models make.
import json

SCHEMA = {"question": str, "options": list, "answer": int, "why": str}

def validate(text):
    """Return (data, errors). Our code checks the contract, not the model."""
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return None, ["not valid JSON"]
    errors = [f"missing '{k}'" for k in SCHEMA if k not in data]
    errors += [f"'{k}' must be {t.__name__}" for k, t in SCHEMA.items()
               if k in data and not isinstance(data[k], t)]
    if not errors and len(data["options"]) != 4:
        errors.append("need exactly 4 options")
    if not errors and not 0 <= data["answer"] < 4:
        errors.append("answer must be 0-3")
    return (data if not errors else None), errors

REPLIES = [  # what our stand-in model says on try 1, 2 and 3
    'Sure! Here is your quiz: {"question": "What does osmosis move?"}',
    '{"question": "What does osmosis move?", "options": ["Water", "Salt",'
    ' "Light", "Heat"], "answer": 7, "why": "Water crosses the membrane."}',
    '{"question": "What does osmosis move?", "options": ["Water", "Salt",'
    ' "Light", "Heat"], "answer": 0, "why": "Water crosses the membrane."}',
]

def fake_model(prompt, attempt):
    return REPLIES[min(attempt, len(REPLIES) - 1)]

FALLBACK = {"question": "Quiz is not ready yet. Try again soon.",
            "options": ["OK", "-", "-", "-"], "answer": 0, "why": ""}

def get_quiz(topic, max_tries=3):
    prompt = f"Write one quiz question about {topic}. Reply with JSON only."
    for attempt in range(max_tries):
        data, errors = validate(fake_model(prompt, attempt))
        print(f"try {attempt + 1}: {'OK' if data else '; '.join(errors)}")
        if data:
            return data
        prompt += f"\nYour last reply had errors: {errors}. Fix them."
    return FALLBACK  # graceful failure: a safe default, never a crash

def grade(quiz, picked):
    return picked == quiz["answer"]  # plain code grades, never the LLM

quiz = get_quiz("osmosis")
print(quiz["question"], "| correct:", quiz["options"][quiz["answer"]])
print("student picked 0 ->", "correct" if grade(quiz, 0) else "wrong")
