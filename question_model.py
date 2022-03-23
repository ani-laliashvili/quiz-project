class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def follow(self, user):
        user.followers += 1
        self.following += 1
