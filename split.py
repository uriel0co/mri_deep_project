import numpy as np
import SimpleITK as sitk
import os
join = os.path.join 
from skimage import transform, io, segmentation
from tqdm import tqdm
import torch
from segment_anything import SamPredictor, sam_model_registry
from segment_anything.utils.transforms import ResizeLongestSide
import argparse

import os
import glob

def split_nii_files(data_dir, train_dir, test_dir, type):
    """Splits the nii files in data_dir into train and test sets.

    Args:
    data_dir: The directory containing the nii files.
    train_dir: The directory where the train nii files should be saved.
    test_dir: The directory where the test nii files should be saved.
    """
    type = "_" + type + ".nii"
    for directory in os.listdir(data_dir):
        train_files = []
        test_files = []

        for filename in glob.glob(os.path.join(data_dir, directory, "*.nii")):
            #if filename.endswith("_seg.nii"):
                #test_files.append(filename)

            if filename.endswith(type):
                train_files.append(filename)

        os.makedirs(os.path.join(train_dir, directory), exist_ok=True)
        os.makedirs(os.path.join(test_dir, directory), exist_ok=True)

        for filename in train_files:
            os.system(f"cp {filename} {os.path.join(train_dir, directory)}")

        for filename in test_files:
            os.system(f"cp {filename} {os.path.join(test_dir, directory)}")



def flatten_nii_files(data_dir):
  """Flattens the .nii files in data_dir.

  Args:
    data_dir: The directory containing the .nii files.
  """

  for directory in os.listdir(data_dir):
        for filename in glob.glob(os.path.join(data_dir, directory, "*.nii")):
            os.system(f"cp {filename} {data_dir}")




data_dir = "BraTS2020_TrainingData/MICCAI_BraTS2020_TrainingData"
train_dir = "medsam_train_data"
test_dir = "medsam_test_data"

# split_nii_files(data_dir, train_dir, test_dir, type="t2")
flatten_nii_files("medsam_seg_map_data")

