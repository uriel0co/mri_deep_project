# Deep-learning applications in MRI (336028) - Final Project - Finetuning SAM model for Brats2020 Dataset - Uriel Cohen & Matan Millionschik - Technion, Israel

## Runtime and system requirements
Finetuning SAM with 32 images took 80 seconds per epoch, which is approximaly two hours for 100 epochs.
We used a machine with RTX A6000 GPU. The process used 5108 MiB of GPU memory.

## Installation:
1. Create a new conda env using the provided environment.tml file `conda env create -f environment.yml` and activate it `conda activate sam_clean`
2. Clone this project `git clone https://github.com/uriel0co/mri_deep_project.git`

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
- We also thank our lecturer, Prof. Moti Freiman, for a fascinating course and for the opportunity to work on this project.
