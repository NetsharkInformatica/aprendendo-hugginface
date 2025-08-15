
from transformers import pipeline

image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")

text=image_to_text("img/onca2.jpg")

# [{'generated_text': 'a soccer game with a player jumping to catch the ball '}]

print(text)

