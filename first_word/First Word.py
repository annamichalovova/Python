def first_word(text: str) -> str:
    text = text.replace('.', ' ').replace(',', ' ').strip()
    text = text.split()
    return text[0]
print(first_word("Greetings Hello"))
