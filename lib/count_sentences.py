#!/usr/bin/env python3

import io
import sys

class MyString:
    def __init__(self, value=""):
        self._value = value
    
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
            self._value = ""
        else:
            self._value = new_value

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        if not isinstance(self._value, str):
            print("The value must be a string.")
            return 0
        sentences = [s.strip() for s in self._value.replace('?', '.').replace('!', '.').split('.') if s.strip()]
        return len(sentences)