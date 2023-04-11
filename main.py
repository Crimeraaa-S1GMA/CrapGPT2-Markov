# Code shamelessly stolen from ChatGPT's reply
#
# CRAPGPT
#
# MADE BY CRIMERAAA-S1GMA

import markovify

print("Loading corpus...")

# Get raw text as string
with open("corpus.txt", encoding="utf-8") as f:
    text = f.read()

print("Training model...")

# Build the model
text_model = markovify.Text(text, state_size=3)

print("Standalone sentence: " + text_model.make_sentence())

while True:
    try:
        print("\nStart of continued sentence: ", end="")

        start = input()

        print("Continued sentence: " + text_model.make_sentence_with_start(start))
    except KeyError:
        print("The model could not make a sentence from this start. Try again with this or another string.")
    except markovify.text.ParamError:
        print("The model could not make a sentence from this start. Try again with this or another string.")
