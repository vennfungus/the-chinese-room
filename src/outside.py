class Outsider:
    """Outsider: only sees input/output, doesn't see inside."""

    def __init__(self, room):
        self.room = room

    def ask(self, question: str):
        answer = self.room.respond(question)
        print(f"\n🧑 You ask: {question}")
        print(f"🏠 The room answers: {answer}")
        return answer