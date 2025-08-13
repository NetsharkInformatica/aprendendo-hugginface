import gradio as gd
from transformers import pipeline
from PIL import Image

def remove_background(img):
    pipeline_model = pipe = pipeline("image-segmentation", model="briaai/RMBG-1.4", trust_remote_code=True)
    mask_pillow= pipeline_model(img, return_mask=True)
    pillow_image = pipeline_model(img)
    return pillow_image

#remove_background("img/carro2.jpg")

app = gd.Interface(
    title= "Remove backgound das imagens",
    description="Faça upload das imagens e remova o  backgroud em um passe de magica",
    fn= remove_background,
    inputs=gd.components.Image(type="pil"),
    outputs=gd.components.Image(type="pil", format="png")
    
    
)

if __name__ == "__main__":
    app.launch(share=True)

    
    