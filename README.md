# Tim! (Art Classifier with Grad-Cam Explainability)
Tim is an art classifier which is finetuned on the [Best Artworks of All Time](https://www.kaggle.com/datasets/ikarus777/best-artworks-of-all-time) dataset. (Only including artists with 99 paintings or more)
## Artists
```
name,paintings
Vincent van Gogh,877
Edgar Degas,702
Pablo Picasso,439
Pierre-Auguste Renoir
Albrecht Dürer,328
Paul Gauguin,311
Francisco Goya,291
Rembrandt,262
Alfred Sisley,259
Titian,255
Marc Chagall,239
Rene Magritte,194
Amedeo Modigliani,193
Paul Klee,188
Henri Matisse,186
Andy Warhol,181
Mikhail Vrubel,171
Sandro Botticelli,164
Leonardo da Vinci,143
Peter Paul Rubens,141
Salvador Dali,139
Hieronymus Bosch,137
Pieter Bruegel,134
Diego Velazquez,128
Kazimir Malevich,126
Frida Kahlo,120
Giotto di Bondone,119
Gustav Klimt,117
Raphael,109
Joan Miro,102
Andrei Rublev,99
```
## Setup and Requirements
- 1- Create a virutal environment with the following command.
`python -m venv .venv`
- 2- Activatie your venv. `.venv/Scripts/Activate`
- 3- Install dependecies with pip. `pip install -r requirements.txt` 
- 4- Install [GraphViz](https://graphviz.org/download/). Make sure it's added to PATH.
- 5- Download the [dataset](https://www.kaggle.com/datasets/ikarus777/best-artworks-of-all-time) and put it in the `data` folder. **you might need to rename the zip archive to "dataset.zip" manually.**
## File Structure
The following is the raw structure. Folders and files may be created as you run Tim.
```
├───data
├───documents
│   ├───phase1
│   └───phase2
├───models
├───notebooks
├───results
│   ├───charts
│   │   ├───convnext_tiny_finetuned
│   │   ├───efficientnet_b0_finetuned
│   │   ├───experiments
│   │   │   ├───efficientnet_b0_finetuned_larger_batch
│   │   │   ├───efficientnet_b0_finetuned_larger_batch_no_padding
│   │   │   └───efficientnet_b0_finetuned_no_padding
│   │   ├───resnet50_baseline
│   │   ├───resnet50_finetuned
│   │   └───structures
│   ├───convnext_tiny_finetuned
│   ├───efficientnet_b0_finetuned
│   ├───experiments
│   │   ├───efficientnet_b0_finetuned_larger_batch
│   │   ├───efficientnet_b0_finetuned_larger_batch_no_padding
│   │   └───efficientnet_b0_finetuned_no_padding
│   ├───resnet50_baseline
│   └───resnet50_finetuned
└───source
    ├───experiments
    ├───preprocessing
    └───training
```
## Order of Operation
This section regards result reproducibility.
## Preprocessing
Run scripts in the following order:
- 1- `source\preprocessing\prep.py` Extract the zip archive and clean up our data directory to get rid of unnecessarily nested folders
- 2- `source\preprocessing\name_correction.py` Remove duplicates and rename the artworks to the appropriate name
- 3- `source\preprocessing\resize.py` Resize to 224×224 (Scaling)
- 4- `source\preprocessing\resize_padding.py` Resize to 224×224 (Padding)

Now you can run any of the scirpts in the `source\training` or `source\experiments` to train your desired model.

## Demo
To demo your trained models run the following notebook. `notebooks\interactive_demo.ipynb`

**For the demo to work you'll need `data\classes.csv` and at least one model in the `models\` directory.**
<img width="819" height="1079" alt="image" src="https://github.com/user-attachments/assets/0da7a963-8541-490f-bd90-e178a8f1e059" />

## Trained models
Trained models can be found [here](https://drive.google.com/drive/folders/1kdbbSOqvKl_gjqTs6UscykaOPi98Naie).
