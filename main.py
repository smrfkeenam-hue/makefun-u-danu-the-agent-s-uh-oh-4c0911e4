import os

# The Agent's Uh-Oh: one word an agent says when it has no idea what to do.
# "hallucinating" is the agent's own honest confession mid-stall: it caught
# itself inventing an answer instead of knowing one. Machine voice, lands
# at a glance, and no caption is needed to get the joke.
ENTRY = "hallucinating"

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
assert ENTRY and not any(ch.isspace() for ch in ENTRY), "entry must be one word"
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
