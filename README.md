# Astro-Recognizer
An image classification model from data collection, cleaning, model training, deployment and API integration. <br/>
The model can classify 17 different types of astronomical elements <br/>
The elements are: <br/>

1. Andromeda Galaxy
2. Black Holes
3. Crab Nebula
4. Eagle Nebula
5. Earth Planet
6. Exoplanets
7. Jupiter Planet
8. Mars Planet
9. Mercury Planet
10. Milky Way Galaxy
11. Neptune Planet
12. Orion Nebula
13. Saturn Planet
14. Supernova Remnants
15. Triangulum Galaxy
16. Uranus Planet
17. Venus Planet

# Dataset Preparation
**Data Collection:** Downloaded from DuckDuckGo using term name <br/>
**DataLoader:** Used fastai DataBlock API to set up the DataLoader. <br/>
**Data Augmentation:** fastai provides default data augmentation which operates in GPU. <br/>
Details can be found in `notebooks/data_prep.ipynb`

# Training and Data Cleaning
**Training:** Fine-tuned a resnet34 model for 5 epochs (8 times) and got upto ~86% accuracy. <br/>
**Data Cleaning:** This part took the highest time. Since I collected data from browser, there were many noises. Also, there were images that contained. I cleaned and updated data using fastai ImageClassifierCleaner. I cleaned the data each time after training or finetuning, except for the last time which was the final iteration of the model. <br/>

# Model Deployment
I deployed to model to HuggingFace Spaces Gradio App. The implementation can be found in `deployment` folder or [here](https://huggingface.co/spaces/nosttradamus/astro-recognizer). <br/>
<img src = "deployment/hf_app.png" width="700" height="350">

# API integration with GitHub Pages
The deployed model API is integrated [here](https://shaek666.github.io/Astro-Recognizer/) in GitHub Pages Website. Implementation and other details can be found in `docs` folder.
