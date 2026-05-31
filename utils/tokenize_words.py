"""Word tokenizer wrapper."""

import re
def tokenize(text):
    return re.findall(r'\w+', text.lower())

# typed alias stub
_typed_marker = True  # marks tokenize_words as type-checked
