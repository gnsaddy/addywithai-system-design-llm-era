# Token budget for StudyMate: tokens, cost and latency per request. Stdlib only.
# All prices and speeds are EXAMPLE numbers. Check your provider's real ones.

def estimate_tokens(text):
    """Rough rule for English: about 4 characters per token."""
    return max(1, round(len(text) / 4))

PRICE_IN, PRICE_OUT = 1.00, 4.00   # $ per 1M tokens (example)
PREFILL, DECODE = 5000, 60         # tokens per second (example)
WINDOW = 32_000                    # context window in tokens (example)

def cost(tin, tout):
    return tin / 1e6 * PRICE_IN + tout / 1e6 * PRICE_OUT

def latency(tin, tout):
    first = 0.3 + tin / PREFILL     # time to first token
    return first, first + tout / DECODE

# One "ask your notes" request: does it fit the window?
question = "Explain osmosis with an example from my notes"
parts = {"system prompt": 600, "notes (5 chunks)": 2500,
         "chat history": 1200, "question": estimate_tokens(question)}
answer_room = 800
used = sum(parts.values()) + answer_room
print(f"context: {used:,} / {WINDOW:,} tokens  fits={used <= WINDOW}")

# The whole app: (name, input tokens, output tokens, requests per day)
MIX = [("ask notes", 5100, 400, 60_000), ("quiz me", 2000, 600, 25_000),
       ("summary", 9000, 700, 10_000), ("daily plan", 1500, 300, 5_000)]
total = 0
for name, tin, tout, n in MIX:
    c = cost(tin, tout)
    first, full = latency(tin, tout)
    total += c * n
    print(f"{name:<10} ${c:.4f}/req  {first:.1f}s / {full:.1f}s  ${c * n:,.0f}/day")
print(f"total: ${total:,.0f}/day  ~${total * 30:,.0f}/month")
