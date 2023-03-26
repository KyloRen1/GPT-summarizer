import re

import nltk

nltk.download("punkt")


def clean_text(text: str) -> str:
    text = " ".join(text.split())
    text = remove_special_chars(text)
    sent = split_to_sentences(text)
    return " ".join(sent)


def remove_special_chars(text: str) -> str:
    text = re.sub(r"\W+", " ", text)
    return text


def split_to_sentences(text: str) -> list:
    sentences = nltk.sent_tokenize(text)
    return sentences
