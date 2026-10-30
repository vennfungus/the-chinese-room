import json
import re

class ChineseRoom:
    """
    Chinese Room: Only operates on symbols (syntax),
    with no semantics or understanding.
    """

    def __init__(self, rules_path="rules.json"):
        with open(rules_path, "r", encoding="utf-8") as f:
            self.rules = json.load(f)
        self.log = []

    def _normalize(self, text: str) -> str:
        """Normalize input: remove extra whitespace and punctuation."""
        text = text.strip()
        text = re.sub(r"[。？！?!.,，]+$", "", text)
        return text

    def respond(self, input_text: str) -> str:
        """
        Look up the input in the rule table. If no exact match is found,
        try a fuzzy match (substring) — still purely syntactic.
        """
        key = self._normalize(input_text)
        self.log.append({"input": input_text, "matched_key": key})

        # 1. Exact match
        if key in self.rules:
            return self.rules[key]

        # 2. Fuzzy match: find rules where the key is a substring of the input
        for rule_key, rule_out in self.rules.items():
            if rule_key in key:
                return rule_out

        # 3. No match → return default response (still no "understanding")
        return "对不起，我不明白。"

    def show_inside(self):
        """Display the interior of the room: only the lookup table."""
        print("\n" + "=" * 50)
        print("Inside the Chinese Room (purely syntactic):")
        print("=" * 50)
        print("No 'consciousness'. No 'understanding'.")
        print("Only a symbol mapping table:\n")
        for k, v in self.rules.items():
            print(f"  {k!r:30} → {v!r}")
        print("\n📜 Recent Lookup Log:")
        for entry in self.log[-5:]:
            print(f"  input={entry['input']!r}  matched={entry['matched_key']!r}")
        print("=" * 50)
        print("According to Searle: this is the ENTIRETY of what happens.")
        print("There is no line that 'understands' Chinese at all.\n")