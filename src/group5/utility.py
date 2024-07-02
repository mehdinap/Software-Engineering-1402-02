import random
from .models import Word
from typing import List


class WordListProxy:
    def __init__(self, words: List[Word]):
        self.words: List[Word] = words

    def get_word_list(self):
        return self.words

    def split_random_word_to_pieces(self):
        if self.words:
            word = random.choice(self.words)
            pieces = list(word.exact_word)
            random.shuffle(pieces)  # Randomly shuffle the pieces
            self.words = [w for w in self.words if w.exact_word != word.exact_word]
            return pieces, word.definition
        else:
            return None, None

    def select_random_word_with_three_definitions(self):
        if self.words:
            word = random.choice(self.words)
            other_words = [w for w in self.words if w.exact_word != word.exact_word]
            selected_words = random.sample(other_words, 3)
            definitions = [w.definition for w in selected_words]
            definitions.append(word.definition)
            random.shuffle(definitions)  # Randomly shuffle the definitions
            self.words = [w for w in self.words if w.exact_word != word.exact_word]
            return word.exact_word, word.definition, definitions
        else:
            return None, None, None

    def choose_random_definition_with_three_words(self):
        if self.words:
            word = random.choice(self.words)
            other_words = [w for w in self.words if w.exact_word != word.exact_word]
            selected_words = random.sample(other_words, 3)
            words = [w.exact_word for w in selected_words]
            words.append(word.exact_word)
            random.shuffle(words)  # Randomly shuffle the words
            self.words = [w for w in self.words if w.exact_word != word.exact_word]
            return word.exact_word, word.definition, words
        else:
            return None, None, None
