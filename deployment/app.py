from fastai.vision.all import *
import gradio as gr

astronomy_labels = (
'Andromeda Galaxy',
 'Black Holes',
 'Crab Nebula',
 'Eagle Nebula',
 'Earth Planet',
 'Exoplanets',
 'Jupiter Planet',
 'Mars Planet',
 'Mercury Planet',
 'Milky Way Galaxy',
 'Neptune Planet',
 'Orion Nebula',
 'Saturn Planet',
 'Supernova Remnants',
 'Triangulum Galaxy',
 'Uranus Planet',
 'Venus Planet'
)

model = load_learner('models/astronomy-recognizer-v7.pkl')

def recognize_image(image):
  pred, idx, probs = model.predict(image)
  return dict(zip(astronomy_labels, map(float, probs)))

image = gr.Image()
label = gr.Label()
examples = [
    'test_images/andromeda_test.jpg',
    'test_images/blackhole_test.jpg',
    'test_images/milkyway_test.webp',
    'test_images/venus_test.webp'
    ]

iface = gr.Interface(fn=recognize_image, inputs=image, outputs=label, examples=examples)
iface.launch(inline=False)