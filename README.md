# The Chinese Room

The Chinese Room argument is the concept about a thought experiment described by philosopher of John Searle, 1980.

The discrete concent had been made by Gottfried Leibniz, Peter Winch, and mores. Main idea mimics:
- A room with one American (or anywhere, who exactly know nothing about chinese language).
- A set of tools: a book of instruction manual and box(es) which is full of chinese text.
    - The book includes guildline following the format of table such: `if getting ... then ...`
- Process of interaction: The people outside gives a question, the man inside the room looks up inside the book, combines words and responds.

In this repository, considered constructing a Python project which simulates "Chinese Room", demonstrate the main concept of Searle, comprehensibly.

## Project structure:

```text
the-chinese-room/
├── src/
│   ├── rules.json              # The room's "rulebook"
│   ├── llm_compare.py          # Compare to real LLM
│   ├── outside.py              # Q&A interface
│   └── room.py                 # Inside logic (reference table)
├── main.py                     # Main source code
└── README.md
```

## Installation and Testing

```bash
git clone https://github.com/vennfungus/the-chinese-room.git
cd game-of-life
```

To deny  failures in printing chinese alphabet, run with the following command:
- `py -X utf8 main.py`      | on Windows
- `python3 -X utf8 main.py` | on MacOS, Linux

