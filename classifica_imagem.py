from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image
import requests

#url = 'http://images.cocodataset.org/val2017/000000039769.jpg'
url="img/cats.jpeg"
#image = Image.open(requests.get(url, stream=True).raw)
image=Image.open(url)

processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224')
model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224')

inputs = processor(images=image, return_tensors="pt")
outputs = model(**inputs)
logits = outputs.logits
# model predicts one of the 1000 ImageNet classes
predicted_class_idx = logits.argmax(-1).item()
print("Predicted class:", model.config.id2label[predicted_class_idx])
