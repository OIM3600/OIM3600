import json


with open("data/words.txt", "r") as file:
    words_list = file.read().splitlines()


formatted_words = [f'"{word}"' for word in words_list]


js_array = f"const WORDS = [{', '.join(formatted_words)}];"


with open("www/scripts/words2.js", "w") as js_file:
    js_file.write(js_array)
