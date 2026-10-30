from src.room import ChineseRoom
from src.outside import Outsider

BANNER = r"""
╔══════════════════════════════════════════════════════════════╗
║                CHINESE ROOM (SEARLE, 1980)                   ║
║     The Thought Experiment on Artificial Intelligence        ║
╚══════════════════════════════════════════════════════════════╝
"""

def main():
    print(BANNER)
    room = ChineseRoom("rules.json")
    outsider = Outsider(room)

    print("You are an outsider to the room. Please type your question in Chinese.")
    print("(or use the sample questions below).")
    print("Type 'inside' to see the interior of the room.")
    print("Type 'quit' to exit.\n")

    print("Sample questions:")
    for q in room.rules.keys():
        print(f"  - {q}")
    print()

    while True:
        try:
            user_input = input("🧑 > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        if user_input.lower() == "inside":
            room.show_inside()
            continue

        outsider.ask(user_input)

if __name__ == "__main__":
    main()