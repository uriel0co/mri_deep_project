# Deep-learning applications in MRI (336028) - Final Project - Finetuning SAM segmentation model for Brats2020 Dataset - Uriel Cohen & Matan Millionschik - Technion, Israel

## Runtime and system requirements
Finetuning SAM with 16 images took 40 seconds per epoch, which is approximaly an hour for 100 epochs we used.
We used a RTX A6000 GPU. The process used 5108 MiB of GPU memory.

## Installation:
1. Create a new conda env using the provided environment.tml file `conda env create -f environment.yml` and activate it `conda activate uriel_sam_clean`
2. Clone this project `git clone https://github.com/uriel0co/mri_deep_project.git`
3. 

## SAM checkpoint Download
Download [SAM checkpoint](https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b_01ec64.pth) and place it at `-workdir-/SAM/sam_vit_b_01ec64.pth`

## Data Download
A link for the Brats2020 Dataset: https://www.kaggle.com/datasets/awsaf49/brats20-dataset-training-validation

We have used only the training dataset, i.e. 'BraTS2020_TrainingData' directory, since we needed the segmentation mask for our self evaluation.

## Data Preprocessing

### Data Splitting
Run the following code: 

```bash
python split.py
```

- This code splits the BraTS2020_TrainingData for a new train and test directories

### Data Preprocesses

Run the following code:

```bash
python pre_MRI.py
```

## We are ready for 👌tuning

Run the following code:

```bash
python finetune.py
```

# Some Results

![image](https://github.com/uriel0co/mri_deep_project/assets/76814133/f2f75556-fa7c-4368-98f5-54d4a1ba07f9)



![image](https://github.com/uriel0co/mri_deep_project/assets/76814133/e30587d4-11ce-4d90-a3eb-a5a853432b3b)


## Acknowledgements
- We thank BoWang's Lab at University of Toronto, for providing the framework for finetuning SAM ['MedSAM'](https://github.com/bowang-lab/MedSAM/tree/main).
- We highly appreciate all the challenge organizers and dataset owners for providing the public dataset to the community. 
- We thank Meta AI for making the source code of [segment anything](https://github.com/facebookresearch/segment-anything) publicly available.
- We also thank Alexandre Bonnet for sharing this great [blog](https://encord.com/blog/learn-how-to-fine-tune-the-segment-anything-model-sam/)
