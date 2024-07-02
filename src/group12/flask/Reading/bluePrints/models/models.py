

class Answer:
    def __init__(self, text, correct):
        self.text = text
        self.correct = correct

class Question:
    def __init__(self, text, answers):
        self.text = text
        self.answers = answers  

class Reading:
    def __init__(self, title, text, questions):
        self.title = title
        self.text = text
        self.questions = questions  

readings = [
    Reading(
        title="Reading 1",
        text="This is the first reading passage.",
        questions=[
            Question(
                text="What is the main idea of the passage?",
                answers=[
                    Answer(text="Main idea 1", correct=True),
                    Answer(text="Main idea 2", correct=False),
                    Answer(text="Main idea 3", correct=False),
                    Answer(text="Main idea 4", correct=False)
                ]
            ),
            Question(
                text="What is the second question?",
                answers=[
                    Answer(text="Answer 1", correct=False),
                    Answer(text="Answer 2", correct=True),
                    Answer(text="Answer 3", correct=False),
                    Answer(text="Answer 4", correct=False)
                ]
            ),
            Question(
                text="What is the third question?",
                answers=[
                    Answer(text="Answer 1", correct=False),
                    Answer(text="Answer 2", correct=False),
                    Answer(text="Answer 3", correct=True),
                    Answer(text="Answer 4", correct=False)
                ]
            ),
            Question(
                text="What is the fourth question?",
                answers=[
                    Answer(text="Answer 1", correct=False),
                    Answer(text="Answer 2", correct=False),
                    Answer(text="Answer 3", correct=False),
                    Answer(text="Answer 4", correct=True)
                ]
            )
        ]
    ),
    Reading(
        title="Reading 2",
        text="This is the second reading passage.",
        questions=[
            Question(
                text="What is the main idea of the second passage?",
                answers=[
                    Answer(text="Main idea 1", correct=False),
                    Answer(text="Main idea 2", correct=True),
                    Answer(text="Main idea 3", correct=False),
                    Answer(text="Main idea 4", correct=False)
                ]
            ),
            Question(
                text="What is the second question of the second passage?",
                answers=[
                    Answer(text="Answer 1", correct=False),
                    Answer(text="Answer 2", correct=False),
                    Answer(text="Answer 3", correct=True),
                    Answer(text="Answer 4", correct=False)
                ]
            ),
            Question(
                text="What is the third question of the second passage?",
                answers=[
                    Answer(text="Answer 1", correct=True),
                    Answer(text="Answer 2", correct=False),
                    Answer(text="Answer 3", correct=False),
                    Answer(text="Answer 4", correct=False)
                ]
            ),
            Question(
                text="What is the fourth question of the second passage?",
                answers=[
                    Answer(text="Answer 1", correct=True),
                    Answer(text="Answer 2", correct=False),
                    Answer(text="Answer 3", correct=True),
                    Answer(text="Answer 4", correct=False)
                ]
            )
        ]
    ),
    Reading(
        title="Reading 3",
        text="This is the third reading passage.",
        questions=[
            Question(
                text="What is the main idea of the third passage?",
                answers=[
                    Answer(text="Main idea 1", correct=False),
                    Answer(text="Main idea 2", correct=True),
                    Answer(text="Main idea 3", correct=False),
                    Answer(text="Main idea 4", correct=False)
                ]
            ),
            Question(
                text="What is the second question of the third passage?",
                answers=[
                    Answer(text="Answer 1", correct=False),
                    Answer(text="Answer 2", correct=False),
                    Answer(text="Answer 3", correct=True),
                    Answer(text="Answer 4", correct=False)
                ]
            ),
            Question(
                text="What is the third question of the third passage?",
                answers=[
                    Answer(text="Answer 1", correct=True),
                    Answer(text="Answer 2", correct=False),
                    Answer(text="Answer 3", correct=False),
                    Answer(text="Answer 4", correct=False)
                ]
            ),
            Question(
                text="What is the fourth question of the third passage?",
                answers=[
                    Answer(text="Answer 1", correct=True),
                    Answer(text="Answer 2", correct=False),
                    Answer(text="Answer 3", correct=True),
                    Answer(text="Answer 4", correct=False)
                ]
            )
        ]
    )
]
