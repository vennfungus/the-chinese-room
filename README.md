# The Chinese Room Argument
The Chinese room argument holds that a computer executing a program cannot have a mind, understanding, or consciousness, regardless of how intelligently or human-like the program may make the computer behave (Wikipedia), being presented in 1980 by the American philosopher John Searle.Precursor arguments had been made by Gottfried Wilhelm Leibniz, Peter Winch, Anatoly Dneprov, et al.; Searle's version has been widely discussed in the years since.

In this repo, I considered to construct a project of Python that mimics the "Chinese Room", demonstrate the main concept of Searle, clearly.

## Project structure:

```text
the-chinese-room/
├── src/
│   ├── rules.json              # The room's "rulebook"
│   ├── llm_compare.py          # Compare to real LLM
│   ├── outside.py              # Q&A interface
│   ├── room.py                 # Inside logic (reference table)
├── main.py                     # Main source code
└── README.md
```

